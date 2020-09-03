# TODO: Add '__pycache__' to each entry with a Makefile function!
BYTECODE = iptool/__pycache__ tests/__pycache__
BUILD_DIRS = build dist
TRASH = iptool.egg-info

pkg:
	python3 setup.py sdist bdist_wheel

.PHONY: clean clean_trash tests

clean: clean_trash clean_builds clean_builds

clean_trash:
	rm -rf $(BYTECODE) $(TRASH)

clean_builds:
	rm -rf $(BUILD_DIRS)

tests:
	python3 -m unittest tests/*.py