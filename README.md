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

## Run 🗲

### Run the brute force without caching 
For running the brute force algorithm, execute:

```
    $ python brute_force.py
```

### Run the brute force with caching
If you want to test the improvement that we could achieve if we had a dictionary with the keys already generated (so we don't need to run the hash function for calculating the key from the passphrase), follow this steps.

#### Create the key cache file
Save the result of the hash function for every passphrase of the dictionary to the data/cached_passwords.txt file with:

```
    $ python cache_passwords.py
```

Then, run the script that uses this cached keys for decrypting the message:

```
    $ python brute_force_cached.py
```

## Results 📉
In my laptop (i5-8265U, with 16GBytes of RAM and kernel 5.15.78) the benchmarks show a 40% improvement when we run the script brute_force_cached.py instead of brute_force.py.
