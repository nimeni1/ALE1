import helpers
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
import parser
=======
import expression_parser
>>>>>>> refactor(ALE1): Windows executable and final report


def compute_nand(predicates, expression_result_values):
    """
    Nandify expression.

    This function makes use of the dnf and a tree structure.

    Args:
        predicates (dict):
            Holds the truth table of the predicates.

        expression_result_values (list):
            Truth values for each possible combination of the predicates.

    Returns:
        str: Nandified form of the expression.

    """
    if predicates == {} or predicates is None \
        or expression_result_values == [] or expression_result_values is None:
        return ''
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    line_root = parser.Node('%')
    temporary_line_root = line_root
    root = parser.Node('%')
=======
    if len(predicates) == 1:
        for predicate in predicates:
            expression = predicate
        nand = '%(%({}, {}), %({}, {}))'.format(
            expression, expression, expression, expression)
        return nand
    line_root = expression_parser.Node('%')
    temporary_line_root = line_root
    root = expression_parser.Node('%')
>>>>>>> refactor(ALE1): Windows executable and final report
    root.label = 'root'
    temporary_root = root
    rows_nand = []
    count_lines = 0
    count_ones = 0
    sortedpredicates = sorted(predicates.keys(), key=lambda x:x.lower())
    for index in range(len(expression_result_values)):
        if expression_result_values[index] == 1:
            count_ones += 1
    for index in range(len(expression_result_values)):
        if expression_result_values[index] == 1:
            count_lines += 1
            nodes = []
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
            line_root = parser.Node('%')
=======
            line_root = expression_parser.Node('%')
>>>>>>> refactor(ALE1): Windows executable and final report
            temporary_line_root = line_root
            count_pred = 0
            count_no_stars = 0
            for predicate in sortedpredicates:
                if predicates[predicate][index] != '*':
                    count_no_stars += 1
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
            for predicate in sortedpredicates:
                if predicates[predicate][index] != '*':
                    count_pred += 1
                    node = parser.Node(predicate)
                    if predicates[predicate][index] == 0:
                        child = node
                        node = parser.Node('%')
                        node.left_child = child
                        node.right_child = child
                        child.parent = node
                    if count_pred == count_no_stars:
                        temporary_line_root.right_child = node
                        node.parent = temporary_line_root
                    else:
                        temporary_line_root.left_child = node
                        node.parent = temporary_line_root
                        if count_pred != count_no_stars - 1:
                            temporary_line_root.right_child = parser.Node('%')
                            temporary_line_root.right_child.parent = temporary_line_root
                            temporary_line_root = temporary_line_root.right_child
                            duplicate_node = parser.Node('%')
                            temporary_line_root.left_child = duplicate_node
                            temporary_line_root.right_child = duplicate_node
                            duplicate_node.parent = temporary_line_root
                            temporary_line_root = duplicate_node
=======
            if count_no_stars == 1:
                for predicate in predicates:
                    symbol = predicate
                temporary_line_root.left_child = expression_parser.Node(symbol)
                temporary_line_root.right_child = expression_parser.Node(symbol)
                temporary_line_root.left_child.parent = temporary_line_root
                temporary_line_root.right_child.parent = temporary_line_root
            else:
                for predicate in sortedpredicates:
                    if predicates[predicate][index] != '*':
                        count_pred += 1
                        node = expression_parser.Node(predicate)
                        if predicates[predicate][index] == 0:
                            child = node
                            node = expression_parser.Node('%')
                            node.left_child = child
                            node.right_child = child
                            child.parent = node
                        if count_pred == count_no_stars:
                            temporary_line_root.right_child = node
                            node.parent = temporary_line_root
                        else:
                            temporary_line_root.left_child = node
                            node.parent = temporary_line_root
                            if count_pred != count_no_stars - 1:
                                temporary_line_root.right_child = expression_parser.Node('%')
                                temporary_line_root.right_child.parent = temporary_line_root
                                temporary_line_root = temporary_line_root.right_child
                                duplicate_node = expression_parser.Node('%')
                                temporary_line_root.left_child = duplicate_node
                                temporary_line_root.right_child = duplicate_node
                                duplicate_node.parent = temporary_line_root
                                temporary_line_root = duplicate_node
>>>>>>> refactor(ALE1): Windows executable and final report
            if count_lines == count_ones:
                temporary_root.right_child = line_root
                temporary_root.right_child.parent = temporary_root
                if count_ones == 1:
                    temporary_root.left_child = line_root
                    temporary_root.left_child.parent = line_root
            else:
                temporary_root.left_child = line_root
                temporary_root.left_child.parent = temporary_root
                if count_lines != count_ones - 1:
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
                    temporary_root.right_child = parser.Node('%')
                    temporary_root.right_child.parent = temporary_root
                    temporary_root = temporary_root.right_child
                    duplicate_node = parser.Node('%')
=======
                    temporary_root.right_child = expression_parser.Node('%')
                    temporary_root.right_child.parent = temporary_root
                    temporary_root = temporary_root.right_child
                    duplicate_node = expression_parser.Node('%')
>>>>>>> refactor(ALE1): Windows executable and final report
                    temporary_root.left_child = duplicate_node
                    temporary_root.right_child = duplicate_node
                    duplicate_node.parent = temporary_root
                    temporary_root = duplicate_node
    nand = helpers.convert2expression(root)
    return nand
