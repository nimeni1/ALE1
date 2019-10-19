import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import *

import helpers
import process


class TruthTable:
    def __init__(self, frame, predicates, expression_result_values, expression):
        self.tree = None
        self.frame = frame
        sortedpredicates = sorted(predicates.keys(), key=lambda x:x.lower())
        self.column_headers = sortedpredicates
        self.column_headers.append(expression)

        self.table_values = self.dict2list(predicates)
        self.expression_result_values = expression_result_values
        self.table_values.append(self.expression_result_values)

        self._setup()
        self._build()

    def dict2list(self, dictionary):
        """
        Convert dictionary to list.

        This is done by taking every value from the dictionary and putting
        it in a list.

        Args:
            dictionary (dict): Dictionary to convert (whose values are to be
                extracted).

        Returns:
            list: List of the values obtained from the dictionary.

        """
        l = []
        sortedkeys = sorted(dictionary.keys(), key=lambda x:x.lower())
        for key in sortedkeys:
            l.append(dictionary[key])
        return l

    def _setup(self):
        """
        Set up the interface for displaying the truth table.

        """
        container = ttk.Frame(self.frame)
        container.pack(fill='both', expand=True, side='right')

        self.tree = ttk.Treeview(columns=self.column_headers, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)

        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)


    def _build(self):
        """
        Build the truth table on the UI.

        """
        for column in self.column_headers:
            self.tree.heading(column, text=column.title())
        for column in self.column_headers:
            self.tree.column(column,
                width=tkFont.Font().measure(column.title()))
        for row_index in range(len(self.table_values[0])):
            tmp = []
            for column_index in range(len(self.table_values)):
                tmp.append(self.table_values[column_index][row_index])
            self.tree.insert('', 'end', values=tmp)
            for index, value in enumerate(tmp):
                column_width = tkFont.Font().measure(value)
                if self.tree.column(self.column_headers[index], width=None) < column_width:
                    self.tree.column(self.column_headers[index], width=column_width)


def create_table(predicates):
    """
    Create truth table.

    This function creates the truth table before the expression
    can be assessed.

    Args:
        predicates (dict): Dictionary storing predicates.

    Returns:
        list: List of lists, representing the truth table for a number of
            predicates.

    """
    if predicates == {} or predicates is None:
        return [[]]
    index = 0
    nr_columns = len(predicates)
    nr_rows = 2 ** len(predicates)
    table = [[0 for i in range(nr_rows)] for j in range(nr_columns)]
    sortedpredicates = sorted(predicates.keys(), key=lambda x:x.lower())
    for key in sortedpredicates:
        predicates[key] = table[index]
        index += 1
    for i in range(nr_columns):
        value = 0
        group_size = 2 ** (nr_columns - (i + 1))
        for j in range(nr_rows):
            if i == 0:
                if j < nr_rows / 2:
                    table[i][j] = 0
                else:
                    table[i][j] = 1
            else:
                if group_size != 0:
                    group_size -= 1
                else:
                    value = (value + 1) % 2
                    group_size = 2 ** (nr_columns - (i + 1)) - 1
                table[i][j] = value
    return table


def initialize_tree(node, predicates, row_index):
    """
    Initialize tree data structure with binary values.

    Args:
        node (parser.Node): Node of the parser.

        predicates (dict): Dictionary of predicates, keeps track of the values
            a predicate can take. Serves as truth table.

        row_index (int): Index keeping track of a row in the table. Used for
            retrieving the value to be stored in the current node.

    """
    if node is None or predicates == {} or predicates is None:
        return
    for predicate in predicates:
        if predicates[predicate] == [] or predicates[predicate] is None:
            return
    is_parent = False
    if node.left_child:
        initialize_tree(node.left_child, predicates, row_index)
        is_parent = True
    if node.right_child:
        initialize_tree(node.right_child, predicates, row_index)
        is_parent = True
    if is_parent:
        return
    node.value = predicates[node.symbol][row_index]


def compute_node_value(node):
    """
    Evaluate truth value for a given node.

    This function peforms some checks on the type of operator and sets truth
    value to the given node according to that. This is done recursively by
    calling the function on the current node's children.

    Args:
        node (parser.Node): Given node to compute truth value for.

    Returns:
        int: Binary value that identifies the truth value of the current node.

    """
    if node is None:
        return None
    if node.symbol is None:
        return None

    if node.symbol == '~':
        if node.left_child is None:
            return None
        operand_to_negate = compute_node_value(node.left_child)
        node.value = (operand_to_negate + 1) % 2

    if node.symbol in [binary_operator for binary_operator in process.symbols if binary_operator != '~']:
        if node.left_child is None or node.right_child is None:
            return None
        left_operand = compute_node_value(node.left_child)
        right_operand = compute_node_value(node.right_child)

        if node.symbol == '&':
            node.value = left_operand & right_operand
        if node.symbol == '|':
            node.value = left_operand | right_operand
        if node.symbol == '>':
            if left_operand == 1 and right_operand == 0:
                node.value = 0
            else:
                node.value = 1
        if node.symbol == '=':
            node.value = (left_operand ^ right_operand + 1) % 2

    return node.value


def compute_result(root, predicates):
    """
    Compute truth table for the input expression.

    Args:
        root (parser.Node): Root of the tree to compute the table for.

        predicates (dict): Dictionary of predicates, keeps track of the values
            a predicate can take. Serves as truth table.

    Returns:
        list: Truth values for the given table.

    """
    if root is None or predicates is None or predicates == {}:
        return []
    expression_result_values = []
    table = create_table(predicates)
    nr_rows = helpers.get_nr_rows(predicates)
    for row_index in range(nr_rows):
        initialize_tree(root, predicates, row_index)
        expression_result_values.append(compute_node_value(root))
    return expression_result_values
