.PHONY: run test

run:
	/opt/homebrew/bin/python3.11 src/main.py

test:
	/opt/homebrew/bin/python3.11 -m unittest discover tests