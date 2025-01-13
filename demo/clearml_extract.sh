#!/bin/bash

CLEARML_ARCHIVE=$(source ./server_sh_vars.sh; echo $CLEARML_ARCHIVE)

ls $CLEARML_ARCHIVE | tail -n 10

while true; do
	read -p "Which archive do you want to restore?" archive_name
	if [[ -f $CLEARML_ARCHIVE/$archive_name ]]; then
    	break;
	else
    	echo "$CLEARML_ARCHIVE/$archive_name is not a file";
	fi
done

# echo 'Okay'
sudo tar -xvf $CLEARML_ARCHIVE/$archive_name --transform 's!opt/!!' -C /opt