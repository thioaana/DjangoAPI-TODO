install:
		# Install dependencies
		pip install --upgrade pip && pip install -r requirements.txt

format:
		# Format *.py
		black config/*.py todos/*.py

test:
		# Testing *.py

all:
		install