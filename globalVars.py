# global variables file
import sqlite3

game=sqlite3.connect("game.db")
gamecurs=game.cursor()

# Progam for retrieving player_name,style
sql= "select name,category,value from stats;"
gamecurs.execute(sql)
players_data_tuple=gamecurs.fetchall()
players_data_list = []
players_score_list = []
for i in range(0,len(players_data_tuple)):
    a = []
    b = []
    a.append(players_data_tuple[i][0])
    b.append(players_data_tuple[i][0])
    a.append(players_data_tuple[i][1])
    b.append(players_data_tuple[i][2])
    players_data_list.append(a)
    players_score_list.append(b)

players_data_dict = dict(players_data_list)
players_score_dict = dict(players_score_list)

game.commit()
game.close()

def init():
    global teamNames
    global selectedTeam
    global teamData
    global pointAvail
    global teamSelections
    global playersAvail
    selectedTeam = '--' # since this is the first option in the combo box
    teamNames = ['--'] # A Default team is created for the player. Just for testing
    teamData = dict() # dictionary for players present in each team
    teamSelections = dict() # dictionary for storing the number of selected team members and points available to the team 
    playersAvail = dict() # store the available players wrt each team

if __name__ == "__main__":
    init()
=======

def init():
    global teamNames
    teamNames = []

# Progam for retrieving player_name,style
sql= "select name,category from stats;"
gamecurs.execute(sql)
players_data_tuple=gamecurs.fetchall()
players_data_list=[]
for i in range(0,len(players_data_tuple)):
    a=[]
    a.append(players_data_tuple[i][0])
    a.append(players_data_tuple[i][1])
    players_data_list.append(a)

print(players_data_list)

game.commit()
game.close()
