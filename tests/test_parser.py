import pytest

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
import parser
=======
import expression_parser
>>>>>>> refactor(ALE1): Windows executable and final report


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
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    assert expected_result == parser.generate_hash_code(expression_result_values)
=======
    assert expected_result == expression_parser.generate_hash_code(expression_result_values)
>>>>>>> refactor(ALE1): Windows executable and final report


def traverse_helper(node1, node2):
    """
    Check if 2 binary trees are identical.

    This recursive function traverses both of the binary trees at the same time,
    starting from the root.

    Args:
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
        node1 (parser.Node):
            Node belonging to the tree that the check is performed against.

        node2 (parser.Node):
=======
        node1 (expression_parser.Node):
            Node belonging to the tree that the check is performed against.

        node2 (expression_parser.Node):
>>>>>>> refactor(ALE1): Windows executable and final report
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
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    test_root = parser.convert2tree(expression)[0]
    unique_node = parser.Node(expression[0])
=======
    test_root = expression_parser.convert2tree(expression)[0]
    unique_node = expression_parser.Node(expression[0])
>>>>>>> refactor(ALE1): Windows executable and final report
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
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    assert expected_result == parser.convert2tree(expression)
=======
    assert expected_result == expression_parser.convert2tree(expression)
>>>>>>> refactor(ALE1): Windows executable and final report
