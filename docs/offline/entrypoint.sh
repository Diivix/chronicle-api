#!/bin/sh

cd /repos/fastapi/docs/en
mkdocs serve --dev-addr=0.0.0.0:8010 &

cd /repos/sqlmodel
mkdocs serve --dev-addr=0.0.0.0:8020 &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?