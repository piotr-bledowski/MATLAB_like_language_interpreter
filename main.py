import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor
from graphviz import Digraph

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

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.start_()


    # Example 1: Nested Expressions
    example_tree_1 = ("expression", 
                      ("operation", ("number", "5"), "+", ("operation", ("number", "3"), "*", ("number", "2")))
                     )
    
    # Example 2: Conditional Expression
    example_tree_2 = ("conditional", 
                      ("comparison", ("identifier", "x"), ">", ("number", "0")),
                      "THEN",
                      ("identifier", "positive_value"),
                      "ELSE",
                      ("identifier", "negative_value")
                     )
    
    # Example 3: Function Call
    example_tree_3 = ("function_call", 
                      ("function_name", "sum"),
                      "(", 
                      ("argument", ("number", "10")), 
                      ",", 
                      ("argument", ("number", "20")), 
                      ")"
                     )
    
    # Example 4: Recursive Function Call
    example_tree_4 = ("function_call", 
                      ("function_name", "fibonacci"),
                      "(", 
                      ("argument", ("number", "5")), 
                      ")"
                     )
    
    # Example 5: Loop Structure
    example_tree_5 = ("loop", 
                      "FOR", 
                      ("identifier", "i"), 
                      "IN", 
                      ("range", ("number", "10")), 
                      "DO", 
                      ("statement", 
                       ("expression", 
                        ("operation", ("identifier", "total"), "+", ("identifier", "i"))
                       )
                      )
                     )
    
    # Example 6: Nested Conditional Expressions
    example_tree_6 = ("conditional", 
                      ("comparison", ("identifier", "x"), ">", ("number", "0")),
                      "THEN",
                      ("conditional", 
                       ("comparison", ("identifier", "y"), ">", ("number", "0")),
                       "THEN",
                       ("expression", ("number", "1")),
                       "ELSE",
                       ("expression", ("number", "2"))
                      ),
                      "ELSE",
                      ("expression", ("number", "3"))
                     )

    for i, example_tree in enumerate([example_tree_1, example_tree_2, example_tree_3,
                                      example_tree_4, example_tree_5, example_tree_6], 1):
        dot = create_parser_tree(example_tree, f"example_{i}")
        dot.render(f"parser_tree_example_{i}", format="png", cleanup=True)

if __name__ == "__main__":
    main()


