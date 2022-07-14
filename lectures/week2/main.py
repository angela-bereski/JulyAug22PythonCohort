pets = [
        {'name':  'Copper', 'breed' : 'Beagle'},
        {'name' : 'Bear', 'breed' : 'Shepard Mix'},
        {'name' : 'Lucy', 'breed' : 'Chawinni'},
        {'name' : 'Roxy', 'breed' : 'Red Nose Pit Shepard'}
    ]

def keyValue(list): # creating function passing in a list to be named during activation
    for i in range(0, len(list)): # looping through the whole list
        output = "" # creating var output setting to empty string so that it can hold info to follow
        for key,val in list[i].items(): # for each key & value in the list of items do the following (items() are refering to the items inside the dict)
            output += f"{key} - {val}," # change the value of output to equal the key - value
        print("Printing output of each index:",output) # print output at end of each loop

# keyValue(pets) # activates function

# Think of this way of doing a for loop like this in order to collect the eggs the farmer needs a basket.  Not just any basket but an empty one.  So line 10 is our way of creating not just a basket but an empty one.  Then on line 11 we need to tell the farmer what to put into this basket.  The Brown Hens aren't collected in the morning just the White ones for example.  So the instructions on line 11 are stating just what we want in the basket.  Line 12 is the act of putting those eggs into the basket and line 13 being outside of the loop will show the final results of what we told the farmer to do... collect the eggs


# The output += means that we add the current value to what was already there... not overwrite it but add to it.  If we just put = then it would over write.  Since we want the collection of eggs to grow we have to add the + in there other wise it's like getting a new basket for each nest.


def keyValue2(list): # creating function passing in a list to be named during activation
    for i in range(0, len(list)): # looping through the whole list
        output = f"name - {list[i]['name']}, breed - {list[i]['breed']}" # creating a var to contain what we want to print in this case an f string containing the manualy coded key and looped index'd value
        print("Printing output of each index:", output) # print output at end of each loop

# keyValue2(pets) # activates function

# list[i]['name'] = the value of the key name
# print(pets[0]) # This will print the whole index
# print(pets[0]['name']) # This will print the value of the chosen key

print(pets) # Print whole list
print(pets[0]) # print 1st index
print(pets[0]['name']) # print the name

def petNames(list): # create the funciton passing in a var for the list
    for p in range(0, len(list)): # create the loop starting a index 0 to to end do the following
        print(list[p]['name']) # print the list[current loops index][key of name]

petNames(pets) # activate passing inthe name of the actual list

for pet in pets:
    pass