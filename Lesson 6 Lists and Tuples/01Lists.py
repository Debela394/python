users = ['Dave', 'John', 'Sara']

data = ['Dollar', 42, 'True']

emptylist = []
print("")
print("Dave" in emptylist)
print("Dave" in users)

print("")

print(users[0])
print(data[0])
print(users[-1])

print("")

print(users[-1])
print(users[-2])
print(users[-3])
print(users.index('Sara'))

print("")

print(users[0:2])
print(users[0:])
print(users[0:-1])
print(users[-2:-1])

print(len(data)) 
print("")

users.append('Elsa')
emptylist.append('Elsa')
print(users)
print(len(users))
print(emptylist)
print(len(emptylist))

print("")

users += ['Jonson']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

print("")

users.extend(data)
print(users)

print("")

users.insert(0, 'Bob')
print(users)
print(len(users))

print("")

users[2:2] = ['Eddie', 'Alex']
print(users)
print(len(users))

print("")

# to replace the second and third string elements
users[1:3] = ['Robert', 'JPJ']
print(users)
print(len(users))

print("")

# To remove specific elemnet/item out of lists
users.remove('Bob')
print(users)
print(len(users))

print("")

# To pop off the last user/item from lists
print(users.pop())
print(len(users))
print(users)

print("")

# To delete specific item from list
del users[0]
print(users)

print("")

#  To delete full list fro data
# del data - to delete completely the list
data.clear()  #Clear the item but empty list exists
print(data)

print("")

# Sort all alphabetical
del users[-1]
users.sort()
print(users)
print("")

# Sort some items and change its case
users[1:2] = ['dave']
users.sort()
print(users)
print("")

users.sort(key=str.lower)
print(users)

print("")

