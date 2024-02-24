import subprocess
from pathlib import Path
import sys

# ANSI escape codes
RED_BACKGROUND = '\033[41m'
GREEN_BACKGROUND = '\033[42m'
RED = '\033[91m'
GREEN = '\033[92m'
WHITE_TEXT = '\033[97m'  # White text color
RESET = '\033[0m'  # Resets the color to default

file_path_results = "Tests_Official/New_Results/"

if (len(sys.argv) > 1):
    if (sys.argv[1] == "-o"):
        file_path_results = "Tests_Official/Results/"


folder_path = Path('Tests_Official/TestCases/')
files = [item for item in folder_path.iterdir() if item.is_file()]
files.sort()
results = {}

def run_test(filename):
    with open(f'Tests_Official/TestCases/{filename}', 'rb') as input_file:
        result = subprocess.run(['antlr4-parse', '../alan.g4', 'source'], stdin=input_file, capture_output=True, text=True)

    if result.returncode == 0:
        with open(f"{file_path_results}{filename.split('.')[0]}.txt", 'r') as result_file:
            expected_output = result_file.read()
            if result.stderr == expected_output:
                results[filename] = "PASSED"
                print(GREEN + "Test passed" + RESET)
            else:
                results[filename] = "FAILED"
                print(RED + "Test failed")
                print("Expected output:\n", expected_output)
                print("Actual output:\n", result.stderr, RESET)
    else:
        print("Command failed with return code:", result.returncode)
        print("Error output:\n", result.stderr)

# Prints each file being tested
for file in files:
    print(file.name + " is being tested...")
    run_test(file.name)
    print("--------------------------------")

# Print the results
print("\n\nResults:")
for key, value in results.items():
    if value == "PASSED":
        # Print with a green background for passed results
        print(GREEN_BACKGROUND + WHITE_TEXT + key + " : " + value + RESET)
    else:
        # Print with a red background for failed results
        print(RED_BACKGROUND + WHITE_TEXT + key + " : " + value + RESET)