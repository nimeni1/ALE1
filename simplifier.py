import copy

import helpers


def check_table_simplified(predicates):
    """
    Check if table can be simplified.

    This function providies the stopping condition for the simplifying
    truth table function. A truth table can not be simplified any longer
    when no simplifying combination can be found.

    Args:
        predicates (dict): Dictionary of predicates, keeps track of the values
            a predicate can take. Serves as truth table.

    Returns:
        boolean: Value that states whether the table can be simplified or not.

    """
    if predicates is None:
        return False
    for predicate in predicates:
        if predicates[predicate] == [] or predicates[predicate] is None:
            return False
    nr_rows = helpers.get_nr_rows(predicates)
    count = 0
    for predicate in predicates:
        for i in range(nr_rows - 1):
            for j in range(i + 1, nr_rows):
                if predicates[predicate][i] != predicates[predicate][j]:
                    for p in predicates:
                        if p != predicate and predicates[p][i] != '*' and predicates[p][i] == predicates[p][j]:
                            return True
    return False


def check_stars(row):
    """
    Check if the given row can be simplified.

    A row cannot be simplified any longer when it has n - 1 stars.
    The method also checks for empty row.

    Args:
        row (list): Row of the truth table to check for simplification.

    Returns:
        boolean: Value that states whether the row can be simplified or not.

    """
    if row is None:
        return False
    if row == []:
        return True

    count = 0
    for i in range(len(row)):
        if row[i] == '*':
            count += 1
    if count >= len(row) - 1:
        return False
    return True


def generate_expansion(row, predicates, expression_result_values):
    """
    Generate expansion of a simplified row and check its validity.

    This is done by checking if the simplified row may represent a row that
    yields a 0 as the result of the expression. This function 'expands' the
    simplified row into all the possibilities it may represent, and does just
    that for each one of them.

    Args:
        row (list): Simplified row.

        predicates (dict):
            Truth table holding binary values for each of the predicates.

        expression_result_values (list):
            Results of the full truth table.

    Returns:
        boolean: True if the simplification is valid, False otherwise.

    """
    if row is None:
        return False
    if len(row) == 0:
        return False
    if predicates is None or len(predicates) == 0 or \
        expression_result_values == [] or expression_result_values is None:
        return False
    for predicate in predicates:
        if len(predicates[predicate]) == 0:
            return False
    if len(row) == len(predicates):
        found_star = False
        for element in row:
            if element == '*':
                found_star = True
                break
        sortedpredicates = sorted(predicates.keys(), key=lambda x:x.lower())
        for predicate in sortedpredicates:
            nr_rows = len(predicates[predicate])
            break
        if not found_star:
            for index in range(nr_rows):
                i = 0
                check_row_identity = True
                for predicate in sortedpredicates:
                    if predicates[predicate][index] != row[i]:
                        check_row_identity = False
                        break
                    i += 1
                if check_row_identity:
                    if expression_result_values[index] == 0:
                        return False
            return True

        expanded = []
        for index in range(len(row)):
            if row[index] == '*':
                expanded_row1 = copy.deepcopy(row)
                expanded_row1[index] = 0
                expanded_row2 = copy.deepcopy(row)
                expanded_row2[index] = 1
                check_row1 = generate_expansion(
                    expanded_row1, predicates, expression_result_values)
                check_row2 = generate_expansion(
                    expanded_row2, predicates, expression_result_values)
                if check_row1 and check_row2:
                    return True
                return False


def compute_intermediate_simplified(
        expression_result_values,
        predicates,
        simplified_predicates,
        simplified_expression_result_values):
    """
    Compute intermediate simplified truth table.

    An intermediate simplification table is the one obtained by simplifying
    any 2 rows in the table, as long as they haven't been simplified before.
    If the number of the rows to simplify is odd, the remaining row is appended
    for a possible next round of simplification.

    Args:
        expression_result_values (list):
            Result values for every instance of the initial truth table.

        predicates (dict):
            Initial truth table to be simplified.

        simplified_predicates (dict):
            Table which may or may not have been simplified before, but it is
            subject to simplification.

        simplified_expression_result_values (list):
            Result values for every instance of the intermediate
            simplified table.

    Returns:
        tuple:
            dict: Simplified dictionary.

            list: Results of the newly simplified dictionary.

            boolean: True if the function finds possible simplifications,
                False otherwise.

    """
    auxiliary_predicates = {}
    auxiliary_predicates2 = {}
    for predicate in predicates:
        auxiliary_predicates[predicate] = []
        auxiliary_predicates2[predicate] = []
    auxiliary_simplified_expression_values = []
    simplified_rows = []
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
=======
    tautologic_rows = []
>>>>>>> refactor(ALE1): Windows executable and final report
    for predicate in simplified_predicates:
        nr_rows = len(simplified_predicates[predicate])
        break
    sortedpredicates = sorted(simplified_predicates.keys(), key=lambda x:x.lower())
    for row_index in range(nr_rows):
        if simplified_expression_result_values[row_index] == 1:
            for predicate in sortedpredicates:
                current_value = simplified_predicates[predicate][row_index]
                for row_index2 in range(row_index + 1, nr_rows):
                    simplified = []
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
                    row1 = []
                    row2 = []
                    for p in sortedpredicates:
                        row1.append(simplified_predicates[p][row_index])
                        row2.append(simplified_predicates[p][row_index2])
