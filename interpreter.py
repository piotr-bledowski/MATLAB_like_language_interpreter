from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor


def print_tree(node, indent=0):
    print(" " * indent + str(node))
    if not isinstance(node, TerminalNodeImpl):
        for child in node.getChildren():
            print_tree(child, indent + 2)

def interpret(input_file: str='example.txt'):
    with open(input_file, 'r') as f:
        code = f.read()
    lexer = GrammarLexer(InputStream(code))
    tokens = CommonTokenStream(lexer)
    parser = GrammarParser(tokens)
    tree = parser.program()
    print_tree(tree)
    # interpreter = GrammarVisitor()
    # interpreter.visit(tree)

interpret()
