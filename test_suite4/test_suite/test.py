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

result = subprocess.run(['javac', 'alanpp.java'], capture_output=True, text=True)

results = {}
def run_passing(filename):
    with open(f'test_suite/test_cases/{filename}', 'rb') as input_file:
        result = subprocess.run(['java', 'alanpp', input_file.name, str(40)], capture_output=True, text=True)
        temp = result.stdout
        with open(f'test_suite/test_cases/temp.alan', 'w') as input_file:
            input_file.write(result.stdout)

        result = subprocess.run(['java', 'alanpp', input_file.name, str(80)], capture_output=True, text=True)
        


    if result.returncode == 0:
        print(filename + '\n' + result.stdout)
        if result.stderr == "":
            results[filename] = "PASSED"
        elif temp != result.stdout:
            results[filename] = "FAILED"
        else:
            results[filename] = "FAILED"
    else:
        results[filename] = "FAILED"
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