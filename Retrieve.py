import sqlite3
game=sqlite3.connect('game.db')
gamecurs=game.cursor()

#Retriving for palyer stats


try:
    name=input("Enter player name:")
    col="PRAGMA table_info(stats)"
    gamecurs.execute(col)
    column_name=gamecurs.fetchall() # to fetch column names
    sql="select * from stats where name='"+ name.upper() +"';"
    gamecurs.execute(sql)
    data=gamecurs.fetchone()   # to fetch data
    data_dict={}
    for i in range(0,len(data)):
        data_dict.update({column_name[i][1]:data[i]})
    game.commit()
    print(data_dict) # prints the record in shell
except:
    data_dict='Can\'t be fetched'
    print(data_dict)
    game.rollback()
game.close()


