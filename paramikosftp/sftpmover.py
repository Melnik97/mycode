#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

A= input('Please enter IP Adress of matchine:  ')
B= input('Please enter Username: ')
C= input('please enter Password: ')
D= input('Please enter Location to copy to: ')
## where to connect to
t = paramiko.Transport(A , 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username= B, password= C)

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, ___ +x) # move file to target location

## close the connection
sftp.close() # close the connection

#need to figure out how to make Var D fit into underscores. Default location was "/tmp/"

