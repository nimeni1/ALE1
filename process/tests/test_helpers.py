import pytest

import expression_parser
import helpers


@pytest.mark.parametrize(
    'expression',
    ['=(>(A,B),|(~(A),B))']
)
def test_convert2expression(expression, root):
    """
    Test converting tree data structure to expression.

    The test also takes into consideration cases when the tree is
    represented by one node or when the node is null.

    """
    assert expression == helpers.convert2expression(root)
    node = expression_parser.Node('A')
    assert 'A' == helpers.convert2expression(node)
    node = None
    assert '' == helpers.convert2expression(node)


@pytest.mark.parametrize(
    'row, expected_result',
    [
        (
        ['*', '*', '*', '*'], {
            'A': [0, 0, 0, 0, '*'],
            'B': [0, 1, 0, 1, '*'],
            'C': [0, 1, 1, 1, '*'],
            'D': [1, 0, 0, 1, '*']}
        ),
        (
        [], {
            'A': [0, 0, 0, 0],
            'B': [0, 1, 0, 1],
            'C': [0, 1, 1, 1],
            'D': [1, 0, 0, 1]}
        ),
        (
        ['*', '*', '*'], None
        ),
        (None, {
            'A': [0, 0, 0, 0],
            'B': [0, 1, 0, 1],
            'C': [0, 1, 1, 1],
            'D': [1, 0, 0, 1]})
    ]
)
def test_append2dict(expected_result, predicates, row):
    """
    Test appending list to a dictionary.

    A totally simplified row is appended to the dictionary.
    A case where the appended row is smaller than the length of the
    dictionary is considered.
    Empty/null input is considered.

    """
    assert helpers.append2dict(predicates, row) == expected_result


@pytest.mark.parametrize(
    'expression_result_values, expected_result',
    [([1, 0, 0, 0, 1], [0, 4]),
    ([1, 0, 0, 0, 1, 0, 0, 1, 1], [0, 4, 7, 8]),
    ([], []),
    (None, [])]
)
def test_get_true_rows(expression_result_values, expected_result):
    """
    Test getting indexes of true rows according the expression result values.

    Test also takes into consideration empty/null input.

    """
    assert helpers.get_true_rows(expression_result_values) == expected_result


@pytest.mark.parametrize(
    'expression, expected_result',
    [('>(&(A,B),|(=(C,D),E))', True),
    ('&(>(&(A,B),|(=(C,D),E)),>(=(F,A),B))', True),
    ('&(A,B', False),
    (None, False)]
)
def test_regex_validate(expression, expected_result):
    """
    Test regex validation.

    This test considerd the case of both correct and incorrect expressions.
    It also checks for missing/null input.

    """
    assert helpers.regex_validate(expression) == expected_result
