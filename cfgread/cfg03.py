#!/usr/bin/env python3
## create file object in "r"ead mode


print("What File would you like to read?")
x=input("")


with open(x, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
for x in configlist:
    print(x.strip())

