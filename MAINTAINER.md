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
This will trigger guthub normal build including unit testing

#### beta/N.M.O branches

Start a new beta branch:
```
git push origin $(./maintaner/release.py micro argparse_plus)
```

#### tag a commit with N.M.O
this will close the N.M.O branch and creates a release.
```
git tag -m release release/A.B.C
```

