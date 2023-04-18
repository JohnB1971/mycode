#!/usr/bin/env python3

# the following lines will create the directory if it does not already exist.  
# code to complete the task
import shutil 
import os

# move into the working directory
os.chdir("/home/student/mycode")

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")


