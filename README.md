# Dictionary Brute Force Attack 🕮

## Set up 📦

### Create and enable a virtual environment

```
    $ pip install virtualenv
    $ python -m venv venv
    $ source venv/bin/activate
```

### Install the dependencies

```
    $ pip install -r requirements.txt
```

### If you're a developer, install the git hooks
We're using a lot of github actions for linting, type checking and testing our code. 
Since some of this tests (like the linting and the typing one) are easy to fail, we recommend you to install a [git hook](https://githooks.com/) for executing the same test that will be running on CI but before pushing it to github.

This project comes with [pre-commit](https://pre-commit.com/) support to facilitate the creation of this git hooks. For installing the hooks install the dependencies and run:

```
    $ pre-commit install && pre-commit autoupdate && pre-commit install --hook-type pre-push
```
