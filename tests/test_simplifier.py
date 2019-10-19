import pytest

import simplifier


@pytest.mark.parametrize(
    'row, expected_result',
    [(['*','*','*'], False),
    ([1, '*', '*'], False),
    ([1, 1, '*'], True),
    ([], True),
    (None, False)]
)
def test_check_stars(expected_result, row):
    """
    Test checking whether a row is potentially simplified.

    Empty/null input is tested.

    """
    assert simplifier.check_stars(row) == expected_result


@pytest.mark.parametrize(
    'predicates, expected_result',
    [
        ({'A': ['*','*', 1],
        'B' : ['*', 0, 1],
        'C': [0, 1, 1],
        'D': [1, '*', '*']}, True),

        ({'A': ['*','*', 1],
        'B' : ['*', 0, '*'],
        'C': [0, '*', '*'],
        'D': [1, '*', '*']}, False),
        ({'A': []}, False),
        (None, False)
    ]
)
def test_check_table_simplified(expected_result, predicates):
    """
    Test checking whether a truth table is simplifiable or not.

    A case where the table can be simplified and a case where it can't are
    provided. Empty/null input is also checked.

    """
    assert simplifier.check_table_simplified(predicates) == expected_result


@pytest.mark.parametrize(
    'row, expression_result_values, expected_result',
    [
        (
        ['*', '*', 1, '*'],
        [0, 0, 1, 1],
        False
        ),
        (
        ['*', 1, 1, '*'],
        [0, 1, 1, 1],
        True
        ),
        ([], [], False),
        (None, [0, 1], False),
        ([0, 1, 0], None, False)

    ]
)
def test_generate_expansion(
        expected_result,
        expression_result_values,
        predicates,
        row):
    """
    Test generate expansion of a simplified line.

    A case where the expansion is valid and a case the expansion is invalid
    are taken into consideration. Cases for invalid input are considered (empty/null
    input).

    """
    assert simplifier.generate_expansion(
        row, predicates, expression_result_values) == expected_result


@pytest.mark.parametrize(
    'predicates, expected_values, expression_result_values',
    [
    ({'A': [1, 0, 0, 1, 0],
    'B': [0, 1, 0, 1, 0],
    'C': [0, 0, 0, 0, 1]},
    {'A': [0, 0], 'B': ['*', 0], 'C': [0, 1]},
    [0, 1, 1, 0, 1]
    ),
    ({'A': [1, 0, 0, 1, 0],
    'B': [0, 1, 1, 1, 0],
    'C': [0, 0, 1, 1, 0]},
    {'A': ['*', 0], 'B': ['*', '*'], 'C': [0, '*']},
    [1, 1, 1, 0, 1]
    )
    ]
)
def test_compute_intermediate_simplified(
        predicates,
        expected_values,
        expression_result_values):
    """
    Test computing intermediate simplification table.

    An intermediate simplification table is the one obtained by simplifying
    any 2 rows in the table, as long as they haven't been simplified before.
    If the number of the rows to simplify is odd, the remaining row is appended
    for a possible next round of simplification.
    This function does not test for missing/null input as it is part of the
    simplify table functionality; input to this function comes from a single
    place in the code and it is therefore trusted.

    """
    simplified_predicates = predicates
    simplified_expression_result_values = expression_result_values
    assert simplifier.compute_intermediate_simplified(
        expression_result_values,
        predicates,
        simplified_predicates,
        simplified_expression_result_values)[0] == expected_values


@pytest.mark.parametrize(
    'predicates, expression_result_values, expected_result',
    [
    ({
        'A': [0, 0, 0, 0],
        'B': [0, 1, 0, 1],
        'C': [0, 1, 1, 1],
        'D': [1, 0, 0, 1]
    }, [0, 1, 1, 1], { 'A': [0], 'B': ['*'], 'C': [1], 'D': ['*']}),
    ({
        'A': [0, 0, 0, 0],
        'B': [0, 1, 0, 1],
        'C': [0, 1, 1, 0],
        'D': [1, 0, 0, 1]
    }, [0, 1, 1, 1], { 'A': [0, 0], 'B': ['*', 1], 'C': [1, 0], 'D': [0, 1]}),
    (None, None, None),
    ({}, None, {}),
    (None, [], None),
    ({}, [], {}),
    ({'A': [0]}, [], {'A': [0]})
    ]
)
def test_compute_simplified_predicates(
        expected_result,
        expression_result_values,
        predicates):
    """
    Test computing simplified predicate truth table.

    The test takes into account missing/null input.

    """
    assert simplifier.compute_simplified_predicates(
        predicates, expression_result_values)[0] == expected_result
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
=======


def test_compute_simplified_predicates_sidecase():
    """
    Tests sidecase when tautologic row is generated.

    If the function does not execute correctly, this leads to
    simplified tables that are missing rows that generate
    tautological entries.

    """
    expected_result = {'A': ['*', '*', '*'], 'B': ['*', '*', '*'], 'C': [0, '*', '*'], 'D': [0, 1, 1]}
    expression_result_values = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    predicates = {
        'A': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        'B': [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        'C': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        'D': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
    simplified_predicates = predicates
    simplified_expression_result_values = expression_result_values
    assert simplifier.compute_simplified_predicates(
        predicates, expression_result_values)[0] == expected_result
>>>>>>> refactor(ALE1): Windows executable and final report
