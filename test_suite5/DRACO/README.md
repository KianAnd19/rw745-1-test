# Assignment 5 Test Suite

:warning: I haven't actually tested this, I just copied the ALAN test_suite, but it should work. :warning:

This checks your parser against the test cases provided for assignment 2.

## Usage 
Place the test_suitem folder in the same directory as your ANTLR files. Then run:
`python3 test_suite/test.py'

Your main must be named `Draco.java`, all your files should be compiled also. The test_suite assumes that your `Draco` class can parse a file given the filename as a paramater. The test_suite also assumes your `Draco` class at least outputs `Fails` or `Passes` to stdout (case sensitive).