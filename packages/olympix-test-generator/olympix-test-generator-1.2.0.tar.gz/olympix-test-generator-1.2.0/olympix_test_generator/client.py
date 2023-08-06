import requests
import argparse
import os
from dotenv import load_dotenv
import inquirer

BASE_URL = 'https://generate-sol-tests.olympixdevsectools.com' 
#BASE_URL = 'http://127.0.0.1:8000'

# Declare global variables
file_content = ""
contract_name = ""
function_name = ""
opix_api_key = ""
source_file_path = ""

def get_opix_api_key() -> bool:
    global opix_api_key  # Use global variable

    opix_api_key = os.getenv('OLYMPIX_API_KEY')
    if opix_api_key is None:
        print("'OLYMPIX_API_KEY' not found.")
        return False
    else:
        select_sol_file()
        return True

def select_sol_file():
    global file_content, contract_name, function_name, source_file_path  # Use global variables

    # Get a list of all .sol files and directories in the current directory, but don't include .t.sol files
    files_and_dirs = [f for f in os.listdir('.') if os.path.isdir(f) or (os.path.isfile(f) and f.endswith('.sol') and not f.endswith('.t.sol'))]
    files_and_dirs.append('..')  # Add option to go up one directory

    # Define the questions
    questions = [
        inquirer.List('file',
                      message="Select a .sol file or a directory",
                      choices=files_and_dirs,
                      ),
    ]

    # Get the user's answer
    answers = inquirer.prompt(questions)

    # If a directory is selected, change the current directory and call this function again
    if os.path.isdir(answers['file']):
        os.chdir(answers['file'])
        select_sol_file()
    elif answers['file'] == '..':
        os.chdir('..')
        select_sol_file()
    else:
        # Print the selected file
        print(f"You selected {answers['file']}")
        with open(answers['file'], 'r') as f:
            file_content = f.read()
        source_file_path = os.path.dirname(os.path.abspath(answers['file']))  # Get the directory of the source file

def get_contract_and_function_name(outline):
    global contract_name, function_name  # Use global variables

    # Get a list of all contracts
    contracts = outline.keys()
    if len(contracts) == 0:
        print("No contracts found in the file")
        return False
    
    if len(contracts) == 1:
        contract_name = list(contracts)[0]
        functions = outline[contract_name]
    else:
        # Define the questions
        questions = [
            inquirer.List('contract',
                        message="Select a contract",
                        choices=contracts,
                        ),
        ]

        # Get the user's answer
        answers = inquirer.prompt(questions)
        contract_name = answers['contract']

        # Get the functions for the selected contract
        functions = outline[answers['contract']]
    
    if len(functions) == 0:
        print("No functions found in the contract")
        return False

    # Define the questions
    questions = [
        inquirer.List('function',
                      message="Select a function for best results, or test an entire contract",
                      choices=functions,
                      ),
    ]

    # Get the user's answer
    answers = inquirer.prompt(questions)
    function_name = answers['function']
    if function_name == "Entire Contract":
        function_name = ""
    return True

def main():
    global function_name, file_content  # Use global variables
    parser = argparse.ArgumentParser(description='Generate a test contract for a given smart contract')
    subparsers = parser.add_subparsers(dest='command')

    # add commands
    generate_parser = subparsers.add_parser('generate')

    args = parser.parse_args()

    if args.command == 'generate':
        found_key = get_opix_api_key()
        if not found_key:
            return
        
        # Now, it gets the contract outline
        print("Fetching contract outline...")
        headers = {
            'Authorization': f'Bearer {opix_api_key}'
        }

        data = {
            'file_content': file_content, 
            }
        response = requests.post(f'{BASE_URL}/outline', headers=headers, json=data)
        outline = response.json()['outline']
        if not outline:
            print("Issues reading contract. ")
            return

        # Now, get the contract name and function name
        valid = get_contract_and_function_name(outline)
        if not valid:
            return
        
        print(f"Generating a test contract for {function_name} in {contract_name}. \nThis may take a few seconds ...")
        headers = {
            'Authorization': f'Bearer {opix_api_key}'
        }

        data = {
            'file_content': file_content, 
            'contract_name': contract_name, 
            'function_name': function_name
            }

        response = requests.post(f'{BASE_URL}/generate', headers=headers, json=data)
        test_content = response.json()['test']
        print("#----------------------------------------#")
        print(test_content)
        print("#----------------------------------------#")

        # Check if a "test" directory exists at the same level as the source file
        parent_dir_path = os.path.dirname(source_file_path)
        test_dir_path = os.path.join(parent_dir_path, 'test')
        if os.path.exists(test_dir_path):
            output_dir_path = test_dir_path
        else:
            output_dir_path = source_file_path

        # capitalize the first letter of the function name
        if len(function_name) > 0:
            function_name_list = list(function_name)
            function_name_list[0] = function_name_list[0].upper()
            function_name = ''.join(function_name_list)
        test_contract_name = f'{contract_name}{function_name}'

        # Write the response to a file in the same directory as the source file
        if not os.path.exists(os.path.join(output_dir_path, f'{test_contract_name}.t.sol')):
            with open(os.path.join(output_dir_path, f'{test_contract_name}.t.sol'), 'w') as f:
                f.write(test_content)
        else:
            counter = 2
            while os.path.exists(os.path.join(output_dir_path, f'{test_contract_name}{counter}.t.sol')):
                counter += 1
            with open(os.path.join(output_dir_path, f'{test_contract_name}{counter}.t.sol'), 'w') as f:
                f.write(test_content)
        
        print(f"Test contract saved to {output_dir_path}")

if __name__ == "__main__":
    main()
