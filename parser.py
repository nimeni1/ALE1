import graphviz

import process

class Node:
    def __init__(self, symbol=None):
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.symbol = symbol
        self.label = None
        self.value = None


def convert2tree(expression, counter=1):
    """
    Parse input expression.

    This function parsed the input expression in the form of a binary parser.

    Args:
        expression (str): Expression to be parsed.

        counter (int): Counter used for labeling the nodes of the
            parsed expression binary parser.

    Returns:
        tuple:
            Node: Root of the parsed expression parser.

            dict: List of predicates present in the expression.

    """
    punctuation_symbols = ['(', ')', ',']
    if expression is None:
        return None
    if len(expression) == 1 and expression.isalpha():
        root = Node(expression)
        root.label = '0'
        predicates = {}
        predicates[expression] = []
        return root, predicates
    predicates = {}
    root_value = expression[0]
    root = Node(root_value)
    root.label = 'node' + str(counter)
    counter += 1
    currentNode = root
    for i in range(1, len(expression)):
        if expression[i] == '(':
            currentNode.left_child = Node()
            currentNode.left_child.parent = currentNode
            currentNode.left_child.label = 'node' + str(counter)
            counter += 1
            currentNode = currentNode.left_child
        if expression[i] in process.symbols:
            currentNode.symbol = expression[i]
        if expression[i] not in process.symbols and \
           expression[i] not in punctuation_symbols:
                currentNode.symbol = expression[i]
                currentNode = currentNode.parent
                predicates[expression[i]] = []
        if expression[i] == ',':
            currentNode.right_child = Node()
            currentNode.right_child.parent = currentNode
            currentNode.right_child.label = 'node' + str(counter)
            counter += 1
            currentNode = currentNode.right_child
        if expression[i] == ')':
            currentNode = currentNode.parent
    return root, predicates


def build_render_tree(tree, node):
    """
    Create additional data structure to render the parser.

    This function is a helper for rendering the parsed expression tree in
    graphical form.

    Args:
        tree (graphviz.Digraph): Addtional data structure used only
            for the purpose of rendering the parsed expression parser.

        node (Node): Node of the parsed parser.

    """
    if node.left_child is not None:
        tree.node(node.left_child.label, node.left_child.symbol)
        tree.edge(node.label, node.left_child.label)
        build_render_tree(tree, node.left_child)
    if node.right_child is not None:
        tree.node(node.right_child.label, node.right_child.symbol)
        tree.edge(node.label, node.right_child.label)
        build_render_tree(tree, node.right_child)


def generate_hash_code(expression_result_values):
    """
    Generate hash code of truth table based on the expression result values.

    Args:
        expression_result_values (list):
            Expression result values of the truth table.

    Retuns:
        str: Hash code of the truth table.

    """
    hash_code = ''
    if expression_result_values is None or expression_result_values == []:
        return hash_code
    for value in reversed(expression_result_values):
        hash_code += str(value)
    return hash_code


def render_tree(root):
    """
    Render expression parser.

    Function that renders the parsed expression tree in a graphical form.

    Args:
        root (Node): Root of the expression tree to render.

    """
    tree = graphviz.Digraph()
    if root is not None:
        tree.node(root.label, root.symbol)
        build_render_tree(tree, root)
        tree.render('tree_diagram.png', view=True)
