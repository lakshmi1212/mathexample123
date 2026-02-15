# Math Operations Example

## Overview
This project provides simple functions for addition and subtraction, with comprehensive pytest test coverage and CI/CD integration readiness.

## Folder Structure
- `src/` : Source code for math operations
- `tests/` : Pytest test files
- `default/requirements.txt` : Python dependencies
- `default/README.md` : This file
- `default/math.json` : CI workflow meta-data

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests

1. Install dependencies:
   ```
   pip install -r default/requirements.txt
   ```

2. Run all tests:
   ```
   pytest tests/
   ```

## CI/CD
Workflow file should be located at `.github/workflows/ci.yml`. See `default/math.json` for workflow meta-data.
