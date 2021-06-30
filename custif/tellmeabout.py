#!/usr/bin/env python3

summary = 'You have chosen '

print("Which series would you like to know more about?\n\n1: Harry Potter\n2: The Lord of the Rings\n3: Chronicales of Narnia\n4: Indiana Jones")

userinput = input("\nPlease type the number of the series listed above: ")

if userinput == 1:
    summary = summary + 'Harry Potter. A series of a boy wizard and his friends saving his magical school from a noseless wizard'
elif userinput == 2:
    summary = summary + 'Lord of the Rings. A series about a group of strangers that set out on a quest to destroy a magical ring and become friends along the way.'
elif userinput == 3:
    summary = summary + 'Chronicales of Narnia. 4 siblings climb it to a magical wardrobe and meet Lion Jesus. They also fight a war against the White witch (cold woman Satan?)'
elif userinput == 4:
    summary = summary + 'Indiana Jones. A series about an Archilogist that travels to romote areas of the world to steal artifacts before other people can steal said atifact. Local population isnt usually happy about it.'
else:
    summary = 'Invalid Input'

print(summary)

