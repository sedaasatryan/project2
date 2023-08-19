#!/bin/bash

#Define remote server details
REMOTE_HOST="139.144.71.186"
REMOTE_USER="Maria"

#SSH command to connect to the remote server and execute ipblock.sh
ssh "$REMOTE_USER"@"$REMOTE_HOST" '/path/to/myscript1.sh'
REMOTE_HOST="139.144.71.186"
REMOTE_USER="Maria"
ssh "$REMOTE_USER"@"$REMOTE_HOST" '/path/to/myscript1.sh'
