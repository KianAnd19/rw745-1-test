# Type Checking Test Suite

:warning: **This test suite is for the type checking part of the assignment only and only checks whether a testcase passes or fails, no idea if this is how it is marked.**:warning:

**The test suite also assumes your driver programs is set up correctly**

## Usage

First make sure all your files are compiled.

The testsuite runs `Main33.java` so make sure that is compiled as well. This test suite only checks type checking, as the test cases are the 244 type checking test cases.

Place the `test_suite` folder in you directory and run the following command:

`python3 test_suite/test_suite.py` in your assignment 3 directory.

**note the file has to run from outside the test_suite folder using the above command**

## Driver Output

Your program must output in the same format as the driver given from the Prof. In particular it has to output either `fails` or `passes` for each test case. This is how the testsute determines if the test case passed or failed. The test suite only determines if your program shoulf fail or pass and does not check the error messages themselves.

