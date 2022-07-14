# in JS console.log("Hello World")
print("Hello World")

# var x = 5
x = 5

# x = "Hey there"
x = "Hey There"

pets = ["Copper", "Lucy"] # List


# Lists

# Add a pet to the list
pets.append("Shosh") # Adds to a list
pets.insert(3, "BayBay") # the number says where to put it and then what put
pets.pop() # pop removes the last entry from a list
pets.remove("Copper") # needs the value of what you want removed


# Dictionary

owner = {"name": "Melissa", "age": 43, "location": "Berwick, PA"}
name = owner['name']
print("the value of name is", name)

# Melissa is 43 years old and lives in Berwick, PA
print(f"{owner['name']} is {owner['age']} years old and lives in {owner['location']}")
print("pring the length of the dict =", len(owner))
print("the whole dict", owner)

# create a if statement to print true if x is less than 5 and false if greater than 5

x = 10
x = 5
x = 6
if (x < 5):
    print(True)
else:
    print(False)

    # True and False don't need "" due to them beeing part of the booleans

y = 9

if (y < 10):
    print("y is less than 10")
if (y < 5):
    print("y is less than 5")
else:
    print("no if statement was true")

    # both teh 1st if and the else will print as both if's were not true

y = 9

if (y < 10):
    print("y is less than 10") #if true print me
elif (y < 5):
    print("y is less than 5") # if above is false but i am true print me
else:
    print("no if statement was true") # if none are true then print me

# This will only print the 1st if because it was true and not the elif so it stopped

# function x () { 
#   instructions here
# }
def x():
    pass