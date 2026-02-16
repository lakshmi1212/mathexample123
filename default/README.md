# Math Operations Example

This repository provides simple math operations (`add` and `subtract`) with corresponding tests.

## Usage

Import and use the math operations:

```python
from src.math_operations import add, subtract
print(add(2, 3))        # 5
print(subtract(5, 3))   # 2
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests using pytest:

```bash
pytest tests/
```

## CI/CD

This repository is intended for integration with GitHub Actions workflows for continuous integration.
See `.github/workflows/ci.yml` for the pipeline configuration (to be generated).
