import astroid
from astroid.helpers import safe_infer

from src.analysis.result import Result, CodeSmell
from src.checkers.base_checker import BaseChecker


class BroadcastingFeatureNotUsed(BaseChecker):
    """
    This class scrutinizes the Python code for import statements pertaining to the "tensorflow" library and usage of
    tf.tile() method.
    """

    ID = "CSA16"
    TITLE = "Use the broadcasting feature in deep learning code to be more memory efficient."
    DESCRIPTION = """
    Context:
    Deep learning libraries like PyTorch and TensorFlow supports
    the element-wise broadcasting operation.

    Problem:
    Without broadcasting, tiling a tensor first to match another
    tensor consumes more memory due to the creation and storage
    of a middle tiling operation result.

    Solution:
    With broadcasting, it is more memory efficient. However,
    there is a trade-off in debugging since the tiling process is not
    explicitly stated.
    """

    def __init__(self, filename):
        super().__init__(filename)
        self.code_smell_found = False
        self.has_import = False

        self.tensorflow_alias = set()

    def visit_import(self, node: astroid.Import) -> None:
        if self.has_import or self.code_smell_found:
            return

        for name, alias in node.names:
            if name == "tensorflow":
                if node.names[0][1] is not None:
                    self.tensorflow_alias.add(node.names[0][1])
                else:
                    self.tensorflow_alias.add(node.names[0][0])

                self.has_import = True

    def visit_call(self, node: astroid.Call) -> None:
        if self.code_smell_found or not self.has_import:
            return

        # Check usage of tf.tile()
        if (
                isinstance(node.func, astroid.Attribute)
                and node.func.attrname == "tile"
                and isinstance(node.func.expr, astroid.Name)
                and node.func.expr.name in self.tensorflow_alias
        ):
            self.record_finding(node)
            self.code_smell_found = True

    def record_finding(self, node: astroid.NodeNG) -> None:
        Result.add(CodeSmell(code_smell_id=self.ID,
                             code_smell_title="Broadcasting Feature Not Used",
                             file_path=self.filename,
                             line=node.lineno,
                             col_offset=node.col_offset,
                             smell_type="Generic",
                             description="Use the broadcasting feature in deep learning code to be more memory "
                                         "efficient.",
                             pipeline_stage="Model Training",
                             effect="Efficiency",
                             source_code=node.as_string(),
                             source_astroid_node=f"Astroid AST: {node} \n Code: {node.as_string()}"))
