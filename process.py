import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import *
import pytest

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
import parser
=======
import expression_parser
>>>>>>> refactor(ALE1): Windows executable and final report
import builder
import dnf_computer
import nand_computer
import simplifier
import helpers
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
from tests import *
=======
import tests.test_builder
import tests.test_dnf_computer
import tests.test_helpers
import tests.test_nand_computer
import tests.test_parser
import tests.test_simplifier
# from tests import *
>>>>>>> refactor(ALE1): Windows executable and final report


symbols = ['~', '>', '&', '|', '=', '%']


def set_up_UI(app):
    """
    Set up the UI.

    This function sets the basic UI and connects its elements to the
    corresponding handlers.

    Args:
        app (tkinter.Tk): Application widget.

    Returns:
        tuple:
            tkinter.Message: Hash code label.
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b

            tkinter.Message: Full dnf label.

            tkinter.Label: Simplified dnf label.

=======

            tkinter.Message: Full dnf label.

            tkinter.Label: Simplified dnf label.

>>>>>>> refactor(ALE1): Windows executable and final report
            tkinter.Message: Nand label.

            tkinter.Message: Test label.

    """
    frame = Frame(app, width=470, height=470)
    frame.pack()
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b

    entry = Entry(frame)
    entry.pack()
    entry.focus_set()
=======

    entry = Entry(frame)
    entry.pack()
    entry.focus_set()

    announce_hash_code = Message(frame, text='Hash Code')
    hash_label = Message(frame, text='')
    announce_dnf = Message(frame, text='Dnf')
    dnf_label = Message(frame, text='')
    announce_dnf_simplified = Label(frame, text='Dnf Simplified')
    dnf_simplified_label = Label(frame, text='')
    announce_nand = Label(frame, text='Nand')
    nand_label = Label(frame, text='')

    announce_hash_code.pack()
    hash_label.pack()
    announce_dnf.pack()
    dnf_label.pack()
    announce_dnf_simplified.pack()
    dnf_simplified_label.pack()
    announce_nand.pack()
    nand_label.pack()

    test_label = Message(frame, text='')
    test_label.pack()

    btn_parse = Button(frame, text='Parse', command=lambda: handle_parse(
        app,
        frame,
        entry.get()))
    btn_tests = Button(frame, text='Tests', command=lambda: run_tests(app, frame))
    btn_parse.pack(side="bottom")
    btn_tests.pack()

    return frame, hash_label, dnf_label, dnf_simplified_label, nand_label, test_label
>>>>>>> refactor(ALE1): Windows executable and final report

    announce_hash_code = Message(frame, text='Hash Code')
    hash_label = Message(frame, text='')
    announce_dnf = Message(frame, text='Dnf')
    dnf_label = Message(frame, text='')
    announce_dnf_simplified = Label(frame, text='Dnf Simplified')
    dnf_simplified_label = Label(frame, text='')
    announce_nand = Message(frame, text='Nand')
    nand_label = Message(frame, text='')

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
    announce_hash_code.pack()
    hash_label.pack()
    announce_dnf.pack()
    dnf_label.pack()
    announce_dnf_simplified.pack()
    dnf_simplified_label.pack()
    announce_nand.pack()
    nand_label.pack()

    test_label = Message(frame, text='')
    test_label.pack()

    btn_parse = Button(frame, text='Parse', command=lambda: handle_parse(
        app,
        frame,
        entry.get()))
    btn_tests = Button(frame, text='Tests', command=lambda: run_tests(app, frame))
    btn_parse.pack(side="bottom")
    btn_tests.pack()

    return frame, hash_label, dnf_label, dnf_simplified_label, nand_label, test_label


def run_tests(app, frame):
    """
    Run unit tests.

    The function takes the exist code of the tests and displays an interpreted
    message based on the value. It also destroys the frame at each call and
    initializes the UI

    Args:
        app (tkinter.Tk): Widget application.

=======
def run_tests(app, frame):
    """
    Run unit tests.

    The function takes the exist code of the tests and displays an interpreted
    message based on the value. It also destroys the frame at each call and
    initializes the UI

    Args:
        app (tkinter.Tk): Widget application.

