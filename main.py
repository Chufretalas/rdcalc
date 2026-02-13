from ast_printer import AstPrinter
from interpreter import Interpreter
from lexer import Lexer
from parser import Parser

try:
    ast_printer = AstPrinter()
    interpreter = Interpreter()
    while True:
        input_str = input("> ")
        lexer = Lexer(input_str)
        tokens = lexer.scanTokens()
        parser = Parser(tokens)
        expr = parser.parse()
        ast_printer.print(expr)
        print(interpreter.do_the_math_stuff(expr))

except KeyboardInterrupt:
    print("\nBye!")
