#!/bin/bash
#KingOfMongeese

#USER EDITABLE
#Name of screen socket
SCREEN_NAME="mainworld"

RESTART_SCRIPT="/path/to/start.sh"


backupDir="/path/to/backup/folder"
File1="/path/to/world"

#If you have a paper sever uncomment these and the lines near the bottom
#File2=/path/to/world_nether"
#File3=/path/to/world_the_end"

#Max Backups
MaxBackups=8

WARNING_TIME=300 #300 max about 5 minutes

#End of User Editable
############################################################3

#sends commands to the screen
execute-command () {
  local COMMAND=$1
  screen -S "$SCREEN_NAME" -p 0 -X stuff "$COMMAND$(printf \\r)"
       
  
}

#loop warns players
while [[ $WARNING_TIME -gt 0 ]] 
do 
 
  if [ $WARNING_TIME -eq 300 ]
  then 
    execute-command "msg @a Server will restart in 5 minutes."
  elif [ $WARNING_TIME -eq 240 ] 
  then 
    execute-command "msg @a Server will restart in 4 minutes."
  elif [ $WARNING_TIME -eq 180 ] 
  then 
    execute-command "msg @a Server will restart in 3 minutes."
  elif [ $WARNING_TIME -eq 120 ] 
  then 
    execute-command "msg @a Server will restart in 2 minutes."
  elif [ $WARNING_TIME -eq 60 ] 
  then 
    execute-command "msg @a Server will restart in 1 minute."
  elif [ $WARNING_TIME -eq 30 ] 
  then
    execute-command "msg @a Server will restart in 30 seconds."
  elif [ $WARNING_TIME -eq 10 ] 
  then
    execute-command "msg @a Server will restart in 10 seconds."
  elif [ $WARNING_TIME -eq 5 ] 
  then
    execute-command "msg @a Server will restart in 5 seconds."
  fi
  ((WARNING_TIME--))
  sleep 1
done

#shuts down the server
execute-command "stop"

#giving time for server to shutdown
sleep 60

#number of files in the backup
fileNum=$(ls $backupDir | wc -l)
((fileNum++))

#makes sure max backups is enforced
if [ $fileNum -gt $MaxBackups  ]
then
  oldest="$(ls -1t $backupDir | tail -1)"
  rm -r $backupDir/$oldest
fi

#creates new backup
fname=$(date +%m.%d.%Y)
mkdir $backupDir/$fname

cp -r $File1 $backupDir/$fname

#Uncomment if you have a PAPER server
#cp -r $File2 $backupDir/$fname
#cp -r $File3 $backupDir/$fname



execute-command ${RESTART_SCRIPT}

