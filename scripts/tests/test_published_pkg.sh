#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"
deactivate 2> /dev/null
rm -rf publish_env
python3 -m venv publish_env
source publish_env/bin/activate
pip install -i https://test.pypi.org/simple/ quickindex==1.1.0
ROOT_DIR=$(git rev-parse --show-toplevel)
TEST_IMPORT_PIP=true python3 "$ROOT_DIR/tests/test.py"