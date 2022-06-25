from sys import get_coroutine_origin_tracking_depth


print(2+3)
print("Learning python with ammar")
print("Lets begin")

print('begin')
print('''again begin''')  # all theses quotations can work for strings

print("what's up")

# we can also excess single character from a string

fruit= ("banana")

print(fruit[1])
print(fruit[2])

# strings are immutable
    # means you cant replace it directly with something
    # can only be done by use +

greetings= ("hello guyz")
new_greeting = greetings[0:5] +" Azam"
print(new_greeting)
#or
new= "j"+greetings[1:]
print(new)

# the type ftn shos type of an object and the dir ftn shows the available methods

print(type(greetings))

print(dir(greetings))
help(greetings.capitalize)
print(greetings.capitalize())

#other example

line= "Have a nice day"
print(line.startswith("Have"))