#!/bin/bash
#KingOfMongeese

echo "autosave called"
#USER EDITABLE
#Put the name of your screen socket here
SCREEN_NAME="mainworld"



#END OF USER EDITABLE
############################################################

#sends commands to the screen
execute-command () {
  local COMMAND=$1
  screen -S "$SCREEN_NAME" -p 0 -X stuff "$COMMAND$(printf \\r)"
       
  
}


echo "Starting autosave"
#saving
execute-command "msg @a autosaving."
execute-command "save-all"

#giving time for server to save
sleep 30


execute-command "msg @a autosave complete."
echo "autosave completed successfully"
