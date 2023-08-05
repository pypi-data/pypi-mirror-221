import astroid
from astroid.helpers import safe_infer

from src.analysis.result import Result, CodeSmell
from src.checkers.base_checker import BaseChecker


class MemoryNotFreed(BaseChecker):
    """
    This class analyzes Python code to detect potential memory management issues related to
    the "tensorflow" and "pytorch" libraries. It looks for loops in which objects from these
    libraries are created but not properly freed, which could lead to memory exhaustion during
    machine learning model training.
    """

    ID = "CSA12"
    TITLE = "Free memory in time."
    DESCRIPTION = """
    Context:
    Machine learning training is memory-consuming, and
    the machine’s memory is always limited by budget.

    Problem:
    If the machine runs out of memory while training the
    model, the training will fail.

    Solution:
    Some APIs are provided to alleviate the run-out-of-memory
    issue in deep learning libraries. TensorFlow’s documentation
    notes that if the model is created in a loop, it is suggested to use
    clear_session() in the loop. Meanwhile, the GitHub repository
    pytorch-styleguide recommends using .detach() to free the tensor
    from the graph whenever possible. The .detach() API can prevent
    unnecessary operations from being recorded and therefore can save
    memory. Developers should check whether they use this kind
    of APIs to free the memory whenever possible in their code.
    """

    def __init__(self, filename):
        super().__init__(filename)
        # Tensorflow code smell indicators
        self.has_tensorflow_clear_session: bool = False
        self.has_tensorflow_object: bool = False
        self.tensorflow_node = None
        # Torch code smell indicators
        self.has_torch_detach: bool = False
        self.has_torch_object: bool = False
        self.torch_node = None
        # General
        self.code_smell_found: bool = False

    def reset_indicators(self):
        self.has_tensorflow_clear_session = False
        self.has_tensorflow_object = False
        self.has_torch_detach = False
        self.has_torch_object = False
        self.tensorflow_node = None
        self.torch_node = None

    def visit_for(self, node: astroid.For) -> None:
        self.check_memory_not_freed(node=node)

    def visit_while(self, node: astroid.While) -> None:
        self.check_memory_not_freed(node=node)

    def check_memory_not_freed(self, node):
        if self.code_smell_found:
            return
        else:
            self.reset_indicators()

        for sub_node in node.body:
            self.dfs(node=sub_node)

        if self.has_memory_been_freed():
            self.code_smell_found = True

    def dfs(self, node: astroid.NodeNG) -> None:
        if self.code_smell_found:
            return

        if isinstance(node, astroid.Call):
            self.check_for_call(node)
        else:
            inferred_node = safe_infer(node)
            if inferred_node:
                self.check_for_package_module(inferred_node, node)

        for child in node.get_children():
            self.dfs(child)  # recursively call dfs on the child

    def check_for_call(self, node: astroid.Call):
        if isinstance(node.func, astroid.Attribute):
            if node.func.attrname == "clear_session":
                self.has_tensorflow_clear_session = True
            elif node.func.attrname == "detach":
                self.has_torch_detach = True

    def check_for_package_module(self, inferred_node, node):
        if inferred_node.root().name == "tensorflow":
            self.has_tensorflow_object = True
            self.tensorflow_node = node

        if inferred_node.root().name == "torch":
            self.has_torch_object = True
            self.torch_node = node

    def has_memory_been_freed(self) -> bool:
        if self.has_torch_object and not self.has_torch_detach:
            self.record_finding(node=self.torch_node)
            return True
        elif self.has_tensorflow_object and not self.has_tensorflow_clear_session:
            self.record_finding(node=self.tensorflow_node)
            return True

        return False

    def record_finding(self, node: astroid.NodeNG) -> None:
        Result.add(CodeSmell(code_smell_id=self.ID,
                             code_smell_title="Memory Not Freed",
                             file_path=self.filename,
                             line=node.lineno,
                             col_offset=node.col_offset,
                             smell_type="Generic",
                             description="Free memory in time.",
                             pipeline_stage="Model Training",
                             effect="Memory Issue",
                             source_code=node.as_string(),
                             source_astroid_node=f"Astroid AST: {node} \n Code: {node.as_string()}"))
