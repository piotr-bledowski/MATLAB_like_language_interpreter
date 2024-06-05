from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor
from VisitorImpl import VisitorImpl


# def print_tree(node, indent=0):
#
#
#     if isinstance(node, TerminalNodeImpl):
#         print(" " * indent + node.getText())  # Print token name with indentation
#     else:
#         print(" " * indent + str(node))  # Print node type for non-terminals
#         for child in node.getChildren():
#             print_tree(child, indent + 2)

def print_tree(node, indent=0):
    # Extract class name from node type
    node_type = node.__class__.__name__

    # Print node type and token name (if applicable)
    print(" " * indent + node_type + (" (" + node.getText() + ")" if isinstance(node, TerminalNodeImpl) else ""))
    if isinstance(node, TerminalNodeImpl):
        pass
        #print(" " * indent + node.getText())  # Print token name with indentation
    else:
        #print(" " * indent + node_type + (" (" + node.getText() + ")" if isinstance(node, TerminalNodeImpl) else ""), end="")
        for child in node.getChildren():
            print_tree(child, indent + 2)

def read_file(input_file: str='example2.txt'):
    r = ''
    with open(input_file, 'r') as f:
        r = f.read()
    return r

def interpret(code: str) -> str:
    lexer = GrammarLexer(InputStream(code))
    tokens = CommonTokenStream(lexer)
    parser = GrammarParser(tokens)
    tree = parser.program()
    #print_tree(tree)
    interpreter = VisitorImpl()
    interpreter.visit(tree)
    return interpreter.output

interpret(read_file())

# def parse_file_to_nested_list(input_file='simple_example.txt'):
#     with open(input_file, 'r') as f:
#         code = f.read()
#     lexer = GrammarLexer(InputStream(code))
#     token_stream = CommonTokenStream(lexer)
#     parser = GrammarParser(token_stream)
#
#     # Parse the input to get the parse tree
#     parse_tree = parser.program()  # Assuming 'program' is the start rule in Matlab.g4
#
#     # Use the visitor to convert the parse tree to a nested list
#     visitor = TreeToNestedListVisitor()
#     nested_list = visitor.visit(parse_tree)
#
#     return nested_list

#print(parse_file_to_nested_list())
