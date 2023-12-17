#string data type

#literal assignment
first = "Debela"
last = "Tesfaye"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

#constructor funcition
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation: adding two strings to form large string
fullname = first + " " + last
print(fullname) 

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1999)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple line
multiline = '''
Hey, how are you?                

I am fine I am fine.               

                     Everything good?

Asap
'''
print(multiline)

# Escaping special characters
statement = 'I\'m back at work\tYou hear me\n\nwhere\'s this at\\located?'
print(statement)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "Ok"))
print(multiline)

print(len(multiline))
multiline += "                         "
multiline = "                " + multiline
print(len(multiline))

# Remove the white space
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffe".ljust(16, "-") + "$2".rjust(4))
print("Tea".ljust(16, "-") + "$2".rjust(4))
print("Makiyato".ljust(16, "-") + "$10".rjust(4))
print("Milk".ljust(16, "-") + "$6".rjust(4))
print("Spris".ljust(16, "-") + "$4".rjust(4))
print("")

# trying index values
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
print(first[5])
print(first[-1]) #The last value in the string in every strings
print("")

print(first[0:3])
print(first[0:5])
print(first[0:-1])
print(first[0:])
print("")

 
# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("A"))
print(first.endswith("a")) 
print("")


