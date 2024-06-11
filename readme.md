# Pylint-Pytest-Unittest

 This repo covers Pylint-driven code refinement, Kaprekar routine implementation with unit tests, Lucas sequence evaluation, palindrome day detection using Pytest, and student score analysis with Pytest

## Directory Structure

```plaintext
.
├── Kaooa_Pylint
│   ├── code
│   │   ├── Kaooa1.py
│   │   ├── Kaooa2.py
│   │   ├── Kaooa3.py
│   │   ├── Kaooa4.py
│   │   ├── Kaooa5.py
│   │   ├── Kaooa6.py
│   │   └── KaooaFinal.py
│   ├── lint
│   │   ├── lint_1.txt
│   │   ├── lint_2.txt
│   │   ├── lint_3.txt
│   │   ├── lint_4.txt
│   │   ├── lint_5.txt
│   │   ├── lint_6.txt
│   │   └── lint_7.txt
│   ├── Original
│   │   └── Kaooa_original.py
│   └── readme.md
├── Kaprekarroutine_unittest
│   ├── code
│   │   └── kaprekarroutine.py
│   ├── readme.md
│   └── testcases
│       └── test.py
├── Lucas_pylint
│   ├── code
│   │   ├── Lucas1.py
│   │   ├── Lucas2.py
│   │   ├── Lucas_3.py
│   │   ├── Lucas_4.py
│   │   └── Lucas_5.py
│   ├── lint
│   │   ├── lint1.txt
│   │   ├── lint2.txt
│   │   ├── lint3.txt
│   │   ├── lint4.txt
│   │   └── lint5.txt
│   └── readme.md
├── Palindrome_day_Pytest
│   ├── code
│   │   ├── palindromeDay.py
│   ├── readme.md
│   └── testcases
│       └── test.py
├── Questions
│   └── ProblemStatements.pdf
└── Score_analyzer_Pytest
    ├── code
    │   └── scoreAnalyzer.py
    ├── readme.md
    └── testcases
        └── test.py
```
## Kaooa_Pylint

It demonstrates the use of Pylint to iteratively improve the code quality. The lint results for each iteration are stored in the lint directory.

### Kaooa Pylint Scores

The code was iteratively improved to achieve a better Pylint score. Here are the results of the iterations:

- Initial score: 0.00/10
- After first iteration: 0.55/10
- After second iteration: 3.21/10
- After third iteration: 3.74/10
- After fourth iteration: 4.24/10
- After fifth iteration: 9.20/10
- Final score: 9.35/10

### Running Pylint

To run Pylint on the code files:

```bash
pylint code/*.py

```

## Kaprekarroutine_unittest

It includes a script for the Kaprekar routine and its corresponding unittests.

### Running Unittests

To run the unittests:

```bash
python -m unittest testcases/test.py

```

## Lucas_pylint

It demonstrates the use of Pylint for the Lucas sequence calculations.

### Lucas Pylint Scores

Here are the Pylint scores for the Lucas modules:

- [Lucas1.py](http://lucas1.py/): 6.43/10
- [Lucas2.py](http://lucas2.py/): 7.14/10
- Lucas_3.py: 7.14/10
- Lucas_4.py: 9.29/10
- Final score: 10.00/10

### Running Pylint

To run Pylint on the code files:

```bash
pylint code/*.py

```

## Palindrome_day_Pytest

It includes a script for checking palindrome days and its corresponding pytest test cases.

### Running Pytest


To run the pytest tests:

```bash
pytest testcases/test.py

```

## Score_analyzer_Pytest

It includes a script for analyzing student scores and its corresponding pytest test cases.

### Running Pytest

To run the pytest tests:

```bash
pytest testcases/test.py

```

# Usage Instructions

Clone the repository:

```bash
git clone <https://github.com/yourusername/project-repo.git>
cd project-repo

```

Navigate to the desired project directory:

```bash
cd Kaooa_Pylint  # Example

```

Run Pylint or tests as required:

```bash
pylint code/*.py  # For Pylint
python -m unittest testcases/test.py  # For unittests
pytest testcases/test.py  # For pytest

```

# Additional Information

Ensure you have the required Python version and dependencies installed.

- For Pylint, make sure to have Pylint installed: `pip install pylint`.
- For unittests and pytest, ensure you have pytest installed: `pip install pytest`.
- Feel free to explore each project directory for more details and specific instructions.

