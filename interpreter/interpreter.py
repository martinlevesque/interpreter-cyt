from syntax_tree.expr import Expr
from syntax_tree.literal_expr import LiteralExpr
from syntax_tree.grouping_expr import GroupingExpr


class Interpreter:
    def visitLiteralExpr(self, expr: LiteralExpr) -> str | None:
        return expr.literal.literal

    def visitGroupingExpr(self, expr: GroupingExpr) -> object | None:
        return self.evaluate(expr.expression)

    def evaluate(self, expr: Expr) -> object | None:
        return expr.accept()
