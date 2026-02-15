# Math Operations Example

This repository implements basic math operations (addition and subtraction) in Python.

## Usage

Import functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)  # returns 5
result_subtract = subtract(5, 2)  # returns 3
```

## Testing

Tests are located in the `tests` folder.
Run all tests using:

```bash
pytest tests/
```

## CI Workflow

- Automated tests run on push and pull request to Feature3/main.
- Workflow file: `.github/workflows/ci.yml`

## Requirements

- Python 3.10+
- See `default/requirements.txt` for dependencies.
