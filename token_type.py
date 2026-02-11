from enum import Enum

class TokenType(Enum):
    PLUS = 1 # "+"
    MINUS = 2 # "-"
    STAR = 3 # "*"
    SLASH = 4 # "/"
    POWER = 5 # "^"
    BANG = 6 # "!"
    LEFT_PARAM = 7 # "("
    RIGHT_PARAM = 8 # ")"
    NUMBER = 9 # "\d+(\.\d)?"