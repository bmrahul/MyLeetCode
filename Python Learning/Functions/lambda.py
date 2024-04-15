# In Python, you can pass a function to another function or return a function from another function.
# Functions that accept a function example

def getFullName(firstName, LastName, formatter):
    return formatter(firstName, LastName)

def firstLast(firstName, lastName):
    return f'{firstName} {lastName}'

def lastFirst(firstName, lastName):
    return f'{lastName} {firstName}'

print("FirstLast: \t", getFullName('Rahul', 'Bansode', firstLast))
print("LastFirst: \t", getFullName('Rahul', 'Bansode', lastFirst))

# Instead of defining the firstLast and lastFirst functions, you can use lambda expressions.

print("\ncall using Lambda expression: \n")

print("FirstLast: \t", getFullName('Rahul', 'Bansode', lambda firstName, lastName: f'{firstName} {lastName}'))
print("LastFirst: \t", getFullName('Rahul', 'Bansode', lambda firstName, lastName: f'{lastName} {firstName}'))


def times(n):
    return lambda x: x * n

come = times(5)

print(come(3))

callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
