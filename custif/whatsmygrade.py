#!/usr/bin/env python3

message = 'Your letter grade is '


numbergrade = float(input("What number grade did you earn? "))

if numbergrade >= 93:
    message = message + 'an A'
elif numbergrade >= 85:
    message =  message + 'a B'
elif numbergrade >= 77:
    message = message + 'a C'
elif numbergrade >= 70:
    message = message + 'a D'
else:
    message = message + 'an F'

print(message)

