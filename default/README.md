# Math Operations Example

This repository demonstrates basic math operations (addition and subtraction) with Python functions and comprehensive pytest-based testing.

## Usage

- Functions are in `src/math_operations.py`.
- Tests are in the `tests/` folder.

## Run Tests

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
   ```

## CI Workflow

- All tests are executed via GitHub Actions (`.github/workflows/ci.yml`).
- Reports are generated in `reports/`.

## Structure

- `src/math_operations.py` - Business logic
- `tests/test_add.py` - Addition tests
- `tests/test_subtract.py` - Subtraction tests
- `default/requirements.txt` - Python dependencies
- `default/math.json` - CI/CD metadata
