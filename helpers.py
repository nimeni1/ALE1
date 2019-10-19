import re

import process


def get_nr_rows(predicates):
    """
    Get number of rows in a truth table.

    Args:
        predicates (dict): Truth table.

    Returns:
        int: Number of rows.

    """
    nr_rows = 0
    for predicate in predicates:
        nr_rows = len(predicates[predicate])
        break
    return nr_rows


def convert2expression(node):
    """
    Convert tree to expression.

    This function traverses the tree recursively and builds an expression
    representing the parser.

    Args:
        node (parser.Node): Current node in the parser.

    Returns:
        str: Expression representing the input parser.

    """
    expression = ''
    if node is None:
        return expression
    if node.symbol in process.symbols:
        expression += node.symbol
        expression += '('
        expression += convert2expression(node.left_child)
        if node.symbol != '~':
            expression += ','
            expression += convert2expression(node.right_child)
        expression += ')'
    else:
        expression += node.symbol
    return expression


def append2dict(predicates, row):
    """
    Append each element of the list to one of list - value of every key.

    Args:
        predicates (dict):
            Truth table holding values for each of the predicates.

        row (list):
            Combination of binary values to be added in the truth table.

    Returns:
        dict:
            Truth table obtained after appending the new row.

    """
    index = 0
    if row is None or predicates is None:
        return predicates
    if row == []:
        return predicates
    if len(row) == len(predicates):
        sortedpredicates = sorted(predicates.keys(), key=lambda x:x.lower())
        for predicate in sortedpredicates:
            predicates[predicate].append(row[index])
            index += 1
        return predicates


def get_true_rows(expression_result_values):
    """
    Determine the rows in the truth table.

    This is done by checking the list that holds those values.

    Args:
        expression_result_values:
            List of values determining whether a certain row is
            evaluated as true or not.

    Returns:
        list: Indexes of true rows.

    """
    if expression_result_values == [] or expression_result_values is None:
        return []
    true_rows = []
    for index in range(len(expression_result_values)):
        if expression_result_values[index] == 1:
            true_rows.append(index)
    return true_rows


def regex_validate(expression):
    """
    Validate input using regex.

    This function checks if the input respects standard pattern. The check
    is done recursively for each layer of the input. Multiple-operands operators
    are allowed, no one-operand operator is allowed except negation. Also,
    nand notation is not supported. Numbers are not allowed.

    Args:
        expression (str): Expression to be validated. Does not contain spaces.

    Returns:
        boolean: True if the input is according to standards, False otherwise.

    Note:
        Writing standards involve having opening bracket after operator symbol,
        having operands separated by commas and a closing bracket to separate
        from the rest of the expression.

    """
    if expression is None:
        return False
    if len(expression) == 1 and expression.isalpha():
        return True
    regex_pattern_binary = re.compile('^[&|>=]\([a-zA-Z()&|~>=,]+,[a-zA-Z()&|~>=,]+\)$')
    regex_pattern_unary = re.compile('^~\([a-zA-Z()&|~>=]\)$')
    if regex_pattern_binary.match(expression):
        left_operand = ''
        right_operand = ''
        count_closed = 0
        count_open = 0
        for index in range(2, len(expression)):
            if count_open == count_closed and expression[index] == ',':
                position = index + 1
                break
            if expression[index] == '(':
                count_open += 1
            if expression[index] == ')':
                count_closed += 1
            left_operand += expression[index]
        count_open = 0
        count_closed = 0
        for index in range(position, len(expression)):
            if count_open == count_closed and expression[index] == ')':
                break
            if expression[index] == '(':
                count_open += 1
            if expression[index] == ')':
                count_closed += 1
            right_operand += expression[index]
        return regex_validate(left_operand) and regex_validate(right_operand)
    if regex_pattern_unary.match(expression):
        operand = ''
        for index in range(2, len(expression) - 1):
            operand += expression[index]
        return regex_validate(operand)
    return False
