#!/bin/bash

CLEARML_ARCHIVE=$(source ./server_sh_vars.sh; echo $CLEARML_ARCHIVE)
# echo $CLEARML_ARCHIVE/archive_$(date +"%Y%m%d_%H%M").tar

sudo tar --wildcards -cvf $CLEARML_ARCHIVE/archive_$(date +"%Y%m%d_%H%M").tar /opt/clearml


