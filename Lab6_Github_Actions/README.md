# Lab 6 - GitHub Actions (Lab 1)

This lab demonstrates CI/CD using GitHub Actions by building a Python calculator, writing tests, and automating test execution on every push.

---

## Project Structure

```
Lab6_Github_Actions/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml       # For structure/documentation consistency
│       └── unittest_action.yml     # For structure/documentation consistency
├── data/
│   └── __init__.py
├── src/
│   ├── __init__.py
│   └── calculator.py               # Core calculator functions
├── test/
│   ├── __init__.py
│   ├── test_pytest.py              # Tests using pytest
│   └── test_unittest.py            # Tests using unittest
├── .gitignore
└── requirements.txt
```

---

## Setup

**1. Create and activate a virtual environment**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Calculator Functions

Defined in `src/calculator.py`:

| Function | Description |
|----------|-------------|
| `add(x, y)` | Returns x + y |
| `subtract(x, y)` | Returns x - y |
| `multiply(x, y)` | Returns x * y |
| `combined(x, y)` | Returns sum of add, subtract, and multiply results |
| `divide(x, y)` | Returns x / y — raises `ValueError` for division by zero |

---

## Run Tests Locally

### Pytest
```bash
pytest test/
```

### Unittest
```bash
python -m unittest test.test_unittest
```

---

## GitHub Actions

Two workflows are configured:
- `Testing with Pytest`
- `Python Unittests`

Actions are triggered on both `push` and `pull_request` events.

Because this project lives inside a larger parent repo, workflow files are stored at the parent repo root:
- `.github/workflows/pytest_action.yml`
- `.github/workflows/unittest_action.yml`

To maintain the Lab6 repository structure, matching workflow YAML files are also kept inside:
- `Lab6_Github_Actions/.github/workflows/pytest_action.yml`
- `Lab6_Github_Actions/.github/workflows/unittest_action.yml`

**Execution note:**
- Parent repo `.github/workflows/` files are used by GitHub Actions to run CI.
- `Lab6_Github_Actions/.github/workflows/` is kept for structure and documentation consistency.
- These workflows are configured to run only for Lab6-related changes.

Both workflows run on a `python:3.8-slim` Docker container, keeping the environment lightweight and consistent.

---

## Additions 

- Added a 5th function `divide()` with proper error handling for division by zero
- Wrote 30+ edge case tests covering floats, negatives, large numbers, and error conditions
- Used `python:3.8-slim` Docker image instead of the default Ubuntu runner for a leaner CI environment
- Workflows trigger on both `push` and `pull_request` events (standard industry practice)
- Used descriptive function names (`add`, `subtract`, etc.) instead of `fun1`, `fun2`

---

## Notes
- Tests must pass locally before pushing
- `.venv/` and `__pycache__/` are excluded via `.gitignore`
- `pytest-report.xml` — downloaded artifact from the GitHub Actions run, confirms pytest executed successfully
- `Both pytest and unittest workflow success.png` — screenshot of both workflows passing in the Actions tab
