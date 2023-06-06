### Description

Fully automated quizzes and tasks, carefully designed in accordance with the great "Python for Everybody" book.

---

### Installation

Update the software.
```
sudo apt update && sudo apt upgrade -y
```

Install [`python`](https://www.python.org/) and [`pip`](https://pip.pypa.io/) (python package manager).
```
sudo apt install python3.11 python3-pip
```

Install [`virtualenv`](https://virtualenv.pypa.io/) (python environments manager).
```
pip3 install virtualenv && source ~/.profile
```

Clone this repository and cd into it.
```
git clone https://github.com/mrguseinov/py4e.git && cd py4e
```

Create a new virtual environment and activate it.
```
virtualenv .venv && source .venv/bin/activate
```

Install the required packages.
```
pip install -r requirements.txt
```

---

### Usage

Activate the virtual environment if it's not active.
```
source .venv/bin/activate
```

Start the jupyter lab.
```
jupyter lab
```

---

### Notes For WSL & SSH Users

*More info in the [Jupyter Notebook Docs](https://jupyter-notebook.readthedocs.io/en/stable/config.html).*

Create a config file:
```
jupyter notebook --generate-config
```

Disable launching browser by redirect file:
```
c.NotebookApp.use_redirect_file = False
```
