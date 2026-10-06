# -- coding: utf-8 --

import sys

from lexer import Lexer
from birch_parser import Parser
from interpreter import Interpreter
from runtime import Runtime


def run(filename):

    with open(filename, "r", encoding="utf-8") as file:
        code = file.read()

    
    lexer = Lexer(code)
    tokens = lexer.tokenize()


    parser = Parser(tokens)
    program = parser.parse()


    runtime = Runtime()
    interpreter = Interpreter(runtime)


    interpreter.run(program)

    
if len(sys.argv) < 2:
    print("No file specified")
else:
    run(sys.argv[1])