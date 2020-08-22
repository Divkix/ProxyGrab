# Installation

!!! warning "Note:"
    Only Python Version 3.6 and above: is supported!

!!! tip
    You can check your Python Version using:
    ```sh
    python --version
    ```
	</br>
    **If it's lower than 3.6:**</br></br>
    [Download Python](https://python.org/downloads){: .md-button}

## Using Pip

To install using pip:

<div class="termy">
```console
$ pip install proxygrab --upgrade
---> 100%
```
</div>

## Using Source Code

### Download the latest source code from Github

[Click here](https://github.com/SkuzzyxD/ProxyGrab/archive/master.zip) to download the latest source code from Github

### Using Git

```sh
git clone https://github.com/SkuzzyxD/ProxyGrab.git
```

After you have downloaded the source code, `cd` (by doing `cd proxygrab`) into the the directory and type this command:</br>
```sh
python setup.py install
```

Wait a few seconds and it should be installed!

## Setting up local docs
Local docs can be setup by getting the latest source code and then using these commands:

```sh
pip install -r requirements.txt
mkdocs build
```

The docs would be ready in a folder called `site`, from there you can access them by clicking on `index.html`.
