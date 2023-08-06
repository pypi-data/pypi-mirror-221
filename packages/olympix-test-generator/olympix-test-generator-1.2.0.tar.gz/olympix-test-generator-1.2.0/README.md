# Olympix Test Generator

Olympix Test Generator is a Python package designed to assist with the generation of unit tests for Solidity smart contracts. These unit tests are specifically designed to be ran through [Foundry](https://book.getfoundry.sh/), a tool for writing unit tests in Solidity. 

## Installation

You can install Olympix Test Generator using pip:

```bash
pip install olympix-test-generator
```

## Usage

The package includes a command-line interface for generating tests.

Before running the script, make sure to set the `OLYMPIX_API_KEY` environment variable in your system.

To generate a test, run:

```bash
olympix generate
```

The tool will guide you through the process of generating the test. 

A test contract will be written in the same directory as the selected smart contract, or in a neighboring test folder if it exists. No existing files will be overwritten. The tests are also outputted to the console. 

## Project Structure

The project includes the following Python files:

- `client.py`: The main script for interacting with the Olympix DevSecTools API. It includes an interactive command-line interface.

## Dependencies

This project's dependencies are specified in the `requirements.txt` file.