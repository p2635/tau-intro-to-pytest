# Introduction to pytest

<img src="https://github.com/p2635/tau-intro-to-pytest/raw/main/certificate.png" width="450">

- This documents my learning on the course from Test Automation University: https://testautomationu.applitools.com/pytest-tutorial/.
- Date completed: 8 November 2022.
- Time spent: ~5 hours
- The work is handcoded by yours truly (except for example code that were copied and pasted).

# Environment

- MacOS Ventura 13.0
- Atom
- Terminal
- Python 3.9.13
- pytest 7.2.0

# Directory

- `/stuff` and `/tests` are project files (yes, you read it right. It says 'stuff', not sure why the tutor told me to use that :rofl:)
- `/output` stores terminal output for the tests I ran.
- `/quiz` stores the quiz answers that I submitted.

# Chapter 1 - The first test case

- Simple setup, installed pytest through pip and created a python file to run.

# Chapter 2 - Failed test case

- Assertion introspection is seems useful, saves you a few secs going into the code to see what's wrong. Failure introspection should be part of our daily life as well (I jest).

# Chapter 3 - Asserting exceptions

- I got the first question wrong. I answered 'To catch exceptions raised by the pytest framework.' but I think the answer is 'To verify that the code under test raises expected exceptions.'. After resubmitting, everything came back correct!

# Chapter 4 - Parameterized tests

- TIL an underscore prefix means that the variable is private. For example, _count denotes a private var for the count variable.
- Class properties are objects you can usually 'Get' and 'Set'.

# Chapter 5 - Testing classes

- I learned about Arrange, Act and Assert. This can confuse me because I previously learned the cybersecurity AAA which has a different meaning.

# Chapter 6 - Fixtures

- Fixtures handle the test setup (Arrange step) by injecting objects as required dependencies for the test functions. Improves readability and maintainability of tests.
- The `yield` keyword enables test setup and cleanup, it's like the act of drawing a line in the sand. Anything before the keyword is setup and after the keyword is cleanup.
- Fixtures can be placed in `conftest.py` within the /tests folder. This allows multiple modules to use the same fixture.

# Chapter 7 - Commands and Configs

- `--verbose` and `--quiet` controls terminal output.
- `--exitfirst` stops the test after the first failure. pytest usually continues tests by default regardless of test failures.
- `--maxfail=(number)` limits number of failures before stopping.
- There is a `pytest.ini` file for specifying pytest configs.
  - `addopts` specify options that you would otherwise type out in the command line.

# Chapter 8 - Filtering tests

- You can run tests in a certain folder, individual modules, or even specific functions in a module. By default, pytest runs tests that it can find in the pwd.
- You can even run tests with a substring in it with the `-k` option, wow! (UPDATE: You can also use and, or, and not).
- `@pytest.mark.(name)` decorator is another option if you want to run a custom list of tests. They work like tags. However, these markers need to be defined in the `pytest.ini` as well.
  - Tried this with my first test case. I marked as 'fave' and was able to run just that test case with the `-m` option.

# Chapter 10 - Useful plugins

- pytest-html for prettier reports.
- pytest-cov for check code coverage statistics, this also can be outputted as html.
- pytest-xdist allows parallel execution of tests. I guess 'xdist' means distributed execution.
