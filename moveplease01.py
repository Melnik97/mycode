#!/usr/bin/env python3

#imports shell utilities
import shutil

#imports operating system utilities
import os

#forces program to run in /home/student/mycode which is git controlled
os.chdir('/home/student/mycode/')

#will move rayor.obj into ceph_storage dir. If the file already exists in the Dir it will be overwritten.
shutil.move('raynor.obj', 'ceph_storage/')

#creates varriable from input. Var will be used to change name of File.
xname = input('What is the new name for Kerrigan.obj? \n')

#will use move to copy over Kerrigan and give it the name as speccified by user input
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


