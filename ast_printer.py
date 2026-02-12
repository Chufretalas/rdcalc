from expr import BinaryExpr, Expr, ExprVisitor, GroupingExpr, LiteralExpr, UnaryExpr


class AstPrinter(ExprVisitor[str]):
    def print(self, expr: Expr) -> None:
        print(expr.accept(self))

    def visitBinaryExpr(self, expr: BinaryExpr) -> str:
        return f"({expr.operator.lexeme} {expr.left.accept(self)} {expr.right.accept(self)})"

    def visitUnaryExpr(self, expr: UnaryExpr) -> str:
        return f"({expr.operator.lexeme} {expr.expr.accept(self)})"

    def visitGroupingExpr(self, expr: GroupingExpr) -> str:
        return f"(group {expr.expr.accept(self)})"

    def visitLiteralExpr(self, expr: LiteralExpr) -> str:
        return str(expr.number)
