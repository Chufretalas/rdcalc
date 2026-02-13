import math
from typing import cast

from expr import BinaryExpr, Expr, ExprVisitor, GroupingExpr, LiteralExpr, UnaryExpr
from my_exceptions import MyRuntimeError
from token_type import TokenType


class Interpreter(ExprVisitor[float]):
    def do_the_math_stuff(self, expr: Expr) -> float:
        return cast(float, expr.accept(self))

    def visitBinaryExpr(self, expr: BinaryExpr) -> float:
        if (
            expr.operator.type == TokenType.POWER
        ):  # Respecting expected solve order (even though it doesn't matter since this calculator does not produce side-effects)
            right_value = cast(float, expr.right.accept(self))
            left_value = cast(float, expr.left.accept(self))
        else:
            left_value = cast(float, expr.left.accept(self))
            right_value = cast(float, expr.right.accept(self))

        match expr.operator.type:
            case TokenType.PLUS:
                return left_value + right_value
            case TokenType.MINUS:
                return left_value - right_value
            case TokenType.STAR:
                return left_value * right_value
            case TokenType.SLASH:
                if right_value == 0.0:
                    raise MyRuntimeError(
                        f"Can not divide by zero. {left_value} / {right_value}"
                    )
                return left_value / right_value
            case TokenType.POWER:
                return left_value**right_value

        raise MyRuntimeError("Unknown case in visitBinaryExpression")

    def visitUnaryExpr(self, expr: UnaryExpr) -> float:
        value = cast(float, expr.expr.accept(self))
        match expr.operator.type:
            case TokenType.MINUS:
                return -value
            case TokenType.BANG:
                if not float.is_integer(value):
                    raise MyRuntimeError(
                        f"Factorial can only be applied to an integer. Expected integer, got {value}"
                    )
                return float(math.factorial(int(value)))

        raise MyRuntimeError("Unknown case in visitUnaryExpression")

    def visitGroupingExpr(self, expr: GroupingExpr) -> float:
        return cast(float, expr.expr.accept(self))

    def visitLiteralExpr(self, expr: LiteralExpr) -> float:
        return expr.number
