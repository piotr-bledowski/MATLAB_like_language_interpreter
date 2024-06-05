from graphviz import Digraph
import os
from interpreter import read_file
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor
from antlr4 import *

def create_parser_tree(tree, name):
    dot = Digraph(name)
    add_nodes(dot, tree)
    return dot

def add_nodes(dot, tree, parent=None):
    node_id = str(id(tree))
    label = tree[0]
    dot.node(node_id, label)
    if parent:
        dot.edge(str(id(parent)), node_id)
    for child in tree[1:]:
        if isinstance(child, tuple):
            add_nodes(dot, child, tree)
        else:
            dot.node(str(id(child)), str(child))
            dot.edge(node_id, str(id(child)))

class TreeToNestedListVisitor(GrammarVisitor):
    def visitChildren(self, node):
        result = [node.__class__.__name__]
        for child in node.getChildren():
            result.append(self.visit(child))
        return result

    def visitTerminal(self, node):
        return node.getText()

def main():
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    example_tree_1 = ("expression", ("operation", ("number", "5"), "+", ("operation", ("number", "3"), "*", ("number", "2"))))
    example_tree_2 = ("conditional", ("comparison", ("identifier", "x"), ">", ("number", "0")), "THEN", ("identifier", "positive_value"), "ELSE", ("identifier", "negative_value"))
    example_tree_3 = ("function_call", ("function_name", "sum"), "(", ("argument", ("number", "10")), ",", ("argument", ("number", "20")), ")")
    example_tree_4 = ("function_call", ("function_name", "fibonacci"), "(", ("argument", ("number", "5")), ")")
    example_tree_5 = ("loop", "FOR", ("identifier", "i"), "IN", ("range", ("number", "10")), "DO", ("statement", ("expression", ("operation", ("identifier", "total"), "+", ("identifier", "i")))))
    example_tree_6 = ("conditional", ("comparison", ("identifier", "x"), ">", ("number", "0")), "THEN", ("conditional", ("comparison", ("identifier", "y"), ">", ("number", "0")), "THEN", ("expression", ("number", "1")), "ELSE", ("expression", ("number", "2"))), "ELSE", ("expression", ("number", "3")))

    examples = [example_tree_1, example_tree_2, example_tree_3, example_tree_4, example_tree_5, example_tree_6]

    for i, example_tree in enumerate(examples, 1):
        dot = create_parser_tree(example_tree, f"example_{i}")
        output_path = os.path.join(output_dir, f"parser_tree_example_{i}.png")
        dot.render(output_path, format="png", cleanup=True)

def nested_list_to_tuple(nested_list):
    if isinstance(nested_list, list):
        return tuple(nested_list_to_tuple(item) for item in nested_list)
    return nested_list

def generateTree(code: str):
    tree_list = nested_list_to_tuple(parse_code_to_nested_list(code))
    dot = create_parser_tree(tree_list, "what")
    dot.render('what', format='png', cleanup=True)

def parse_code_to_nested_list(code: str):
    lexer = GrammarLexer(InputStream(code))
    token_stream = CommonTokenStream(lexer)
    parser = GrammarParser(token_stream)

    # Parse the input to get the parse tree
    parse_tree = parser.program()  # Assuming 'program' is the start rule in Matlab.g4

    # Use the visitor to convert the parse tree to a nested list
    visitor = TreeToNestedListVisitor()
    nested_list = visitor.visit(parse_tree)

    return nested_list

if __name__ == "__main__":
    main()
    generateTree(read_file('test_examples/example2.txt'))

