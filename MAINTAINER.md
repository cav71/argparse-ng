## Intro

Here you can find detailed instructions on how to manage this project.

Source code is under src/argparse_plus

### Initial setup

TBD -> pre-commit
        * black
        * lint
        * run-tests

### Testing

#### unit test
This will run all the unit tests
```
PYTHONPATH=$(pwd) py.test -vvs tests
```

#### code coverage
This will run all the unit tests and generate the code coverage
```
PYTHONPATH=$(pwd) \
    py.test -vvs tests \
        --cov=argparse_plus \
        --cov-report=html:build/coverage --cov-report=xml:build/coverage.xml \
        --junitxml=build/junit/junit.xml --html=build/junit/junit.html --self-contained-html
```

#### MyPy
```
PYTHONPATH=$(pwd) \
    mypy src/argparse_plus \
        --no-incremental --xslt-html-report build/mypy
```

### Releases

#### master branch
Master branch won't release anything to pypi (or conda-forge), but it
will trigger all the github tests, coverages and code metrics.

#### beta/N.M.O branches
The release process start from the master branch and it will create a "beta" branch (eg. beta/N.M.O):
this branch will run all the github tests, coverages and code metrics as in the master branch, but on success
it will deploy on the pypi server. 

To start on the master branch:
```
    PYTHONPATH=src python -c "import argparse_plus; print(argparse_plus.__version__)"
    N.M.O
```

This will create a new branch beta/N.M.O if no beta/ is present or beta/N.M.(O+1):
```
    ./maintaner/release.py micro src/argparse_plus/__init__.py
```
(you can use the -n|--dry-run flag to run without executing)

Push into origin
```
    git push --set-upstream origin $(git branch --show-current)
```

#### tag a commit with N.M.O
This will close the N.M.O branch and creates a new release.
```
    git tag -m release release/A.B.C
    git push origin release/A.B.C
```

