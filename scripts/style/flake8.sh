ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR"
flake8
