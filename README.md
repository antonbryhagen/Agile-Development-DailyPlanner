DailyPlanner
==========================


DailyPlanner is an automatic scheduling application. Using user created activties the application creates a schedule based on the users
needs. 

- [DailyPlanner](#dailyplanner)
  * [Get going](#get-going)
    + [Check version of Python](#check-version-of-python)
    + [Python virtual environment](#python-virtual-environment)
    + [Install the dependencies](#install-the-dependencies)
    + [Run the code](#run-the-code)
    + [Run the validator](#run-the-validator)
- [Run unttests without coverage](#run-unttests-without-coverage)
- [Run unittests with coverage](#run-unittests-with-coverage)
- [Run the linters and the unittests with coverage](#run-the-linters-and-the-unittests-with-coverage)
- [Run a testfile](#run-a-testfile)
- [Run a test method, in a class, in a testfile](#run-a-test-method--in-a-class--in-a-testfile)
- [Remove files generated for tests or caching](#remove-files-generated-for-tests-or-caching)
- [Do also remove all you have installed](#do-also-remove-all-you-have-installed)


Get going
--------------------------

This is how you can work with the development environment.



### Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).



### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

Read more on [Python PIP](https://pypi.org/project/pip/).



### Run the code

Before running the application, make sure you export your PYTHONPATH.
The path used here is the path to the root project folder on your machine
```
# Export PYTHONPATH (using example path)
export PYTHONPATH="C:/ExampleUser/Development/Agile-Development-DailyPlanner"
```

The application also needs a MySQL database in order to work. If it is your first time running the application, please checkout db/SETUP.md to install and setup the database correctly.

The application can be started like this.

```
# Execute the main program
python planner/main.py
```

All code is stored below the directory `planner/`.



### Run the validator

You can run the static code validator like this. It check the sourcecode and exclude the testcode.

```
make pylint


You might need to update the Makefile if you change the name of the source directory currently named `planner/`.

Read more on:

* [pylint](https://pylint.org/)



### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

Read more on:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



### Run parts of the testsuite

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_interface
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_interface.TestInterface.test_display_menu
```



### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```


More targets
--------------------------

The Makefile contains more targets, they are however not yet tested on this directory structure.
