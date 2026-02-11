from my_token import Token
from token_type import TokenType


class Lexer:
    def __init__(self, source: str) -> None:
        self.source = source
        self.start_idx = 0
        self.curr_idx = 0
        self.tokens: list[Token] = []

    def scanTokens(self) -> list[Token]:
        while not self._isAtEnd():
            self.start_idx = self.curr_idx
            self._scanToken()

        return self.tokens

    def _scanToken(self) -> None:
        c = self.advance()
        match c:
            case "+":
                self.addToken(TokenType.PLUS)
            case "-":
                self.addToken(TokenType.MINUS)
            case "*":
                self.addToken(TokenType.STAR)
            case "/":
                self.addToken(TokenType.SLASH)
            case "^":
                self.addToken(TokenType.POWER)
            case "!":
                self.addToken(TokenType.BANG)
            case "(":
                self.addToken(TokenType.LEFT_PARAM)
            case ")":
                self.addToken(TokenType.RIGHT_PARAM)
            case _ if c.isdigit():
                self.consume_number()
            case _ if c.isspace():
                pass
            case _:
                raise Exception("Unexpected character")

    def addToken(self, type: TokenType) -> None:
        lexeme = self.source[self.start_idx : self.curr_idx]
        self.tokens.append(Token(type, lexeme))

    def advance(self) -> str:
        curr_char = self.source[self.curr_idx]
        self.curr_idx += 1
        return curr_char
        
    def peek(self) -> str:
        if self._isAtEnd():
            return " "
        
        return self.source[self.curr_idx]

    def _isAtEnd(self) -> bool:
        return self.curr_idx >= len(self.source)
