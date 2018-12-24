# global variables file
import sqlite3

game=sqlite3.connect("game.db")
gamecurs=game.cursor()


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
