# Assignment 5 Test Suite

This checks your parser against the test cases provided for assignment 1 as well as the official test cases from 244.

## Usage 
Place the test_suitem folder in the same directory as your ANTLR files. Then run:
`python3 test_suite/test.py'

Your main must be named `Alan.java`, all your files should be compiled also. The test_suite assumes that your `Alan` class can parse a file given the filename as a paramater. The test_suite also assumes your `Alan` class at least outputs `Fails` or `Passes` to stdout (case sensitive).