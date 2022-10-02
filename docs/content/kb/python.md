+++
title = "Python"
+++

> Note: Configuration from this KB can be applied through [this](https://github.com/Mamut3D/mamut3d.github.io/blob/main/ansible/playbooks/personal_config.yml) Ansible playbook.

## Python shell autocomplete

Taken from [here](https://stackoverflow.com/questions/246725/how-do-i-add-tab-completion-to-the-python-shell).

```console
$ cat ~/.pythonrc

# ~/.pythonrc
# enable syntax completion
try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")
```

## Python IDE

Long story short, lets go VIM + terminal ;-). Vim plugin jedi-vim for python autocomplete installation can be found [here]({{< ref "/kb/vim#python-autocomplete" >}} "Vim").

## Python debugger pdb

To start pdb use either:

- `breakpoint()` - directly in the code and then just run it `./xyz.py`
- `python -m pdb xyz.py` - run python script in debugger

### pdb commands

```console
# view all variable names
dir()

# Pretty print variable content
pp <variable>

# Print variable content
p <variable>

# Print the source code around current line
l

# Print the source code around until current line
ll

# Step - execute current line
s

# Continue program execution
c

# Execute until return from current func
r

# Quit
q

```

## Simple web server

```bash
python -m http.server 8080
```
