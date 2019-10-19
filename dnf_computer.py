<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
import parser
=======
import expression_parser
>>>>>>> refactor(ALE1): Windows executable and final report


def build_line_dnf(nodes):
    """
    Build dnf expression for given nodes on the same row.

    Recursive helper function for computing a dnf expression from a truth table.

    Args:
        nodes (list): Nodes belonging to the same line in the truth table.

    Returns:
        str: Expression that represents

    """
    line_expression = ''
    if nodes is None:
        return line_expression
    if len(nodes) == 0:
        return line_expression
    if len(nodes) == 1:
        node = nodes.pop(0)
        if node.symbol != '~':
            line_expression = node.symbol
        else:
            line_expression += '~'
            line_expression += '('
            line_expression += node.left_child.symbol
            line_expression += ')'
        return line_expression
    node = nodes.pop(0)
    line_expression = '&'
    line_expression += '('
    if node.symbol == '~':
        line_expression += '~'
        line_expression += '('
        line_expression += node.left_child.symbol
        line_expression += ')'
    else:
        line_expression += node.symbol
    line_expression += ','
    line_expression += build_line_dnf(nodes)
    line_expression += ')'
    return line_expression


def build_full_dnf(rows):
    """
    Build full dnf expression.

    Recursive helper function for computing a full dnf given intermediate
    expressions for all the valid lines (resulting in true value) in the truth
    table.

    Args:
        rows (list): ASCII dnfs for all the valid rows in truth table.

    Returns:
        str: Full dnf.

    """
    if rows is None:
        return ''
    if rows == [''] or rows == []:
        return ''
    if len(rows) == 1:
        return rows.pop()
    full_expression = '|'
    full_expression += '('
    full_expression += rows.pop(0)
    full_expression += ','
    full_expression += build_full_dnf(rows)
    full_expression += ')'
    return full_expression


def compute_dnf(predicates, expression_result_values):
    """
    Compute disjunctive normal form.

    This function computes dnf by creating an intermediate list of nodes for
    each of the valid rows and transform each one of them in ASCII form.

    Args:
        predicates (dict): All possible value combinations of the predicates.

        expression_result_values (list): Truth values of the input expression
            evaluated for each of the rows in the truth table.

    Returns:
        str: ASCII expression of the disjunctive normal form of the given
            truth table.

    """
    if predicates == {} or predicates is None:
        return ''
    if expression_result_values == [] or expression_result_values is None:
        return ''
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
=======
    if len(predicates) == 1:
        for predicate in predicates:
            dnf = predicate
            break
        return dnf
>>>>>>> refactor(ALE1): Windows executable and final report
    rows_dnf = []
    sortedpredicates = sorted(predicates.keys(), key=lambda x:x.lower())
    for index in range(len(expression_result_values)):
        if expression_result_values[index] == 1:
            nodes = []
            for predicate in sortedpredicates:
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
                node = parser.Node(predicate)
                if predicates[predicate][index] == 0:
                    parent = parser.Node('~')
=======
                node = expression_parser.Node(predicate)
                if predicates[predicate][index] == 0:
                    parent = expression_parser.Node('~')
>>>>>>> refactor(ALE1): Windows executable and final report
                    parent.left_child = node
                    nodes.append(parent)
                else:
                    nodes.append(node)
            line_expression = build_line_dnf(nodes)
            rows_dnf.append(line_expression)
    dnf = build_full_dnf(rows_dnf)
    return dnf


def compute_simplified_dnf(simplified_table):
    """
    Compute disjunctive normal form for simplified table.

    This function computes dnf by creating an intermediate list of nodes
    and transform it in ASCII form.

    Args:
        simplified_table (dict): Simplified truth table.

    Returns:
        str: ASCII expression of the disjunctive normal form of the given
            simplified truth table.

    """
    if simplified_table == {} or simplified_table is None:
        return ''
    rows_dnf = []
    for predicate in simplified_table:
        nr_rows = len(simplified_table[predicate])
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    sortedpredicates = sorted(simplified_table.keys(), key=lambda x:x.lower())
    for index in range(nr_rows):
        nodes = []
        for predicate in sortedpredicates:
            node = parser.Node(predicate)
            if simplified_table[predicate][index] == 0:
                parent = parser.Node('~')
                parent.left_child = node
                nodes.append(parent)
            if simplified_table[predicate][index] == 1:
                nodes.append(node)
        if len(nodes) > 1:
            line_expression = build_line_dnf(nodes)
        else:
            unique_node = nodes.pop()
            if unique_node.symbol != '~':
                line_expression = unique_node.symbol
            else:
                line_expression = '~({})'.format(unique_node.left_child.symbol)
        rows_dnf.append(line_expression)
=======
        break
    if len(simplified_table) == 1:
        for predicate in simplified_table:
            dnf = predicate
            break
        return dnf
    sortedpredicates = sorted(simplified_table.keys(), key=lambda x:x.lower())
    for index in range(nr_rows):
        nodes = []
        if len(sortedpredicates) > 1:
            for predicate in sortedpredicates:
                node = expression_parser.Node(predicate)
                if simplified_table[predicate][index] == 0:
                    parent = expression_parser.Node('~')
                    parent.left_child = node
                    nodes.append(parent)
                if simplified_table[predicate][index] == 1:
                    nodes.append(node)
            if len(nodes) > 1:
                line_expression = build_line_dnf(nodes)
            else:
                unique_node = nodes.pop()
                if unique_node.symbol != '~':
                    line_expression = unique_node.symbol
                else:
                    line_expression = '~({})'.format(unique_node.left_child.symbol)
            rows_dnf.append(line_expression)
>>>>>>> refactor(ALE1): Windows executable and final report
    dnf = build_full_dnf(rows_dnf)
    return dnf
