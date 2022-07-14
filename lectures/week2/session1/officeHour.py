from data import trainingSchool
# [] = a list (like basket of eggs) will need an index to chose just 1
# {} = a dict (1 egg) will not need and index but the key to print the value

# I want to print the 1st classes 1st pet's owners first name


# Step 1: print everything in our data
# print("1:", trainingSchool)

#  Step 2: print 1st index
# print("2: ", trainingSchool[0])

# Step 3: print 1 value from the dict
# print("3: ", trainingSchool[0]['className'])
# Now we are printing a value inside our 1st index lets work on the next level inside it

# Step 4: print the 1st index of petsInClass
# print("4: ", trainingSchool[0]['petsInClass'][0])

# Step 5: print 1 value from the dict (repeat of step 3)
# print("5: ", trainingSchool[0]['petsInClass'][0]['name'])

# Step 6: print owner
# print("6: ", trainingSchool[0]['petsInClass'][0]['owner'])

# Step 7: Print pet's owner's first name
# print("6: ", trainingSchool[0]['petsInClass'][0]['owner']['firstName'])


# print Jane's skill of agility

# Step 3: Printing Janes information
# print("3: ", trainingSchool[0]['trainer'])

# Step 4: print the skill index we want
# print("4: ", trainingSchool[0]['trainer']['skills'][1])

# Step 5: print the value of agility
# print("5: ", trainingSchool[0]['trainer']['skills'][1]['skillName'])

# print Lady's owners 1st name in the Krusing Kainines class

# Step 2: Print the correct class
print("2: ", trainingSchool[3])

# Step 3: print the correct pet's info
print("3: ", trainingSchool[3]['petsInClass'][1])

# Step 4: print the owners information
print("4: ", trainingSchool[3]['petsInClass'][1]['owner'])

# Step 5: print the owners first name
print("5: ", trainingSchool[3]['petsInClass'][1]['owner']['firstName'])