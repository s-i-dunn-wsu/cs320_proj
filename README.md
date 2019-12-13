# POFIS
### Python Onboarding For Incoming Students
## Authors
Abdi Vicenciodelmoral, Andrew Cornish, Becca Daniel, Samuel Dunn

# Overview
POFIS is lesson suite for bringing incoming students, transfer or freshmen, up to speed 
with the Python programming language.

# Current Phase
completed phase


# Getting Started
### Python dependencies
POFIS requires python3, as well as a few dependencies.

To install these dependencies the following line is suitable:
```bash
python3 -m pip install -r requirements.txt
```
This may require super-user permissions depending on your environment.

### Source dependencies
If you have cloned this repository, then you will need to initialize some submodules as well.
This can be done like so:
```bash
git submodule init && git submodule update
```

### Launching the site

There is a helper script at the root folder of this project, `qls.py`.
Run this script with an appropriately set up python3 interpreter 
to launch POFIS on port `8080`. 
