from my_exceptions import MySyntaxError
from my_token import Token
from token_type import TokenType


class Lexer:
    def __init__(self, source: str) -> None:
        self._source = source
        self._start_idx = 0
        self._curr_idx = 0
        self._tokens: list[Token] = []

    def scanTokens(self) -> list[Token]:
        while not self._isAtEnd():
            self._start_idx = self._curr_idx
            self._scanToken()

        self._tokens.append(Token(TokenType.EOF, ""))
        return self._tokens

    # ====== Consumers ====== #
    def _scanToken(self) -> None:
        c = self._advance()
        match c:
            case "+":
                self._addToken(TokenType.PLUS)
            case "-":
                self._addToken(TokenType.MINUS)
            case "*":
                self._addToken(TokenType.STAR)
            case "/":
                self._addToken(TokenType.SLASH)
            case "^":
                self._addToken(TokenType.POWER)
            case "!":
                self._addToken(TokenType.BANG)
            case "(":
                self._addToken(TokenType.LEFT_PARAM)
            case ")":
                self._addToken(TokenType.RIGHT_PARAM)
            case _ if c.isdigit():
                self._consume_number()
            case _ if c.isspace():
                pass
            case _:
                raise MySyntaxError(f"Unexpected character '{c}'")

    def _consume_number(self) -> None:
        while self._peek().isdigit():
            self._advance()

        if self._peek() == ".":
            self._advance()
            while self._peek().isdigit():
                self._advance()

        self._addToken(TokenType.NUMBER)

    # ====== Helpers ====== #
    def _addToken(self, type: TokenType) -> None:
        lexeme = self._source[self._start_idx : self._curr_idx]
        self._tokens.append(Token(type, lexeme))

    def _advance(self) -> str:
        curr_char = self._source[self._curr_idx]
        self._curr_idx += 1
        return curr_char

    def _peek(self) -> str:
        if self._isAtEnd():
            return " "

        return self._source[self._curr_idx]

    def _isAtEnd(self) -> bool:
        return self._curr_idx >= len(self._source)
