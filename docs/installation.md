# Installation

!!! warning "Note:"
    Only Python Version 3.7 and above are supported!

!!! tip
    You can check your Python Version using:
    `sh python --version `
    </br>
    **If it's lower than 3.7:**</br></br>
    [Download Python](https://python.org/downloads){: .md-button}

## Using Pip

To install using pip:

```sh
pip install pip setuptools wheel --upgrade
pip install proxygrab --upgrade
```

## Using Source Code

### Download the latest source code from Github

[Click here](https://github.com/Divkix/ProxyGrab/archive/master.zip) to download the latest source code from Github

### Using Git

```sh
git clone https://github.com/Divkix/ProxyGrab.git
```

Make sure you have poetry installed

```sh
pip install --upgrade poetry
```

After you have downloaded the source code, `cd` (by doing `cd ProxyGrab`) into the the directory and type this command:</br>

```sh
poetry install
```

Wait a few seconds and it should be installed!

You can now run it using:

```sh
poetry run proxygrab <options>
```

## Setting up local docs

Local Docs can be setup by getting the latest source code and then using these commands:

```sh
make docs
```

The docs would be ready in a folder called `site`, from there you can access them by opening `index.html` file.
