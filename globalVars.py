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

def Team_name():
    game=sqlite3.connect('game.db')
    gamecurs=game.cursor()
    sql ="select name from teams"
    gamecurs.execute(sql)
    a=gamecurs.fetchall()
    game.commit()
    b=['--']
    for i in a:
        print("element is:",i[0])
        if i[0] not in b:
            b.append(i[0])
    game.close()
    return b
def Team_data(b):
    game=sqlite3.connect('game.db')
    gamecurs=game.cursor()
    team={}
    for i in b:
        if i != '--':
            sql="select player from teams where name='"+str(i)+"';"
            gamecurs.execute(sql)
            c=gamecurs.fetchall()
            temp=[]
            for j in c:
                temp.append(j[0])
            team.update({i:temp})
    game.commit()
    game.close()
    return team

def Players_avail(team):
    game=sqlite3.connect('game.db')
    gamecurs=game.cursor()
    teamav={}
    for i in team.keys():
        if i!='--':
            sql="select name,category from stats;"
            gamecurs.execute(sql)
            a=gamecurs.fetchall()
            temp={"BAT":[],"BOW":[],"AR":[],"WK":[]}
            for j in a:
                if j[0] not in team[i]:
                    if j[1] =='BAT':
                        temp["BAT"].append(j[0]) 
                    elif j[1]=='BOW':
                        temp["BOW"].append(j[0])
                    elif j[1]=='WK':
                        temp["WK"].append(j[0])
                    elif j[1]=='ALL':
                        temp["AR"].append(j[0])                
            teamav.update({i:temp})
    game.commit()
    game.close()
    return teamav
def Team_select(team):
    game=sqlite3.connect('game.db')
    gamecurs=game.cursor()
    teamsel={}
    for i in team.keys():
        if i!='--':
            temp={"bat":0,"bow":0,"ar":0,"wk":0,"point":840,"used":0}
            j=team[i]
            for a in j :
                sql="select category,value from stats where name='"+str(a)+"';"
                gamecurs.execute(sql)
                b=gamecurs.fetchone()
                use=0
                if b[0] =='BAT':
                    temp["bat"] += 1
                    use += b[1]
                elif b[0]=='BOW':
                    temp["bow"] += 1
                    use += b[1]
                elif b[0]=='WK':
                    temp["wk"] += 1
                    use += b[1]
                elif b[0]=='ALL':
                    temp["ar"] += 1
                    use += b[1]
                temp["used"] += use
                temp["point"] -= use
        teamsel.update({i:temp})
    game.commit()
    game.close()
    return teamsel

    
def init():
    global teamNames
    global selectedTeam
    global teamData
    global pointAvail
    global teamSelections
    global playersAvail
    selectedTeam = '--' # since this is the first option in the combo box
    teamNames = Team_name() # A Default team is created for the player. Just for testing
    teamData = Team_data(teamNames) # dictionary for players present in each team
    teamSelections = Team_select(teamData) # dictionary for storing the number of selected team members and points available to the team 
    playersAvail = Players_avail(teamData) # store the available players wrt each team

if __name__ == "__main__":
    init()
