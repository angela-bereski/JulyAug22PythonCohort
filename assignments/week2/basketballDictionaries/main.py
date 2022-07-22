class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age =data['age']
        self.position = data['position']
        self.team = data['team']
    
    def showInfo(self):
        print(f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
damian = {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
}
joel = {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Forward", 
    	"team": "Philadelphia 76ers"
}
player_kevin=Player(kevin)
player_jason=Player(jason)
player_kyrie=Player(kyrie)
player_damian=Player(damian)
player_joel=Player(joel)

player_jason.showInfo()

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]



# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for i in Player:
    new_team.append(i)
    


