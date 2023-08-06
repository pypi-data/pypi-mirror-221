import astroid
from astroid.helpers import safe_infer

from src.analysis.result import Result, CodeSmell
from src.checkers.base_checker import BaseChecker

PANDAS_READ_METHODS = frozenset(("read_csv",
                        "read_table",
                        "read_sql",
                        "read_xml",
                        "read_json",
                        "read_excel",
                        "read_sql_query",))


class ColumnsAndDataTypeNotExplicitlySet(BaseChecker):
    """
    This class checks function calls for the inferred "pandas" module and the presence of attribute names beginning
    with "read_". It also inspects for the explicit use of keyword arguments "columns" and "dtype" within these
    "read_" method calls.
    """

    ID = "CS4"
    TITLE = "Explicitly select columns and set DataType when importing data."
    DESCRIPTION = """
    Context:
    In Pandas, all columns are selected by default when a
    DataFrame is imported from a file or other sources. The data type
    for each column is defined based on the default dtype conversion.

    Problem:
    If the columns are not selected explicitly, it is not easy
    for developers to know what to expect in the downstream data
    schema. If the datatype is not set explicitly, it may silently
    continue the next step even though the input is unexpected, which
    may cause errors later. The same applies to other data importing
    scenarios.

    Solution:
    It is recommended to set the columns and DataType explicitly in data processing.
    """

    def __init__(self, filename):
        super().__init__(filename)

    def visit_call(self, node: astroid.nodes.Call):
        has_pandas_module = False
        if (
                isinstance(node.func, astroid.Attribute)
                and isinstance(node.func.expr, astroid.Name)
                and node.func.attrname in PANDAS_READ_METHODS
        ):
            inferred_node = safe_infer(node.func.expr)
            if inferred_node and "pandas" in inferred_node.root().name:
                has_pandas_module = True

        if has_pandas_module:
            self.check_explicit_columns_and_dtype(node=node)

    def check_explicit_columns_and_dtype(self, node: astroid.Call):
        # No check for dtype_backends, according to pandas doc "The dtype_backends are still experimential."
        # Checking usercols and dtype is redundant. Therefore, only checking dtype keyword is set
        has_explicit_dtype = False

        for keyword in node.keywords:
            if keyword.arg == 'dtype':
                has_explicit_dtype = True

        if not has_explicit_dtype:
            self.record_finding(node=node)

    def record_finding(self, node: astroid.Call) -> None:
        Result.add(CodeSmell(code_smell_id=self.ID,
                             code_smell_title="Columns and DataType Not Explicitly Set",
                             file_path=self.filename,
                             line=node.lineno,
                             col_offset=node.col_offset,
                             smell_type="Error-prone",
                             description="Explicitly select columns and set DataType when importing data.",
                             pipeline_stage="Data Cleaning",
                             effect="Readability",
                             source_code=node.as_string(),
                             source_astroid_node=f"Astroid AST: {node} \n Code: {node.as_string()}"))
