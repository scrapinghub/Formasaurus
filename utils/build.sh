#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SUPPORTED_SKL_VERSIONS="$(cat $SCRIPT_DIR/SKL_VERSIONS.txt)"

for SKL_VERSION in $SUPPORTED_SKL_VERSIONS
do
    rm -rf "$SCRIPT_DIR/.venv" &> /dev/null
    python3 -m venv "$SCRIPT_DIR/_venv"
    . "$SCRIPT_DIR/_venv/bin/activate"
    pip install scikit-learn==$SKL_VERSION
    pip install .[with-deps]
    python3 "$SCRIPT_DIR/_build.py"
    deactivate
    rm -rf "$SCRIPT_DIR/.venv" &> /dev/null
done
