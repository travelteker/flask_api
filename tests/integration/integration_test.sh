#!/bin/bash

export ROBOT_OPTIONS="--debugfile plytix_integration.log --logtitle 'Plytix Integration Api Words' -P . --variable variables/integration.yml -d /mnt/c/ProyectosPython/flask/factory_method/tests/integration/results"
export ROBOT_SYSLOG_FILE=DEBUG

robot /mnt/c/ProyectosPython/flask/factory_method/tests/integration/plytix.robot



