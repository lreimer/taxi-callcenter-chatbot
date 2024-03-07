# Variables
PYTHON = python
PIP = pip

# Targets
install:
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m pytest *_test.py
