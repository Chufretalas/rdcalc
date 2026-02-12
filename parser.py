from expr import BinaryExpr, Expr, GroupingExpr, LiteralExpr, UnaryExpr
from my_token import Token
from token_type import TokenType


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self._tokens = tokens
        self._curr_idx = 0

    def parse(self) -> Expr:
        return self._sum_sub()

    def _sum_sub(self) -> Expr:
        left = self._mul_div()

        while self._check(TokenType.PLUS) or self._check(TokenType.MINUS):
            operator = self._advance()
            right = self._mul_div()
            left = BinaryExpr(left, operator, right)

        return left

    def _mul_div(self) -> Expr:
        left = self._neg()

        while self._check(TokenType.STAR) or self._check(TokenType.SLASH):
            operator = self._advance()
            right = self._neg()
            left = BinaryExpr(left, operator, right)

        return left

    def _neg(self) -> Expr:
        if self._check(TokenType.MINUS):
            operator = self._advance()
            expr = self._neg()
            return UnaryExpr(expr, operator)

        return self._power()

    def _power(self) -> Expr:
        left = self._factorial()

        if self._check(TokenType.POWER):
            operator = self._advance()
            right = self._power()
            return BinaryExpr(left, operator, right)

        return left

    def _factorial(self) -> Expr:
        expr = self._grouping()
        while self._check(TokenType.BANG):
            expr = UnaryExpr(expr, self._advance())

        return expr

    def _grouping(self) -> Expr:
        if self._check(TokenType.LEFT_PARAM):
            self._advance()  # Consume the '('
            expr = self._sum_sub()

            if not self._check(TokenType.RIGHT_PARAM):
                raise Exception("Expected ')'")

            self._advance()  # Consume the ')'

            return GroupingExpr(expr)

        return self._number()

    def _number(self) -> Expr:
        token = self._advance()
        if token.type != TokenType.NUMBER:
            raise Exception(f"Expected number, got {token}")

        return LiteralExpr(float(token.lexeme))

    # =============== HELPERS =============== #
    def _advance(self) -> Token:
        if not self._isAtEnd():
            self._curr_idx += 1

        return self._previous()

    def _check(self, type: TokenType) -> bool:
        if self._isAtEnd():
            return False
        return self._peek().type == type

    def _previous(self) -> Token:
        return self._tokens[self._curr_idx - 1]

    def _peek(self) -> Token:
        return self._tokens[self._curr_idx]

    def _isAtEnd(self) -> bool:
        return self._tokens[self._curr_idx].type == TokenType.EOF
