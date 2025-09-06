#!/bin/bash
# Bash wrapper for Linux Log Cleaner
# Usage: ./run_cleaner.sh [--dry-run] [--wipe-all] [--target /path/to/file]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="python3"

if ! command -v $PYTHON_BIN &> /dev/null; then
    echo "Error: python3 is not installed."
    exit 1
fi

cd "$SCRIPT_DIR"
$PYTHON_BIN cleaner.py "$@"
