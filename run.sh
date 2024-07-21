#!/bin/bash

# path to java exec
JAVA="/usr/lib/jvm/java-17-openjdk-amd64/bin/java"

#path to server jar
JAR=""

#ram example 10G
RAM=""

# garbage collection optimization
FLAGS="-XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableE>
echo "Starting server..."
${JAVA} -Xmx${RAM} -Xms${RAM} ${FLAGS} -jar ${JAR} --nogui