=======
>>>>>>> refactor(ALE1): Windows executable and final report
                    true_rows = helpers.get_true_rows(simplified_expression_result_values)
                    if len(true_rows) - 1 == len(simplified_rows):
                        last_index = true_rows[-1]
                        simplified_rows.append(last_index)
                        for predicate in sortedpredicates:
                            simplified.append(simplified_predicates[predicate][last_index])
                        auxiliary_predicates = helpers.append2dict(auxiliary_predicates, simplified)
                        auxiliary_simplified_expression_values.append(1)
                    else:
                        if row_index not in simplified_rows and row_index2 not in simplified_rows:
                            if current_value != simplified_predicates[predicate][row_index2]:
                                for predicate2 in sortedpredicates:
                                    if predicate == predicate2:
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
                                        simplified.append('*')
=======
                                        if len(predicates) != 1:
                                            simplified.append('*')
>>>>>>> refactor(ALE1): Windows executable and final report
                                    else:
                                        if simplified_predicates[predicate2][row_index] != simplified_predicates[predicate2][row_index2]:
                                            simplified.append('*')
                                        else:
                                            simplified.append(simplified_predicates[predicate2][row_index])
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
                                if generate_expansion(simplified, predicates, expression_result_values):
=======
                                tautologic_row = True
                                for value in simplified:
                                    if value != '*':
                                        tautologic_row = False
                                        break
                                if tautologic_row:
                                    tautologic_rows.append(row_index)
                                    tautologic_rows.append(row_index2)
                                if not tautologic_row and generate_expansion(simplified, predicates, expression_result_values):
>>>>>>> refactor(ALE1): Windows executable and final report
                                    auxiliary_predicates = helpers.append2dict(auxiliary_predicates, simplified)
                                    auxiliary_simplified_expression_values.append(1)
                                    simplified_rows.append(row_index)
                                    simplified_rows.append(row_index2)
    true_rows = helpers.get_true_rows(expression_result_values)
    if len(true_rows) == 1:
        only_row = []
        for p in predicates:
            only_row.append(predicates[p][true_rows[0]])
        auxiliary_predicates = helpers.append2dict(auxiliary_predicates, only_row)
        auxiliary_simplified_expression_values = [1]

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
=======
    for index in range(len(tautologic_rows)):
        found = False
        for index2 in range(len(simplified_rows)):
            if tautologic_rows[index] == simplified_rows[index2]:
                found = True
        if not found:
            row = []
            for predicate in sortedpredicates:
                row.append(simplified_predicates[predicate][tautologic_rows[index]])
            auxiliary_predicates = helpers.append2dict(auxiliary_predicates, row)
            auxiliary_simplified_expression_values.append(1)

>>>>>>> refactor(ALE1): Windows executable and final report
    simplification_flag = False
    if auxiliary_predicates != auxiliary_predicates2:
        simplification_flag = True
        simplified_predicates = auxiliary_predicates
        simplified_expression_result_values = auxiliary_simplified_expression_values
    return simplified_predicates, simplified_expression_result_values, simplification_flag


def compute_simplified_predicates(
        predicates,
        expression_result_values,
        simplified_predicates=None,
        simplified_expression_result_values=None):
    """
    Compute simplified truth table.

    Recursive function that generates all the possible row combinations and
    performs checks on the table's values. Finally, a new truth table is
    generated after a round of simplifications. The stopping condition is
    either all the rows have N - 1 number of stars in them (where N is the
    row length), either there are no possible combinations that would make for
    a simplification.

    Args:
        predicates (dict): Dictionary of predicates, keeps track of the values
            a predicate can take. Serves as truth table.

    Returns:
        tuple:
            dict: Dictionary representing the simplified truth table.

            list: Simplified expression result values.

    """
    if predicates is None or predicates == {} or \
        expression_result_values == [] or expression_result_values is None:
        return predicates, expression_result_values

    if simplified_predicates is None:
        simplified_predicates = {}
        for predicate in predicates:
            simplified_predicates[predicate] = []
            for i in range(len(predicates[predicate])):
                simplified_predicates[predicate].append(predicates[predicate][i])

    if simplified_expression_result_values is None:
        simplified_expression_result_values = []
        for value in expression_result_values:
            simplified_expression_result_values.append(value)

    simplified_predicates, \
    simplified_expression_result_values, \
    simplification_flag = \
        compute_intermediate_simplified(
            expression_result_values,
            predicates,
            simplified_predicates,
            simplified_expression_result_values)
    if check_table_simplified(simplified_predicates) and simplification_flag:
        return compute_simplified_predicates(
                predicates,
                expression_result_values,
                simplified_predicates,
                simplified_expression_result_values)
    return simplified_predicates, simplified_expression_result_values
