# Development

## Dependencies

* `python3`
* `virtualenv` (optional)
* `virtualenvwrapper` (optional - helps to manage virtualenvs)

## Setup Environment

### (Optional) - Setup `venv` environment

```
export VENV_ROOT=~/.local/venvs # Set to wherever you would like to manage your venvs

python -m venv $VENV_ROOT/silo-idm-a
. $VENV_ROOT/silo-idm-a/bin/activate
```

### (Optional) - Setup `virtualenvwrapper` environment

Refer to setup instructions [here](https://github.com/bernardobarreto/virtualenvwrapper/blob/master/virtualenvwrapper.sh#L31)

```
mkvirtualenv silo-idm-a
workon silo-idm-a
```

### Install requirements

```
pip install -r requirements-dev.txt
pip install -r requirements.txt
```

### Setup and run server

```
cd scripts && ./reset.bash
python app.py # Listening on port 5000
```

## Gotchas

* macOS AirPlay receiver listens on port 5000 by default, ensure that is disabled or use a different port.
