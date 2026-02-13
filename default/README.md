# Math Example Project

This repository contains basic math operations (addition and subtraction) implemented in Python, with automated tests and CI integration.

## Folder Structure

- `src/` : Source code for math operations
- `tests/` : Pytest files for unit testing
- `default/requirements.txt` : Python dependencies
- `default/README.md` : This file
- `default/math.json` : CI workflow metadata

## Usage

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run tests:

```bash
pytest tests/ -v --tb=short
```

## CI/CD

A GitHub Actions workflow will use the metadata in `default/math.json` to generate `.github/workflows/ci.yml` for automated testing on push and pull request.