>>>>>>> refactor(ALE1): Windows executable and final report
        frame (tkinter.Frame): Widget that holds all the UI components.

    """
    frame.destroy()
    exit_status = pytest.main()
    test_label = set_up_UI(app)[-1]
    if exit_status == 0:
        test_label['text'] = 'All tests were collected and passed successfully'
    if exit_status == 1:
        test_label['text'] = 'Tests were collected and run but some of the tests failed'
    if exit_status == 2:
        test_label['text'] = 'Test execution was interrupted by the user'
    if exit_status == 3:
        test_label['text'] = 'Internal error happened while executing tests'
    if exit_status == 4:
        test_label['text'] = 'Pytest usage error'
    if exit_status == 5:
        test_label['text'] = 'No tests were collected'


def handle_parse(
        app,
        frame,
        input_expression):
    """
    Parse input expression.

    This function represents the handler for parsing
    an expression. It prepares the expression for parsing, and represents
    the entrypoint for parsing, rendering the application in graphical form,
    computing the expression's truth values and simplifying the table.
    At each execution, it destroys the existing interface and builds it up with
    the updated information.

    Args:
        app (tkinter.Tk): The application widget.

        frame (tkinter.Frame): The frame that holds all the UI widgets.

        input_expression (str): Propositional expression to be parsed.

    """
    frame.destroy()
    frame, hash_label, dnf_label, dnf_simplified_label, nand_label = \
        set_up_UI(app)[0:-1]
    expression = input_expression.replace(" ", "")
    if not expression:
        validated = False
    else:
        validated = helpers.regex_validate(expression)
    if validated:
        if len(expression) > 1:
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
            root, predicates = parser.convert2tree(expression)
            parser.render_tree(root)
=======
            root, predicates = expression_parser.convert2tree(expression)
            expression_parser.render_tree(root)
>>>>>>> refactor(ALE1): Windows executable and final report
            expression_result_values = builder.compute_result(root, predicates)
            truth_table = builder.TruthTable(frame, predicates, expression_result_values, expression)
            dnf_full = dnf_computer.compute_dnf(predicates, expression_result_values)
            simplified_predicates, simplified_expression_result_values = \
                simplifier.compute_simplified_predicates(predicates, expression_result_values)
            simplified_truth_table = builder.TruthTable(
                frame, simplified_predicates, simplified_expression_result_values, expression)
            dnf_simplified = dnf_computer.compute_simplified_dnf(simplified_predicates)
            nand_dnf = nand_computer.compute_nand(simplified_predicates, simplified_expression_result_values)
        elif expression.isalpha():
<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
            root = parser.Node(expression)
            root.label = '0'
            parser.render_tree(root)
=======
            root = expression_parser.Node(expression)
            root.label = '0'
            expression_parser.render_tree(root)
>>>>>>> refactor(ALE1): Windows executable and final report
            predicates = {expression: [0, 1]}
            expression_result_values = [0, 1]
            truth = builder.TruthTable(frame, predicates, expression_result_values, expression)
            dnf_full = expression
            simplified_predicates = predicates
            simplified_expression_result_values = expression_result_values
            simplified_truth_table = builder.TruthTable(
                frame, simplified_predicates, simplified_expression_result_values, expression)
            dnf_simplified = dnf_full
            nand_dnf = '%(%({}, {}), %({}, {}))'.format(
                expression, expression, expression, expression)

<<<<<<< 7829042473e459aa2bae2b41a6d9d7cf216a379b
        hash_code = parser.generate_hash_code(expression_result_values)
=======
        hash_code = expression_parser.generate_hash_code(expression_result_values)
>>>>>>> refactor(ALE1): Windows executable and final report
        hash_label['text'] = hash_code
        dnf_label['text'] = dnf_full
        dnf_simplified_label['text'] = dnf_simplified
        nand_label['text'] = nand_dnf


def main():
    """
    Start the application.

    This function represents the entry point in the application.
    It starts the processes of creating handling the user interaction with
    the UI.

    """
    app = Tk()
    app.wm_title('Expression analyzer')
    app.minsize(300, 300)
    set_up_UI(app)
    app.mainloop()


if __name__ == '__main__':
    main()
