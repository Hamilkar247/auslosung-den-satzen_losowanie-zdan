#!/bin/bash
REAL="$(dirname "$(realpath "$0")")"
echo "$REAL"
PATH="$REAL"/venv/bin:"$PATH"
python "$REAL"/auslosung-den-satzen_losowanie-zdan.py "$@"
echo "python \"$REAL\"/auslosung-den-satzen_losowanie-zdan.py \"$@\" "

