Decisions:
-generating expansion of simplified row instead of holding initial rows for each new simplified
-opting for traversing the table instead of generating all the possibilities and then simplifying
because of added complexity in function size and number of variables
-one node class
-no global variables
-class file
-parsing to tree file
-computing result values file
-simplify table file
-computing dnf file
-computing nand file
-using dictionary as primary data structure for the truth table
-using tree to compute nand form of the expression starting from dnf
-creating intermediate nand form before fixing the negations using a '%' wrapper around them
-using plain string manipulation to compute dnf
-choice of keeping functions rather modular, even if their functionality is used only once per UI
trigger (keeping functions as self-contained as possbile, with intuitive naming)
-documentation added for each written function
-separate tests folder
-similar separation of the tests files as the functionality files
-use of pytest
-use of python
-having pytest triggered by user interaction with the interface
-sanitizing input and allowing for operators with multiple operands

Simplifying table:
Auxiliary predicates for holding intermediate simplified truth table; the
intermediate table cannot be modified as it contains values from the previous recursive
call and finding algorithmic workarounds would rather complicate the problem instead of
simplifying it.
A dictionary for holding the values of the main truth table data structure but without holding the reference to the
variable itself. Main table is sent as parameter recursively for call on method which
performs checking on intermediate table.

Input is partially trusted for computing node value. Checking for missing
children in a recursive function would make the function work well on side cases
when input is not proper, but will fail on any other case where the application
follows the main scenario. A workaround for this would be to set reference from
the current evaluated node to its parent and check for its existence. But this would
introduce the assumption that the child has a node set as its parent. So instead a
parameter to indicate this is sent to the next recursive call.

Input is validated in almost every function. The idea is that functions that
belong to the same functionality can be seen as standalone blocks even if for
convenience (meaning readability as well as testing purposes) they have been
split, they occur in predetermined places in the application. So in the case
of a function making use of some others, validating the input in the former
guarantees validated input in the latter, given that the latter is not called
in any other places in the code. But this is considered to be the starting
point of this structure. This is the case of computing the simplified table
functionality.
The only exception are the functions that are tied to the UI, having the purpose
of initializing the interface or modifying it according to the logic. Also, functions
that create files or build data structure belonging to external libraries such
as graphviz are not tested either.

Parsing the expression into a tree data structure is made by iterating once over the whole
string. A counter label is held to identify each Node uniquely.

Regex validation also checks for input that contains white spaces, which should result
in a False evaluation. The input is filtered at the entry point in the application, but
since that function cannot be tested as it interacts with the interface, the regex
validation function is tested with additional missing/null input parameters.

Dependencies:
-graphviz
-pytest
-tkinter

graphviz and tkinter installed on the machine, pytest with pip

Add current directory to PYTHONPATH

Inside this archive you will find 3 things:
1. The design report.
2. Executable of the application (process folder).
3. Source code (ALE1 folder).

For the application to run there is no additional installation needed.
This includes any kind of libraries or even the python interpreter.
The executable can be found under the name of 'process' of type 
Application.

To run the tests individually from the command line, you will have
to add the path to the main source code folder in the PYTHONPATH.
Moreover, you will have to install pytest by issuing 'pip install pytest'.
To run a specific test you can "pytest -k 'name_of_the_test'". 
To run the application from the source code, you will have to
'pip install graphviz' as well.

The assumption is made that graphviz is installed on the machine that runs
the application and that the path environment variable is set accordingly.
