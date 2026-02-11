from lexer import Lexer

try:
    while True:
        input_str = input("> ")
        lexer = Lexer(input_str)
        print(lexer.scanTokens())
except KeyboardInterrupt:
    print("Bye!")
