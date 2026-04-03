# Lab 6 - GitHub Actions (Lab 1)

This lab demonstrates CI/CD using GitHub Actions by building a Python calculator, writing tests, and automating test execution on every push.

---

## Project Structure

```
Lab6_Github_Actions/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml       # Runs pytest automatically on push
│       └── unittest_action.yml     # Runs unittest automatically on push
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

## Testing

Tests are written using both **pytest** and **unittest** and cover:
- Positive numbers
- Zeros and one-zero inputs
- Negative numbers and mixed signs
- Floating point values
- Large numbers
- Division by zero (expects `ValueError`)

To run locally:
```bash
# pytest
pytest test/

# unittest
python -m unittest test.test_unittest
```

---

## GitHub Actions

Two workflows trigger automatically on every push or pull request to `main`:

- **`pytest_action.yml`** — runs the pytest suite and uploads an XML test report as an artifact
- **`unittest_action.yml`** — runs the unittest suite and reports pass/fail

Both workflows run on a `python:3.8-slim` Docker container, keeping the environment lightweight and consistent.

---

## Extra work added

- Added a 5th function `divide()` with proper error handling for division by zero
- Wrote 30+ edge case tests covering floats, negatives, large numbers, and error conditions
- Used `python:3.8-slim` Docker image instead of the default Ubuntu runner for a leaner CI environment
- Workflows trigger on both `push` and `pull_request` events (standard industry practice)
- Used descriptive function names (`add`, `subtract`, etc.) instead of `fun1`, `fun2`
