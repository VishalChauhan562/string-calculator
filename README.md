# String Calculator TDD Kata

A Test-Driven Development implementation of a String Calculator that handles various input formats and edge cases.

## Features

- Empty string returns 0
- Single number returns that number
- Two or more numbers returns their sum
- Handles newlines as delimiters
- Supports custom delimiters
- Throws exception for negative numbers
- Ignores numbers greater than 1000
- Supports delimiters of any length

## Project Structure

```
string-calculator/
├── README.md
├── calculator/
│   ├── __init__.py
│   └── string_calculator.py
└── tests/
    ├── __init__.py
    └── test_string_calculator.py
```

## Requirements

- Python 3.10 or higher
- pytest 8.3 or higher

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd string-calculator
```

2. Create and activate a virtual environment (recommended):
```bash
# For Unix/macOS
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pytest
```

## Running Tests

Run all tests:
```bash
pytest tests/
```

Run tests with verbose output:
```bash
pytest -v tests/
```

## Test Cases

The project includes the following test cases:

1. `test_empty_string_returns_zero`: Empty string returns 0
2. `test_single_number_returns_that_number`: Single number returns the same number
3. `test_two_numbers_returns_their_sum`: Two comma-separated numbers return their sum
4. `test_multiple_numbers_returns_their_sum`: Multiple numbers return their sum
5. `test_newlines_between_numbers`: Handles newlines between numbers
6. `test_support_different_delimiter`: Supports custom delimiter format "//[delimiter]\n"
7. `test_negative_numbers_throw_exception`: Throws exception for negative numbers
8. `test_numbers_bigger_than_1000_are_ignored`: Numbers > 1000 are ignored
9. `test_delimiter_of_any_length`: Supports delimiters of any length

## Usage Examples

```python
from calculator.string_calculator import add

# Basic usage
add("1,2,3")  # Returns 6

# Using newlines
add("1\n2,3")  # Returns 6

# Custom delimiter
add("//;\n1;2")  # Returns 3

# Custom delimiter with multiple characters
add("//[***]\n1***2***3")  # Returns 6

# Numbers > 1000 are ignored
add("2,1001")  # Returns 2

# Negative numbers throw exception
add("1,-2")  # Raises ValueError: "negatives not allowed: -2"
```

## Development Process

This project was developed following strict TDD principles:
1. Write a failing test
2. Write the minimum code to make the test pass
3. Refactor if needed
4. Repeat

Each commit in the repository represents one cycle of this process.