#!/usr/bin/python3

# look at file keystone.common.wsgi and total failed login attempts.

# count fails
loginfail = 0

# open file for reading
keystone_file=open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()

# loop over the list of lines
for line in keystone_file_lines:
    #if this appears in the line it fails
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed log in attmepts is", loginfail)

#close the file
keystone_file.close()

