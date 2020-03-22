#!/usr/bin/env bash

# build
python3 setup.py sdist bdist_wheel

# config file is under ~/.pipyrc
# username is <__token__>
# password is token created from pypi
# see https://packaging.python.org/guides/using-testpypi/

# upload to pypi test
python3 -m twine upload --skip-existing --repository testpypi dist/*

# clean up when build succeed
rm -rf build/ dist/ *.egg-info/
