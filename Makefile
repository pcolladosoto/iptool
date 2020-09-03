# TODO: Add '__pycache__' to each entry with a Makefile function!
BYTECODE = iptool/__pycache__ tests/__pycache__
BUILD_DIRS = build dist
TRASH = iptool.egg-info
PROG = iptool

# NOTE: Information regarding the building, uploading and downloading of the package has benn taken
# NOTE: form: https://packaging.python.org/tutorials/packaging-projects.

# NOTE: For the following to work we need to run: 'python3 -m pip install --user --upgrade setuptools wheel'
# NOTE: That is, we need to install both 'setuptools' and 'wheel' with pip3.
build:
	python3 setup.py sdist bdist_wheel

.PHONY: clean clean_trash tests upload download local_install uninstall

clean: clean_trash clean_builds clean_builds

clean_trash:
	rm -rf $(BYTECODE) $(TRASH)

clean_builds:
	rm -rf $(BUILD_DIRS)

tests:
	python3 -m unittest tests/*.py

# NOTE: For it to work we need to run 'python3 -m pip install --user --upgrade twine'
# NOTE: That is, we need to install 'twine' with pip3.
# NOTE: We are currently uploading to testpypi so as not to mess with the real index!
# NOTE: Our config lives in ~/.pypirc
upload:
	python3 -m twine upload --repository testpypi dist/*

# NOTE: We are using the test index instead of the real one (take a look at the URL)
# NOTE: We are NOT installing any dependencies. Even though our package has none it's
# NOTE: a good idea to force it so that we don't get funky broken packages.
download:
	pip3 install --index-url https://test.pypi.org/simple/ --no-deps $(PROG)

local_install:
	pip3 install . --upgrade

uninstall:
	pip3 uninstall $(PROG)