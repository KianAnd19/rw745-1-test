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

file_path_results = "test_suite/test_cases/"

if (len(sys.argv) > 1):
    if (sys.argv[1] == "-o"):
        file_path_results = "test_suite/test_cases/"


folder_path = Path('test_suite/test_cases')
files_passing = [item for item in folder_path.iterdir() if item.is_file()]
files_passing.sort()

results = {}
def run_passing(filename):
    with open(f'test_suite/test_cases/{filename}', 'rb') as input_file:
        result = subprocess.run(['java', 'Main33', input_file.name], capture_output=True, text=True)

    if result.returncode == 0:
        if 'error' in filename:
            if 'fails' in result.stdout:
                results[filename] = "PASSED"
                print(GREEN + "Test passed" + RESET)
                print("Actual output:\n", result.stderr)
            else:
                results[filename] = "FAILED"
                print(RED + "Test failed")
                print("Actual output:\n", result.stdout,result.stderr, RESET)
        else:
            if 'passes' in result.stdout:
                results[filename] = "PASSED"
                print(GREEN + "Test passed" + RESET)
            else:
                results[filename] = "FAILED"
                print(RED + "Test failed")
                print("Actual output:\n", result.stderr, RESET)
    else:
        print("Command failed with return code:", result.returncode)

# Prints each file being tested
for file in files_passing:
    print(file.name + " is being tested...")
    run_passing(file.name)
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