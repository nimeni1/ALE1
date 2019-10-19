import pytest

import nand_computer


@pytest.mark.parametrize(
    'expression_result_values, expected_nand',
    [
    (
    [1, 1, 1, 0],
    '%({},%(%({},{}),%({},{})))'.format(
        '%(%(A,A),%(%(%(B,B),%(%(%(C,C),D),%(%(C,C),D))),%(%(B,B),%(%(%(C,C),D),%(%(C,C),D)))))',
        '%(%(A,A),%(%(B,%(%(C,%(D,D)),%(C,%(D,D)))),%(B,%(%(C,%(D,D)),%(C,%(D,D))))))',
        '%(%(A,A),%(%(%(B,B),%(%(C,%(D,D)),%(C,%(D,D)))),%(%(B,B),%(%(C,%(D,D)),%(C,%(D,D))))))',
        '%(%(A,A),%(%(B,%(%(C,%(D,D)),%(C,%(D,D)))),%(B,%(%(C,%(D,D)),%(C,%(D,D))))))',
        '%(%(A,A),%(%(%(B,B),%(%(C,%(D,D)),%(C,%(D,D)))),%(%(B,B),%(%(C,%(D,D)),%(C,%(D,D))))))')
    )
    ]
)
def test_compute_nand(predicates, expression_result_values, expected_nand):
    """
    Test computing nand.

    Standard input is tested.

    """
    assert expected_nand == nand_computer.compute_nand(predicates, expression_result_values)


def test_compute_simplified_nand():
    """
    Test computing nand for a simplified table.

    """
    predicates = {'A': [1], 'B': [0], 'C': [1], 'd': ['*'], 'H': ['*'], 'G': ['*']}
    expression_result_values = [1]
    expected_nand = '%(%(A,%(%(%(B,B),C),%(%(B,B),C))),%(A,%(%(%(B,B),C),%(%(B,B),C))))'
    assert expected_nand == nand_computer.compute_nand(predicates, expression_result_values)


@pytest.mark.parametrize(
    'expression_result_values, expected_nand',
    [
    ([], ''),
    (None, ''),
    ([0, 0, 0, 1], '%(%(A,B),%(A,B))')
    ]
)
def test_compute_nand_sidecases(expression_result_values, expected_nand):
    """
    Test computing nand.

    Only sidecases are considered

    """
    predicates = {'A': [0, 0, 1, 1], 'B': [0, 1, 0, 1]}
    assert expected_nand == nand_computer.compute_nand(predicates, expression_result_values)
