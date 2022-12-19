# Reproduce `pylint` PEP420 `cyclic-import` false-positive

```sh
python3.11 -m venv venv
./venv/bin/python -m pip install -r requirements.txt
./venv/bin/pylint $(find src -name '*.py')
```

and

```sh
python3.11 -m venv venv
./venv/bin/python -m pip install -r requirements.txt
./venv/bin/pylint --recursive=y src
```

produces

```
************* Module logging.wrapper.__init__
src/some/package/logging/wrapper/__init__.py:1:0: R0401: Cyclic import (logging -> logging.wrapper) (cyclic-import)
```

while

```sh
./venv/bin/pylint src
```

would work yet linting individual file would not be possible.
