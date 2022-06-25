## while and for loops

## WHILE loop


x=0
while x<5:
    print(x)
    x=x+1


## FOR loop
    #if we want to loop through a set of things such as, list of words, the line in a file, or list of numbers
    # we have list of thing to loop through, we can construct a definite loop using a for statement

#example 
friends= ['A','B','c','D']
for friend in friends:
    print("Happy new year: ",friend)

#example

for i in range(2,12):
    print(i)


#example

days =['Mon','tue','wed','thur','fri','sat','sun']

for day in days:
    # if day=="fri":break  #loop stops
    if day =="fri":continue # skips day
    print("Today is : ",day)

# for example if we want to get the index also

age =[10,13,15,17,20]
for index,a in enumerate(age):
    print("index"+str(index)+  ":"+ str(age))

# for loop also works on strings

for c in "family":
    print(c.capitalize())


# loop on other data structure such as Dictonary
    # we use item()

#example

world= {"Pak":350, "india":600, "US":900}

for k, v in world.items():
    print(k+":", str(v))

#  using for loop on 2D Numpy (Arrays)
    # we use np.nditer

import numpy as np
np_height = np.array([1.73,1.66,1.89,2.0])
np_wedth = np.array([65.4,59.3,60.7,70])
total= np.array([np_height,np_wedth])
 
for val in np.nditer(total):
    print(val)



