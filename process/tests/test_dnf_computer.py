import pytest

import dnf_computer
import expression_parser


@pytest.mark.parametrize(
    'dnf',
    ['&(A,&(B,&(C,D)))']
)
def test_build_line_dnf(dnf, dnf_nodes):
    """
    Test building line disjunctive normal form.

    This test also checks for 1 element list and empty list cases.

    """
    assert dnf == dnf_computer.build_line_dnf(dnf_nodes)
    dnf_nodes = []
    dnf = ''
    assert dnf == dnf_computer.build_line_dnf(dnf_nodes)
    dnf_nodes.append(expression_parser.Node('A'))
    dnf = 'A'
    assert dnf == dnf_computer.build_line_dnf(dnf_nodes)


@pytest.mark.parametrize(
    'dnf_full',
    ['|(&(A,&(B,&(C,D))),|(&(~(A),&(B,&(C,D))),|(&(A,&(~(B),&(C,D))),&(A,&(B,&(C,~(D)))))))']
)
def test_build_full_dnf(dnf_full, dnf_rows):
    """
    Test building full disjunctive normal form.

    This test also takes into consideration input made of one node
    as well as input which is null.

    """
    assert dnf_full == dnf_computer.build_full_dnf(dnf_rows)
    dnf_full = ['A']
    dnf_rows = [['A']]
    assert dnf_full == dnf_computer.build_full_dnf(dnf_rows)
    dnf_rows = None
    dnf_full = ''
    assert dnf_full == dnf_computer.build_full_dnf(dnf_rows)


def test_compute_dnf(predicates):
    """
    Test full computation of a dnf.

    This test takes into consideration input made of one node as well as
    input which is null or empty. It also asserts for the case where
    all rows in the truth table yield false.
    For empty input, combinations of empty/null input have been tested.

    """
    dnf = '|(&(~(A),&(B,&(C,~(D)))),&(~(A),&(~(B),&(C,~(D)))))'
    expression_result_values = [0, 1, 1, 0]
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)
    dnf = ''
    expression_result_values = [0, 0, 0, 0]
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)
    dnf = 'A'
    expression_result_values = [1]
    predicates = {'A': [0]}
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)
    expression_result_values = []
    predicates = {}
    dnf = ''
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)
    expression_result_values = [0, 1, 1, 1]
    predicates = {}
    dnf = ''
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)
    expression_result_values = None
    predicates = None
    dnf = ''
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)
    expression_result_values = [0, 1, 1, 1]
    predicates = None
    dnf = ''
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)
    expression_result_values = [1, 1]
    predicates = {'A': [0, 1]}
    dnf = 'A'
    assert dnf == dnf_computer.compute_dnf(predicates, expression_result_values)


@pytest.mark.parametrize(
    'simplified_predicates, expected_dnf',
    [
    (
    {'A': ['*', 0, 1],
    'B': ['*', '*', 1],
    'C': [1, 0, '*']}, '|(C,|(&(~(A),~(C)),&(A,B)))'
    ),
    ({'A': [0]}, 'A'),
    ({}, ''),
    (None, '')
    ]
)
def test_compute_simplified_dnf(simplified_predicates, expected_dnf):
    """
    Test computing simplified dnf.

    Test takes into consideration empty or null input.

    """
    assert expected_dnf == dnf_computer.compute_simplified_dnf(
        simplified_predicates)
