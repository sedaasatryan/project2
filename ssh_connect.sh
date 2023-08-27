#!/bin/bash

#Define remote server details
REMOTE_HOST="ip address"
REMOTE_USER="name"

#SSH command to connect to the remote server and execute ipblock.sh
ssh "$REMOTE_USER"@"$REMOTE_HOST" '/path/to/myscript1.sh'
REMOTE_HOST="ip address"
REMOTE_USER="name"
ssh "$REMOTE_USER"@"$REMOTE_HOST" '/path/to/myscript1.sh'
