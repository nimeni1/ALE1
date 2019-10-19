import pytest

import builder
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
import parser
=======
import expression_parser
>>>>>>> refactor(ALE1): Windows executable and final report


@pytest.mark.parametrize(
    'table, predicates',
    [
    (
    [[0,0,0,0,1,1,1,1],
     [0,0,1,1,0,0,1,1],
     [0,1,0,1,0,1,0,1]], {'A': [], 'B': [], 'C': []}
    ),
    ([[]], {}),
    ([[]], None)
    ]
)
def test_create_table(table, predicates):
    """
    Test creating truth table.

    Empty/null input tested.

    """
    assert table == builder.create_table(predicates)


def check_initialize(node):
    """
    Traverse tree with given root and check if leaves are initialized.

    Done recursively.

    Args:
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
        node (parser.Node): Current node of the tree.
=======
        node (expression_parser.Node): Current node of the tree.
>>>>>>> refactor(ALE1): Windows executable and final report

    Returns:
        boolean: True if all the leaves are initialized, False otherwise.

    """
    if node is None:
        return False
    if not node.left_child and not node.right_child:
        if node.value is None:
            return False
        return True
    if node.left_child:
        return check_initialize(node.left_child)
    if node.right_child:
        return check_initialize(node.right_child)


def test_initialize_tree(predicates):
    """
    Test initialization of a binary tree.

    Empty/null input is tested.
    Combinations of missing binary tree and no-predicate truth table/
    missing values predicates are considered.

    """
    row_index = 0
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    root = parser.Node('=')
    node1 = parser.Node('>')
    node1.left_child = parser.Node('A')
    node1.right_child = parser.Node('B')
    node2 = parser.Node('|')
    node2.left_child = parser.Node('C')
    node2.right_child = parser.Node('D')
=======
    root = expression_parser.Node('=')
    node1 = expression_parser.Node('>')
    node1.left_child = expression_parser.Node('A')
    node1.right_child = expression_parser.Node('B')
    node2 = expression_parser.Node('|')
    node2.left_child = expression_parser.Node('C')
    node2.right_child = expression_parser.Node('D')
>>>>>>> refactor(ALE1): Windows executable and final report
    root.left_child = node1
    root.right_child = node2
    builder.initialize_tree(root, predicates, row_index)
    assert check_initialize(root)
    root = None
    predicates = {}
    builder.initialize_tree(root, predicates, row_index)
    assert not check_initialize(root)
    root = None
    predicates = None
    builder.initialize_tree(root, predicates, row_index)
    assert not check_initialize(root)
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    root = parser.Node('A')
=======
    root = expression_parser.Node('A')
>>>>>>> refactor(ALE1): Windows executable and final report
    predicates = {'A': []}
    builder.initialize_tree(root, predicates, row_index)
    assert not check_initialize(root)


@pytest.mark.parametrize(
    'operator, value1, value2, expected_result',
    [('~', 0, 0, 1),
    ('&', 0, 1, 0),
    ('|', 0, 1, 1),
    ('=', 0, 1, 0),
    ('>', 1, 0, 0),
    ('', None, None, None),
    (None, None, None, None)]
)
def test_compute_node_value(expected_result, operator, value1, value2):
    """
    Test computing truth value for a given node.

    This test takes into consideration the following operators: ~,&,|,=,<.
    It also checks for null values.

    """
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    node = parser.Node(operator)
    child1 = parser.Node('A')
    child1.value = value1
    node.left_child = child1
    child2 = parser.Node('B')
=======
    node = expression_parser.Node(operator)
    child1 = expression_parser.Node('A')
    child1.value = value1
    node.left_child = child1
    child2 = expression_parser.Node('B')
>>>>>>> refactor(ALE1): Windows executable and final report
    child2.value = value2
    node.right_child = child2
    assert builder.compute_node_value(node) == expected_result
    node = None
    assert builder.compute_node_value(node) == None
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    node = parser.Node(None)
    assert builder.compute_node_value(node) == None
    node = parser.Node(operator)
=======
    node = expression_parser.Node(None)
    assert builder.compute_node_value(node) == None
    node = expression_parser.Node(operator)
>>>>>>> refactor(ALE1): Windows executable and final report
    node.left_child = None
    node.right_child = None
    assert builder.compute_node_value(node) == None


def test_compute_result(predicates):
    """
    Test computing result array of an expression.

    The test checks for a case where the output of the tested function
    is compared against what the result should be, given that the
    truth table is the one supplied by the fixture. In that case, the
    test checks for failure, since the tested function rereferences the
    truth table to a complete one (which is definitely not the case of
    the fixture).
    The other case considers the output for all the 2^n rows from a table,
    given that n is the number of predicates. In this case, the test checks
    for a pass.
    The test also considers cases of missing/null input.

    """
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    root = parser.Node('=')
    node1 = parser.Node('>')
    node1.left_child = parser.Node('A')
    node1.right_child = parser.Node('B')
    node2 = parser.Node('|')
    node2.left_child = parser.Node('C')
    node2.right_child = parser.Node('D')
=======
    root = expression_parser.Node('=')
    node1 = expression_parser.Node('>')
    node1.left_child = expression_parser.Node('A')
    node1.right_child = expression_parser.Node('B')
    node2 = expression_parser.Node('|')
    node2.left_child = expression_parser.Node('C')
    node2.right_child = expression_parser.Node('D')
>>>>>>> refactor(ALE1): Windows executable and final report
    root.left_child = node1
    root.right_child = node2
    expected_result_false = [0, 1, 1, 1]
    expected_result_true = [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
    result = builder.compute_result(root, predicates)
    assert result == expected_result_true
    assert result != expected_result_false


@pytest.mark.parametrize(
    'root, predicates, expected_result',
    [
    (None, None, []),
    (None, {}, []),
    (None, {'A': []}, []),
    (None, {'A': None}, [])
    ]
)
def test_compute_result_sidecases(root, predicates, expected_result):
    """
    Test sidecases for computing result functionality.

    This function considers only missing/null input to the function.

    """
    assert expected_result == builder.compute_result(root, predicates)
