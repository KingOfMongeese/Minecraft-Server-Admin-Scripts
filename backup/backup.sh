#!/bin/bash
#KingOfMongeese

#USER EDITABLE
#Name of the screen socket
SCREEN_NAME="mainworld"


#files to backup
backupDir="/path/to/backup_folder"
File1="/path/to/world"

#if you are running a paper server, uncomment these and the comments near the bottom
#File2=/path/to/world_nether"
#File3=/path/to/world_the_end"

#How many backups you want to have
MaxBackups=8

#End of User Editable
############################################################

#sends commands to the screen
execute-command () {
  local COMMAND=$1
  screen -S "$SCREEN_NAME" -p 0 -X stuff "$COMMAND$(printf \\r)"
       
  
}



#saving
execute-command "msg @a starting backup."
execute-command "save-all"

#giving time for server to save
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

#Uncomment these for a PAPER server
#cp -r $File2 $backupDir/$fname
#cp -r $File3 $backupDir/$fname



execute-command "msg @a backup finished."

