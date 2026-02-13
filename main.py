from ast_printer import AstPrinter
from interpreter import Interpreter
from lexer import Lexer
from my_exceptions import MyRuntimeError, MySyntaxError
from parser import Parser

try:
    ast_printer = AstPrinter()
    interpreter = Interpreter()
    while True:
        try:
            input_str = input("> ")
            lexer = Lexer(input_str)
            tokens = lexer.scanTokens()
            parser = Parser(tokens)
            expr = parser.parse()
            ast_printer.print(expr)
            print(interpreter.do_the_math_stuff(expr))
        except MySyntaxError as e:
            print(f"SYNTAX ERROR: {e}")
        except MyRuntimeError as e:
            print(f"RUNTIME ERROR: {e}")
        except OverflowError:
            print("RUNTIME ERROR: Overflow!")

except KeyboardInterrupt:
    print("\nBye!")
