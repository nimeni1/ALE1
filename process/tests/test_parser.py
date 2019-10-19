import pytest

import expression_parser


@pytest.mark.parametrize(
    'expression_result_values, expected_result',
    [
    ([0, 0, 1, 0, 1], '10100'),
    ([0, 1, 0], '010'),
    (None, ''),
    ([], '')
    ]
)
def test_generate_hash_code(expression_result_values, expected_result):
    """
    Test generating hash code.

    This test also considers the case of missing/null input.

    """
    assert expected_result == expression_parser.generate_hash_code(expression_result_values)


def traverse_helper(node1, node2):
    """
    Check if 2 binary trees are identical.

    This recursive function traverses both of the binary trees at the same time,
    starting from the root.

    Args:
        node1 (expression_parser.Node):
            Node belonging to the tree that the check is performed against.

        node2 (expression_parser.Node):
            Node belonging to the tree the check is performed for.

    Returns:
        boolean:
            Whether the 2 trees are identical or not (same values stored in
            its nodes and same number of children).

    """
    if node1 is None and node2 is None:
        return True
    elif node1 is not None and node2 is not None:
        if node1.symbol != node2.symbol:
            return False
        return (traverse_helper(node1.left_child, node2.left_child) and
            traverse_helper(node1.right_child, node2.right_child))
    else:
        return False


@pytest.mark.parametrize(
    'expression',
    ['=(>(A,B),|(~(A),B))',
    pytest.param('=( >(A,B) , | (~(A),B))', marks=pytest.mark.xfail),
    'A'])
def test_convert2tree(expression, root):
    """
    Test for converting expression to a tree data structure.

    The expression must not contain any spaces. This is done in the
    application right in the beginning of the executed code. This test also
    checks for this case and passes if the output tree is wrong. This is done
    through parametrization of the 'expression'. A fixture provides the tree
    data structure to be have the output checked against and a traverse helper
    which performs the checking.
    Case when expression is only a proposition is also taken into consideration.

    """
    test_root = expression_parser.convert2tree(expression)[0]
    unique_node = expression_parser.Node(expression[0])
    assert test_root.symbol == unique_node.symbol
    if len(expression) > 1:
        for ch in expression:
            if ch == ' ':
                assert not traverse_helper(root, test_root)
            else:
                assert traverse_helper(root, test_root)
            break


@pytest.mark.parametrize(
    'expression, expected_result',
    [(None, None)]
)
def test_convert2tree_sidecases(expression, expected_result):
    """
    Test sidecases for converting expression to a tree data structure.

    This test takes into consideration only missing/null input as parameters of
    the tested function.

    """
    assert expected_result == expression_parser.convert2tree(expression)
