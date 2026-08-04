import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _evaluate(node):
    if isinstance(node, ast.Expression):
        return _evaluate(node.body)

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp):
        operator_func = OPERATORS.get(type(node.op))
        if operator_func is None:
            raise ValueError("unsupported operator")

        return operator_func(
            _evaluate(node.left),
            _evaluate(node.right),
        )

    if isinstance(node, ast.UnaryOp):
        operator_func = OPERATORS.get(type(node.op))
        if operator_func is None:
            raise ValueError("unsupported operator")

        return operator_func(_evaluate(node.operand))

    raise ValueError("only numeric expressions are supported")


def calculate(expression: str) -> str:
    parsed = ast.parse(expression, mode="eval")
    result = _evaluate(parsed)
    return str(result)
