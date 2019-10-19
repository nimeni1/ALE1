import pytest

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
import parser 
=======
import expression_parser
>>>>>>> refactor(ALE1): Windows executable and final report


@pytest.fixture
def dnf_nodes():
    """
    Create array of nodes.

    Returns:
        list: List of nodes

    """
    dnf_nodes = []
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    dnf_nodes.append(parser.Node('A'))
    dnf_nodes.append(parser.Node('B'))
    dnf_nodes.append(parser.Node('C'))
    dnf_nodes.append(parser.Node('D'))
=======
    dnf_nodes.append(expression_parser.Node('A'))
    dnf_nodes.append(expression_parser.Node('B'))
    dnf_nodes.append(expression_parser.Node('C'))
    dnf_nodes.append(expression_parser.Node('D'))
>>>>>>> refactor(ALE1): Windows executable and final report
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

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    node1 = parser.Node('%')
    child1 = parser.Node('expression1')
=======
    node1 = expression_parser.Node('%')
    child1 = expression_parser.Node('expression1')
>>>>>>> refactor(ALE1): Windows executable and final report
    node1.left_child = child1
    node1.right_child = child1
    child1.parent = node1

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    node2 = parser.Node('%')
    child21 = parser.Node('expression21')
    child22 = parser.Node('expression22')
=======
    node2 = expression_parser.Node('%')
    child21 = expression_parser.Node('expression21')
    child22 = expression_parser.Node('expression22')
>>>>>>> refactor(ALE1): Windows executable and final report
    node2.left_child = child21
    child21.parent = node2
    node2.right_child = child22
    child22.parent = node2

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    node3 = parser.Node('&')
    child31 = parser.Node('expression31')
=======
    node3 = expression_parser.Node('&')
    child31 = expression_parser.Node('expression31')
>>>>>>> refactor(ALE1): Windows executable and final report
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
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
        parser.Node: Root of the binary tree.
    """
    root = parser.Node('=')
    node1_left = parser.Node('>')
    node1_21_left = parser.Node('A')
    node1_22_right = parser.Node('B')
    node1_right = parser.Node('|')
    node1_23_left = parser.Node('~')
    node1_31_left = parser.Node('A')
    node1_24_right = parser.Node('B')
=======
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
>>>>>>> refactor(ALE1): Windows executable and final report

    root.left_child = node1_left
    root.right_child = node1_right

    node1_left.left_child = node1_21_left
    node1_left.right_child = node1_22_right

    node1_right.left_child = node1_23_left
    node1_right.right_child = node1_24_right

    node1_23_left.left_child = node1_31_left

    return root
