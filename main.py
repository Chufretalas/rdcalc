from ast_printer import AstPrinter
from lexer import Lexer
from parser import Parser

try:
    ast_printer = AstPrinter()
    while True:
        input_str = input("> ")
        lexer = Lexer(input_str)
        tokens = lexer.scanTokens()
        parser = Parser(tokens)
        expr = parser.parse()
        ast_printer.print(expr)
        
except KeyboardInterrupt:
    print("Bye!")
