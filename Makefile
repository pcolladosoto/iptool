# TODO: Add '__pycache__' to each entry with a Makefile function!
BYTECODE = iptool/__pycache__ iptool/__pycache__
BUILD_DIRS = build dist
TRASH = iptool/iptool.egg-info

pkg:
	python3 setup.py sdist bdist_wheel

.PHONY: clean clean_trash tests

clean: clean_trash

clean_trash:
	rm -rf $(BYTECODE) $(TRASH)

tests:
	python3 -m unittest tests/*.py