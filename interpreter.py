from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor

def interpret(input_file: str='example.txt'):
    with open(input_file, 'r') as f:
        code = f.read()
    lexer = GrammarLexer(InputStream(code))
    tokens = CommonTokenStream(lexer)
    parser = GrammarParser(tokens)
    tree = parser.program()
    print(type(tree))
    # interpreter = GrammarVisitor()
    # interpreter.visit(tree)

interpret()