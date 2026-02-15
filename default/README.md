# Math Operations Example

This repository demonstrates basic math operations (addition and subtraction) with production-ready Python code, automated testing, and CI/CD integration.

## Usage

Import and use the math operations:

```python
from src.math_operations import add, subtract

result1 = add(2, 3)        # 5
result2 = subtract(5, 2)   # 3
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests:

```bash
pytest tests/
```

## CI/CD Workflow

- Automated tests run on push and pull requests.
- Workflow file: `.github/workflows/ci.yml`
- Test reports generated in `reports/` directory.

See `default/math.json` for workflow metadata.
