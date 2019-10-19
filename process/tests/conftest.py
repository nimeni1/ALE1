import pytest

import expression_parser


@pytest.fixture
def dnf_nodes():
    """
    Create array of nodes.

    Returns:
        list: List of nodes

    """
    dnf_nodes = []
    dnf_nodes.append(expression_parser.Node('A'))
    dnf_nodes.append(expression_parser.Node('B'))
    dnf_nodes.append(expression_parser.Node('C'))
    dnf_nodes.append(expression_parser.Node('D'))
    return dnf_nodes


@pytest.fixture
def dnf_rows():
    """
    Create array of intermediate dnf strings for rows of a truth table.

    Number of rows is random, they only serve the purpose of testing
    correct functionality of the function, and not mathematically sound
    result.

    Returns:
        list: Dnf strings.

    """
    dnf_rows = []
    row1 = '&(A,&(B,&(C,D)))'
    row2 = '&(~(A),&(B,&(C,D)))'
    row3 = '&(A,&(~(B),&(C,D)))'
    row4 = '&(A,&(B,&(C,~(D))))'
    dnf_rows.append(row1)
    dnf_rows.append(row2)
    dnf_rows.append(row3)
    dnf_rows.append(row4)
    return dnf_rows


@pytest.fixture
def nodes():
    """
    Create list of nodes.

    Returns:
        list: List of nodes.

    """
    nodes = []

    node1 = expression_parser.Node('%')
    child1 = expression_parser.Node('expression1')
    node1.left_child = child1
    node1.right_child = child1
    child1.parent = node1

    node2 = expression_parser.Node('%')
    child21 = expression_parser.Node('expression21')
    child22 = expression_parser.Node('expression22')
    node2.left_child = child21
    child21.parent = node2
    node2.right_child = child22
    child22.parent = node2

    node3 = expression_parser.Node('&')
    child31 = expression_parser.Node('expression31')
    node3.left_child = child31
    node3.right_child = child31
    child31.parent = node3

    nodes.append(node1)
    nodes.append(node2)
    nodes.append(node3)

    return nodes


@pytest.fixture
def predicates():
    """
    Create predicates truth table.

    Size of table for 4 predicates should be 16. However, the purpose of this
    fixture is to generate a table that can be used to test functionality
    of methods and not provide a sound mathematical construction.


    Returns:
        dict: Truth table of predicates.

    """
    predicates = {
        'A': [0, 0, 0, 0],
        'B': [0, 1, 0, 1],
        'C': [0, 1, 1, 1],
        'D': [1, 0, 0, 1]
    }
    return predicates


@pytest.fixture
def root():
    """
    Build binary tree.

    Returns:
        expression_parser.Node: Root of the binary tree.
    """
    root = expression_parser.Node('=')
    node1_left = expression_parser.Node('>')
    node1_21_left = expression_parser.Node('A')
    node1_22_right = expression_parser.Node('B')
    node1_right = expression_parser.Node('|')
    node1_23_left = expression_parser.Node('~')
    node1_31_left = expression_parser.Node('A')
    node1_24_right = expression_parser.Node('B')

    root.left_child = node1_left
    root.right_child = node1_right

    node1_left.left_child = node1_21_left
    node1_left.right_child = node1_22_right

    node1_right.left_child = node1_23_left
    node1_right.right_child = node1_24_right

    node1_23_left.left_child = node1_31_left

    return root
