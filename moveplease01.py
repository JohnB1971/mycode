#!/usr/bin/env python3

# add functionality with libraries
import shutil
import os

def main():

    # tell where to start the program
    os.chdir('/home/student/mycode/')

    # call to move the file
    shutil.move('raynor.obj', 'ceph_storage/')

    # ask user to rename file program will pause
    xname = input('What is the new name for kerrigan.obj? ')

    # rename the file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main() # end of main function
