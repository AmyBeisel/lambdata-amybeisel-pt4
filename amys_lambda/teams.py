
# example teams.py (functional approach)

class Team():
    def __init__(self, name, city):
        self.name = name
        self.city = city

def advertise(my_team):
    print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")

def full_name(my_team):
    return f"{my_team['city']} {my_team['name']}"

if __name__ == "__main__":
    # teams = [
    #     {"city": "New York", "name": "Yankees"},
    #     {"city": "New York", "name": "Mets"},
    #     {"city": "Boston", "name": "Red Sox"},
    #     {"city": "New Haven", "name": "Ravens"},
    #     {"city": "Washington", "name": "Nationals"}
    # ]
    # for team in teams:
    #     print("-------")
    #     print(full_name(team))
    #     advertise(team)


    # df = DataFrame ({"x": [1,2,3], "y" : [4,5,6]})
    #df.head()
    #df = DataFrame({"x": [7,7,7], "y": [4,4,4]})
    #df.head()

    team = Team(city="Washington", name = "Wizards") #initilize / create an instance of the object. 
    print(team)
    print(type(team))
    print(team.name) #invoking attributes
    print(team.city) #invoking attributes

    team2 = Team("New York", "Giants") #initilize / create an instance of the object. 
    print(team2)
    print(type(team2))
    print(team2.name) #invoking attributes
    print(team2.city) #invoking attributes


