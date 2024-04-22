# Assignment 4 Test Suite

This just tests whether the output of your pretty printer can be run through your pretty printer as an input again. This checks if your pretty printer is outputting syntactically correct code and whether it produces the same output. You pretty printer could still be incomplete even if it passes all the tests.

## Usage 
Place the test_suitem folder in the same directory as your ANTLR files. Then run:
`python3 test_suite/test.py'

Your main must be named `alanpp.java`, all your files should be compiled also. `alanpp.java` should take in a file name and a textwdith as parameters.