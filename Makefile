SHELL := /usr/local/bin/fish

run:
	python3 project/main.py

setup:
	pip3 install -r requirements.txt

help:
	@echo "---- HELP ----"
	@echo "1) Create a virtual env"
	@echo "	python3 -m venv hash-code-env"
	@echo "2) Activate your virtual env"
	@echo "	Example: source /hash-code-env/bin/activate.fish"
	@echo "3) Download requirements"
	@echo "	make setup"
	@echo "4) Run program"
	@echo "	python3 project/main.py --help"
	@echo "---- ---- ----"

test:
	python -m unittest discover ./tests -v
