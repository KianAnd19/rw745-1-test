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


folder_path = Path('test_suite/draco-pinpoint/passing/')
files_passing = [item for item in folder_path.iterdir() if item.is_file()]
files_passing.sort()

folder_path = Path('test_suite/draco-pinpoint/failing/')
files_failing = [item for item in folder_path.iterdir() if item.is_file()]
files_failing.sort()
results = {}

def run_passing(filename):
    input_file = f'./test_suite/draco-pinpoint/passing/{filename}'
    result = subprocess.run(['java', 'Draco', input_file], capture_output=True, text=True)

    if result.returncode == 0:
        if 'Passes' in result.stdout:
            results[filename] = "PASSED"
            print(GREEN + "Test passed" + RESET)
        else:
            results[filename] = "FAILED"
            print(RED + "Test failed")
            print("Actual output:\n", result.stderr, RESET)
    else:
        results[filename] = "FAILED"
        print(RED + "Test failed")
        print("Command failed with return code:", result.returncode)

def run_failing(filename):
    input_file = f'./test_suite/draco-pinpoint/failing/{filename}'

    result = subprocess.run(['java', 'Draco', input_file], capture_output=True, text=True)

    if result.returncode == 0:
        if 'Fails' in result.stdout:
            results[filename] = "PASSED"
            print(GREEN + "Test passed" + RESET)
        else:
            results[filename] = "FAILED"
            print(RED + "Test failed")
            print("Actual output:\n", result.stderr, RESET)
    else:
        results[filename] = "PASSED"
        print(GREEN + "Test passed" + RESET)
        # print("Command failed with return code:", result.returncode)

# Prints each file being tested
for file in files_passing:
    print(file.name + " is being tested... (passing)")
    run_passing(f'{file.name}')
    print("--------------------------------")

for file in files_failing:
    print(file.name + " is being tested... (failing)")
    run_failing(file.name)
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