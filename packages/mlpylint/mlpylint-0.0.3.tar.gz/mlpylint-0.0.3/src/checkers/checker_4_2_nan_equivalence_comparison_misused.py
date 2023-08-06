import astroid
from astroid.helpers import safe_infer

from src.analysis.result import Result, CodeSmell
from src.checkers.base_checker import BaseChecker

COMPARISON_OP = frozenset(("<", "<=", ">", ">=", "!=", "==", "is", "is not"))


class NaNEquivalenceComparisonMisusedChecker(BaseChecker):
    """
    This class inspects the Python code for the import of "numpy" and stores its alias. It also checks for
    'importfrom' statements related to 'numpy.nan' and keeps track of its alias. Furthermore, it reviews comparisons
    involving 'numpy.nan', utilizing the stored alias and the predicted inferred string.
    """

    ID = "CS2"
    TITLE = "The NaN equivalence comparison is different to None comparison. The result of NaN == NaN is False."
    DESCRIPTION = """
    Context:
    NaN equivalence comparison behaves differently from
    None equivalence comparison.

    Problem:
    While None == None evaluates to True, np.nan == np.nan
    evaluates to False in NumPy. As Pandas treats None like np.nan for
    simplicity and performance reasons, a comparison of DataFrame
    elements with np.nan always returns False. If the developer is
    not aware of this, it may lead to unintentional behaviours in the
    code.

    Solution:
    Developers need to be careful when using the NaN comparison.
    """

    def __init__(self, filename):
        super().__init__(filename)
        self.has_numpy_import: bool = False
        self.numpy_alias: set = set()
        self.numpy_nan_alias: set = set()

    def visit_import(self, node: astroid.Import) -> None:
        for name, alias in node.names:
            if name == "numpy":
                if node.names[0][1] is not None:
                    self.numpy_alias.add(node.names[0][1])
                else:
                    self.numpy_alias.add(node.names[0][0])

                self.has_numpy_import = True

    def visit_importfrom(self, node: astroid.ImportFrom) -> None:
        if node.modname == "numpy":
            if any(name in {"nan", "NaN", "NAN"} for name in node.names[0]):
                if node.names[0][1] is not None:
                    self.numpy_nan_alias.add(node.names[0][1])
                else:
                    self.numpy_nan_alias.add(node.names[0][0])

            self.has_numpy_import = True

    def visit_compare(self, node: astroid.Compare) -> None:
        if not self.has_numpy_import:
            return

        # Iterate compare object and search for numpy.nan occurrences and valid operator
        # Check left
        if node.ops[0][0] in COMPARISON_OP and self.check_nan_equivalence_misuse(obj=node.left):
            self.record_finding(node=node)
            return

        # Check ops
        for op, obj in node.ops:
            if (
                op in COMPARISON_OP
                and self.check_nan_equivalence_misuse(obj=obj)
            ):
                self.record_finding(node=node)
                return

        return
        # High precision detection of nan comparison
        # prev_obj = node.left
        # prev_op = node.ops[0][0]
        # for op, obj in node.ops:
        #     if (
        #         prev_op in COMPARISON_OP
        #         and self.check_nan_equivalence_misuse(obj=prev_obj)
        #         and self.check_nan_equivalence_misuse(obj=obj)
        #     ):
        #         self.record_finding(node=node)
        #         return
        #     else:
        #         prev_op = op
        #         prev_obj = obj

    def check_nan_equivalence_misuse(self, obj: astroid.NodeNG) -> bool:
        if isinstance(obj, astroid.Attribute):
            if obj.attrname in {"nan", "NaN", "NAN"} and isinstance(obj.expr, astroid.Name):
                return self.check_attr_name(name=obj.expr)
        elif isinstance(obj, astroid.Name):
            return self.check_name(name=obj)

    def check_attr_name(self, name: astroid.Name) -> bool:
        inferred_node = safe_infer(name)
        # Check if inferred node is numpy module
        if inferred_node and inferred_node.root().name == "numpy":
            return True
        # Check if variable name matches any of the stored numpy alias
        elif name.name in self.numpy_alias:
            return True

        return False

    def check_name(self, name: astroid.Name) -> bool:
        # Check if variable name matches any of the stored numpy nan aliases
        if name.name in self.numpy_nan_alias:
            return True

        return False

    def record_finding(self, node: astroid.Compare) -> None:
        Result.add(CodeSmell(code_smell_id=self.ID,
                             code_smell_title="NaN Equivalence Comparison Misused",
                             file_path=self.filename,
                             line=node.lineno,
                             col_offset=node.col_offset,
                             smell_type="Generic",
                             description="NaN equivalence comparison behaves differently from None "
                                         "equivalence comparison.",
                             pipeline_stage="Data Cleaning",
                             effect="Error-prone",
                             source_code=node.as_string(),
                             source_astroid_node=f"Astroid AST: {node} \n Code: {node.as_string()}"))
