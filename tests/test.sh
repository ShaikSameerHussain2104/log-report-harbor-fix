#!/bin/sh
set -eu

mkdir -p /logs/verifier

set +e
pytest \
  /tests/test_outputs.py \
  --ctrf /logs/verifier/ctrf.json
pytest_exit_code=$?
set -e

if [ "$pytest_exit_code" -eq 0 ]; then
    echo "1" > /logs/verifier/reward.txt
else
    echo "0" > /logs/verifier/reward.txt
fi

exit "$pytest_exit_code"