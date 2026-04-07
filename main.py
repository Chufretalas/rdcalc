import argparse

from ast_printer import AstPrinter
from interpreter import Interpreter
from lexer import Lexer
from my_exceptions import MyRuntimeError, MySyntaxError
from parser import Parser


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--ast",
        help="show raw AST representation of the input",
        action="store_true",
    )
    args = arg_parser.parse_args()

    ast_printer = AstPrinter()
    interpreter = Interpreter()
    try:
        while True:
            try:
                input_str = input("> ")
                lexer = Lexer(input_str)
                tokens = lexer.scanTokens()
                parser = Parser(tokens)
                expr = parser.parse()

                if args.ast:
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


if __name__ == "__main__":
    main()
