from dataclasses import dataclass

from token_type import TokenType


@dataclass()
class Token():
    type: TokenType
    lexeme: str
    
    def __str__(self) -> str:
        return f"Token({self.type.name}, '{self.lexeme}')"
    
    def __repr__(self) -> str:
        return f"Token({self.type.name}, '{self.lexeme}')"
