#!/usr/bin/python
#Filename:backup_ver2.py
import os
import time
#1.The files and directories to be backed up are specified in a list.
source = [r'C:\Users\apple\Documents\C++PrimePlus\chapter2_2.7',r'C:\Users\apple\Documents\C++PrimePlus\chapter3_3.7']
#2.The back up must be stored in a main backup directory
target_dir = r'C:\Users\apple\Documents\pybackup\backup'
#3.The files are backed up into a zip file
#4.The name of the zip archive is the current date and time
today = target_dir + time.strftime('%Y%m%d')
#The current time is the name of a zip file
now = time.strftime('%H%M%S')
#Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)#make directory
    print'Successfully created directory',today
#The name of the zip file
target = today + os.sep + now + '.zip'
#5.We use the zip command to put the files in a zip archive
zip_command = "zip -qr %s %s"%(target,' '.join(source))
print zip_command
#Run the backup
if os.system(zip_command) == 0:
    print'Successful backed up to',target
else:
    print'Backup FAILED'
