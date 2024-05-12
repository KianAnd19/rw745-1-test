# Assignment 6 Test Suite

This just tests whether your output can be run again through the parser and whether the output is the same as the input. This checks if your parser is outputting syntactically correct code and whether it produces the same output. Your parser could still be incomplete even if it passes all the tests.


## Usage 
Place the test_suitem folder in the same directory as your ANTLR files. Then run:
`python3 test_suite/test.py'

Your main must be named `Alan.java`, all your files should be compiled also. `Alan.java` should take in a file name as a parameter and parse and replace the code with labels and gotos and print out the result.