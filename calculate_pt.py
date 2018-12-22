# for calucating performances

from math import floor
import sqlite3
game=sqlite3.connect('game.db')
gamecurs=game.cursor()

#function for calculation points(batting)

def score_bat(faced,runs,fours,sixes):
    score=0
    score += (floor(runs/2)+fours*1+sixes*2)
    if runs>=100:
        score += 10
    elif 50<=runs<100:
        score += 5
    else:
        score +=0
    try:
        sr=(runs/faced)*100
        if sr>100:
            score += 4
        elif 80<=sr<=100:
            score +=2
        else:
            score +=0
    except:
        score +=0   
    return score

#function for calculation points(Bowling)

def score_bow(bowled,wkts):
    score=0
    score += 10*wkts
    if wkts>=5:
        score += 10
    elif 3<=wkts<5:
        score +=5
    else:
        score +=0
    try:
        ec=(runs*6/bowled)
        if 3.5<ec<=4.5:
            score +=4
        elif 2<ec<=3.5:
            score +=7
        elif ec<=2:
            score +=10
        else:
            score +=0
    except:
        score +=0
    return score

#function for calculation points(Fielding)

def score_fld(catches,stumping,runouts):
    score=0
    score += 10*(catches+runouts+stumping)
    return score

#function for calculation points(Total of palyer)

def score(match_num,player_nm):
    sql="SELECT FACED,RUNS,FOURS,SIXES,BOWLED,WKTS,CATCHES,STUMPING,RUNOUTS FROM'"+str(match_num)+"'WHERE NAME='"+str(player_nm)+"';"
    gamecurs.execute(sql)
    data=gamecurs.fetchone()
    score_pl=0;
    score_pl += score_bat(data[0],data[1],data[2],data[3]);
    score_pl += score_bow(data[4],data[5]);
    score_pl += score_fld(data[6],data[7],data[8]);
    return score_pl
    
try:
    score_pt=0
    match=int(input("Enter match number:"))
    match="MATCH"+str(match)
    for i in range(1,12):
        name=input("enter player name:")
        score_pt +=score(match,name.upper())
    total_pt = score_pt
    print(total_pt)
except:
    total_pt=0
    print(total_pt)









        
        
