#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR" || exit
deactivate 2> /dev/null
rm -rf publish_env
python3 -m venv publish_env
# shellcheck disable=SC1091
source publish_env/bin/activate
pip install tomli
ROOT_DIR=$(git rev-parse --show-toplevel)
VERSION=$(python3 "$SCRIPT_DIR/parse_pyproject.py" "$ROOT_DIR/pyproject.toml")
pip install -i https://test.pypi.org/simple/ "quickindex==$VERSION"
TEST_IMPORT_PIP=true python3 "$ROOT_DIR/tests/test.py"
