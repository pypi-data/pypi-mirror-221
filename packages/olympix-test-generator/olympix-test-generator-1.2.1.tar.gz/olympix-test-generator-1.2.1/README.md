# Olympix Test Generator

Olympix Test Generator is a Python-based utility tool to streamline the process of generating unit tests for Solidity smart contracts. These unit tests are tailored to be compatible with [Foundry](https://book.getfoundry.sh/), a specialized tool for writing unit tests in Solidity.

## Prerequisites

- Python 3.7 or later
- Solidity 0.8.0 or later

## Installation

Install the Olympix Test Generator through pip:

```bash
pip install olympix-test-generator
```

## Configuration

Prior to running the script, you'll need to set the `OLYMPIX_API_KEY` environment variable in your system.

For Unix or Linux:

```bash
export OLYMPIX_API_KEY=your-api-key
```

For Windows:

```cmd
setx OLYMPIX_API_KEY "your-api-key"
```

## Usage

Olympix Test Generator offers a command-line interface for creating tests.

Initiate the test generation process with:

```bash
olympix generate
```

Upon executing the command, the tool will guide you through the steps required to generate the test. 

A test contract will be created either in the same directory as the chosen smart contract, or in an adjacent test folder, should one exist. Existing files will remain unaffected. The generated tests are also displayed on the console. 

For optimal results, generate tests for one function at a time. 