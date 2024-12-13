#! /usr/bin/env bash
set -uvx
set -e
cp -rp ~/.pypirc $USERPROFILE/
pip install --user --upgrade pip
pip install twine
twine upload dist/*
