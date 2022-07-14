melissa = {
    "favoriteNumber": 24,
    "meaning": "HoneyBee",
    "age": 43,
    "hobbies": [
        "Crocheting",
        "Garding",
        "Playing Minecraft"
        ]
    }

# 1. Print to the terminal all of the data
print("#1 Printing the whole object:", melissa)

# 2. Print my age
print("#2a Melissa's Age:", melissa['age'])
print("#2b Melissa's Age:"+ str(melissa['age']))


print(f"Melissa is {melissa['age']} years old") #f-string
print("Melissa is {} years old and her favorite number is {}".format(melissa['age'], melissa['favoriteNumber'])) # string.format
print("Melissa is %s years old" % melissa['age']) # %-formating


# 3. Print my hobbies
print("#3 printing all my Hobbies:", melissa['hobbies'])

#  4. Print the last hobby listed
print("#4 printing the last hobby in the list:", melissa['hobbies'][2])

melissa2 = {
    "favoriteNumber": 24,
    "meaning": "HoneyBee",
    "age": 43,
    "hobbies": [
            {
                "name": "Crocheting"
            },
            {
                "name": "Garding"
            },
            {
                "name": "Playing Minecraft"
            }
        ]
    }
# 5 print all the hobby names
print("#5a all the hobby names:", melissa2['hobbies'][0]['name'], melissa2['hobbies'][1]['name'], melissa2['hobbies'][2]['name']) # Bad format due to you never know the length of the list

hobbies = melissa2['hobbies'] # Globally accessible for whole file
def hobbyNames():
    for hobby in hobbies:
        print("#5b the hobby names:", hobby['name'])

hobbyNames()
# line 50 =  creating a var called hobbies that contains the list of the hobby objects
# line 51 = start of function 
# line 52 = starting a loop saying for every hobby in the list of hobbies follow the following instructions
# line 53 = the instructions of what to print
# line 55 = activating the function

for hobby in hobbies:
    print("#5c the hobby names:", hobby['name'])

# 6 Print the last hobby
print("#6a printing the last hobby name:",melissa2['hobbies'][2]['name'])
print("#6b printing the last hobby name:", hobbies[2]['name'])

# 7 check to see if the second hobby is crocheting
for i in range(len(hobbies)):
    if hobbies[i]['name'] == "Crocheting":
        print("#7a:",True)
    else:
        print("7a:", False)

if (hobbies[1]['name'] == "Crocheting"):
    print("#7b:",True)
else:
    print("7b:", False)