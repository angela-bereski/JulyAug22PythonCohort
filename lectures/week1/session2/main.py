trainingSchool = [
    {
        id: 1,
        "className": "Eating right with Jane",
        "trainer": {
            id: 1,
            "firstName": "Jane",
            "lastName": "Doe",
            "skills": [
                {
                    id: 1,
                    "skillName": "Nutrition"
                },
                {
                    id: 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [
            {
                id: 2,
                "name": "Bear",
                "breed": "Mixed",
                "species": "Dog",
                "gender": "Male",
                "age": 7,
                "owner": {
                    id: 1,
                    "firstName": "Melissa",
                    "lastName": "Longenberger"
                }
            },
            {
                id: 3,
                "name": "Copper Tone",
                "breed": "Beagle",
                "species": "Dog",
                "gender": "Male",
                "age": 1,
                "owner": {
                    id: 1,
                    "firstName": "Melissa",
                    "lastName": "Longenberger"
                }
            }
        ]
    },
    {
        id: 2,
        "className": "Jumping Basics",
        "trainer": {
            id: 2,
            "firstName": "John",
            "lastName": "Smith",
            "skills": [
                {
                    id: 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [
            {
                id: 1,
                "name": "Butch",
                "breed": "Boxer",
                "species": "Dog",
                "gender": "Male",
                "age": 3,
                "owner": {
                    id: 2,
                    "firstName": "Bob",
                    "lastName": "Ross"
                }
            }
        ]
    },
    {
        id: 3,
        "className": "Advanced Jumping",
                "trainer": {
            id: 2,
            "firstName": "John",
            "lastName": "Smith",
            "skills": [
                {
                    id: 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [

        ]
    },
    {
        id: 4,
        "className": "Kruisin Kaninies",
        "trainer": {
            id: 1,
            "firstName": "Jane",
            "lastName": "Doe",
            "skills": [
                {
                    id: 1,
                    "skillName": "Nutrition"
                },
                {
                    id: 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [
            {
                id: 3,
                "name": "Copper Tone",
                "breed": "Beagle",
                "species": "Dog",
                "gender": "Male",
                "age": 1,
                "owner": {
                    id: 1,
                    "firstName": "Melissa",
                    "lastName": "Longenberger"
                }
            },
            {
                id: 4,
                "name": "Lady",
                "breed": "Mixed",
                "species": "Dog",
                "gender": "Female",
                "age": 2,
                "owner": {
                    id: 3,
                    "firstName": "Bill",
                    "lastName": "Ross"
                }
            }
        ]
    }
]


# print("#1:", trainingSchool[0]) # will print all of index 0 or id1
# print("#2:", trainingSchool[0]['trainer']) #prints just index 0's trainer information
# print("#3:", trainingSchool[0]['trainer']['skills'])

trainerSkills = trainingSchool[0]['trainer']['skills']
for skill in trainerSkills:
    # print("#4a:", skill['skillName'])
    # print("#4b:", skill)
    pass

# print("#5a:", trainingSchool[0]['trainer']['petsInClass'])
# print("#5b:", trainingSchool[0]['petsInClass'])
print("#6:", trainingSchool[0]['petsInClass'][0])

pets = trainingSchool[0]['petsInClass']

for pet in pets:
    # print("#7a:", pet['name'])
    print("#7b:", pet['owner']['firstName'])

thePets = trainingSchool[3]['petsInClass']

for pet in thePets:
    # print("#7a:", pet['name'])
    print("#7b:", pet['owner']['firstName'])

for c in trainingSchool: # looping through entire list of school classes
    print("#8a:", c['className']) # printing the class names
    print("#8a:", c['className'],c['trainer'])
    for trainer in c['trainer']: # looping through all the trainers in each class
        print("#8b:", trainer) # printing the trainer object

