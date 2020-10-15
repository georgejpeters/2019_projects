import pandas as pd
import random
import numpy as np 
import math
def team_input():
    av1=[0]
    av2=[0]
    fa=[]
    t1=[]
    t2=[]
    player_rating=[]
    gpg_list=[]
    final_team1=[]
    final_team2=[]
    players=[]
    pl=[]
    file='sd.xlsx'
    x1=pd.read_excel(file)
    df = pd.DataFrame(x1)
    regulars = df["fname"].tolist()
    Wl = df["W/L"].values.tolist()
    gpg=df['gpg'].values.tolist()
    gp=df['gpg'].values.tolist()
    ages=df['age'].values.tolist()
    gpg.sort(reverse=True)
    print(ages)
    print(gpg)
    for n in gp:
        if n>=1.5:
            player_rating.append(6)
        elif 1.5>n>=1:
            player_rating.append(4)
        elif 1>n>=0.6:
            player_rating.append(2)
        elif n<0.6:
            player_rating.append(0)
    print(player_rating)
    for n in list(enumerate(ages)):
        if n[1]<=34:
            ind=n[0]
            player_rating[ind]=player_rating[ind]+4
        elif 34<n[1]<=42:
            ind=n[0]
            player_rating[ind]=player_rating[ind]+3
        elif 42<n[1]<=50:
            ind=n[0]
            player_rating[ind]=player_rating[ind]+2
        elif n[1]>50:
            ind=n[0]
            player_rating[ind]=player_rating[ind]+1
    print(player_rating)
    size=input('Is the game 6 (6) a side 5 (5) a side or 4 (4) a side? ')
    
    if size=='6':
        for i in range(12):    
            p=input('What players are playing: ')
            players.append(p)
            pl.append(p)
    elif size=='5':        
        for i in range(10):    
            p=input('What players are playing: ')
            players.append(p)
            pl.append(p)
    elif size=='4':    
        for i in range(8):    
            p=input('What players are playing: ')
            players.append(p)
            pl.append(p)
    else:
        print('Invalid entry')
    
    for i in range(10000):
        if players==[]:
            for n in pl:
                players.append(n)
        elif size=='7':
            for i in range(7):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t1.append(player_rating[ind])
                final_team1.append(r)
                players.pop(indexr)
            for i in range(7):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t2.append(player_rating[ind])
                final_team2.append(r)
                players.pop(indexr)
            if len(t1)>7:
                oteam1_avg=(t1[0]+t1[1]+t1[2]+t1[3]+t1[4]+t1[5]+t1[6])/7
                oteam2_avg=(t2[0]+t2[1]+t2[2]+t2[3]+t2[4]+t2[5]+t2[6])/7
                if oteam1_avg>=oteam2_avg:
                    old_diff=oteam1_avg-oteam2_avg
                elif oteam1_avg<oteam2_avg:
                    old_diff=oteam2_avg-oteam1_avg
                nteam1_avg=(t1[12]+t1[7]+t1[8]+t1[9]+t1[10]+t1[11]+t1[13])/7
                nteam2_avg=(t2[12]+t2[7]+t2[8]+t2[9]+t2[10]+t2[11]+t2[13])/7
                if nteam1_avg>=nteam2_avg:
                    new_diff=nteam1_avg-nteam2_avg
                elif nteam1_avg<nteam2_avg:
                    new_diff=nteam2_avg-nteam1_avg
            if len(t1)>7:
                if new_diff>=old_diff:
                    final_team1.pop(7)
                    final_team1.pop(7)
                    final_team1.pop(7)
                    final_team1.pop(7)
                    final_team1.pop(7)
                    final_team1.pop(7)
                    final_team1.pop(7)
                    t1.pop(7)
                    t1.pop(7)
                    t1.pop(7)
                    t1.pop(7)
                    t1.pop(7)
                    t1.pop(7)
                    t1.pop(7)
                    final_team2.pop(7)
                    final_team2.pop(7)
                    final_team2.pop(7)
                    final_team2.pop(7)
                    final_team2.pop(7)
                    final_team2.pop(7)
                    final_team2.pop(7)
                    t2.pop(7)
                    t2.pop(7)
                    t2.pop(7)
                    t2.pop(7)
                    t2.pop(7)
                    t2.pop(7)
                    t2.pop(7)
                elif new_diff<old_diff:
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
        elif size=='6':
            for i in range(6):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t1.append(player_rating[ind])
                final_team1.append(r)
                players.pop(indexr)
            for i in range(6):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t2.append(player_rating[ind])
                final_team2.append(r)
                players.pop(indexr)
            if len(t1)>6:
                oteam1_avg=(t1[0]+t1[1]+t1[2]+t1[3]+t1[4]+t1[5])/6
                oteam2_avg=(t2[0]+t2[1]+t2[2]+t2[3]+t2[4]+t2[5])/6
                if oteam1_avg>=oteam2_avg:
                    old_diff=oteam1_avg-oteam2_avg
                elif oteam1_avg<oteam2_avg:
                    old_diff=oteam2_avg-oteam1_avg
                nteam1_avg=(t1[6]+t1[7]+t1[8]+t1[9]+t1[10]+t1[11])/6
                nteam2_avg=(t2[6]+t2[7]+t2[8]+t2[9]+t2[10]+t2[11])/6
                if nteam1_avg>=nteam2_avg:
                    new_diff=nteam1_avg-nteam2_avg
                elif nteam1_avg<nteam2_avg:
                    new_diff=nteam2_avg-nteam1_avg
            if len(t1)>6:
                if new_diff>=old_diff:
                    final_team1.pop(6)
                    final_team1.pop(6)
                    final_team1.pop(6)
                    final_team1.pop(6)
                    final_team1.pop(6)
                    final_team1.pop(6)
                    t1.pop(6)
                    t1.pop(6)
                    t1.pop(6)
                    t1.pop(6)
                    t1.pop(6)
                    t1.pop(6)
                    final_team2.pop(6)
                    final_team2.pop(6)
                    final_team2.pop(6)
                    final_team2.pop(6)
                    final_team2.pop(6)
                    final_team2.pop(6)
                    t2.pop(6)
                    t2.pop(6)
                    t2.pop(6)
                    t2.pop(6)
                    t2.pop(6)
                    t2.pop(6)
                elif new_diff<old_diff:
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
        elif size=='5':
            for i in range(5):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t1.append(player_rating[ind])
                final_team1.append(r)
                players.pop(indexr)
            for i in range(5):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t2.append(player_rating[ind])
                final_team2.append(r)
                players.pop(indexr)
            if len(t1)>5:
                oteam1_avg=(t1[0]+t1[1]+t1[2]+t1[3]+t1[4])/5
                oteam2_avg=(t2[0]+t2[1]+t2[2]+t2[3]+t1[4])/5
                if oteam1_avg>=oteam2_avg:
                    old_diff=oteam1_avg-oteam2_avg
                elif oteam1_avg<oteam2_avg:
                    old_diff=oteam2_avg-oteam1_avg
                nteam1_avg=(t1[5]+t1[6]+t1[7]+t1[8]+t1[9])/5
                nteam2_avg=(t2[5]+t2[6]+t2[7]+t2[8]+t2[9])/5
                if nteam1_avg>=nteam2_avg:
                    new_diff=nteam1_avg-nteam2_avg
                elif nteam1_avg<nteam2_avg:
                    new_diff=nteam2_avg-nteam1_avg
            if len(t1)>5:
                if new_diff>=old_diff:
                    final_team1.pop(5)
                    final_team1.pop(5)
                    final_team1.pop(5)
                    final_team1.pop(5)
                    final_team1.pop(5)
                    t1.pop(5)
                    t1.pop(5)
                    t1.pop(5)
                    t1.pop(5)
                    t1.pop(5)
                    final_team2.pop(5)
                    final_team2.pop(5)
                    final_team2.pop(5)
                    final_team2.pop(5)
                    final_team2.pop(5)
                    t2.pop(5)
                    t2.pop(5)
                    t2.pop(5)
                    t2.pop(5)
                    t2.pop(5)
                elif new_diff<old_diff:
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                
        elif size=='4':
            for i in range(4):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t1.append(player_rating[ind])
                final_team1.append(r)
                players.pop(indexr)
            for i in range(4):
                r=random.choice(players)
                ind=regulars.index(r)
                indexr=players.index(r)
                t2.append(player_rating[ind])
                final_team2.append(r)
                players.pop(indexr)
            if len(t1)>4:
                ft1=final_team1[0]+' '+final_team1[1]+' '+final_team1[2]+' '+final_team1[3]
                ft2=final_team2[0]+' '+final_team2[1]+' '+final_team2[2]+' '+final_team2[3]
                nft1=final_team1[4]+' '+final_team1[5]+' '+final_team1[6]+' '+final_team1[7]
                nft2=final_team2[4]+' '+final_team2[5]+' '+final_team2[6]+' '+final_team2[7]
                oteam1_avg=(t1[0]+t1[1]+t1[2]+t1[3])/4
                oteam2_avg=(t2[0]+t2[1]+t2[2]+t2[3])/4
                if oteam1_avg>=oteam2_avg:
                    old_diff=oteam1_avg-oteam2_avg
                elif oteam1_avg<oteam2_avg:
                    old_diff=oteam2_avg-oteam1_avg
                nteam1_avg=(t1[4]+t1[5]+t1[6]+t1[7])/4
                nteam2_avg=(t2[4]+t2[5]+t2[6]+t2[7])/4
                if nteam1_avg>=nteam2_avg:
                    new_diff=nteam1_avg-nteam2_avg
                elif nteam1_avg<nteam2_avg:
                    new_diff=nteam2_avg-nteam1_avg
            if len(t1)>4:
                if new_diff>=old_diff:
                    final_team1.pop(4)
                    final_team1.pop(4)
                    final_team1.pop(4)
                    final_team1.pop(4)
                    t1.pop(4)
                    t1.pop(4)
                    t1.pop(4)
                    t1.pop(4)
                    final_team2.pop(4)
                    final_team2.pop(4)
                    final_team2.pop(4)
                    final_team2.pop(4)
                    t2.pop(4)
                    t2.pop(4)
                    t2.pop(4)
                    t2.pop(4)
                elif new_diff<old_diff:
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    final_team1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    t1.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    final_team2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
                    t2.pop(0)
        else:
            print('Invalid size')
            break
    print(final_team1, t1, final_team2, t2)
    

    
team_input()