from graphviz import Digraph
import os
from interpreter import parse_file_to_nested_list

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

if __name__ == "__main__":
    main()
    tree_list = nested_list_to_tuple(parse_file_to_nested_list('example.txt'))
    dot = create_parser_tree(tree_list, "what")
    dot.render('what', format='png', cleanup=True)
