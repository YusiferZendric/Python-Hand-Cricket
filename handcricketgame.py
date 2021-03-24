import random
import ast

from modules import toss
from modules import scorecard
from modules.commentary import scoreRun
from modules.batting import playIn
from modules.bowling import playOut
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice

# Score for each ball faced in the innings
l=[]
# All the arrays required for implementing batting and fielding
m=[]
lb=[]
mb=[]
lq=[]
# Score for each ball faced in an over
lp=[]
# First innings score
sa=0
# Second innings score
sb=0
# Innings: 1st innings or 2nd innings
inig=1
# Possible scores in a ball.
runchoice=('0','1','2','3','4','5','6','W')

pwod=input("Enter match password: ")
fz=open("gpascd.txt",'r')
pchek=fz.read()
fz.close()

if pwod == pchek:
    try:
        opchoice=int(input("For how many overs game? Default: T20, Your choice: "))
    except:
        opchoice=20
    if opchoice<1:
        opchoice=20
    print("Match is for", opchoice, "overs.")

    try:
        wa=int(input("For how many wickets would you want to play? Default: 10 wicket game, Your choice: "))
    except:
        wa=10
    if wa<1 or wa>10:
        wa=10
    print("Total:", wa, "wickets game")

    za=toss.tossPlay()

    if za == "bat":
        f=open("team1.txt", 'r')
        sla=f.read()
        f.close()
        la=ast.literal_eval(sla)
        T3=la[0]
        gpldb=int(la[12])
        gwonb=int(la[13])

        lc=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

    else:
        la=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

        g=open("team1.txt", 'r')
        slb=g.read()
        g.close()
        lc=ast.literal_eval(slb)
        T3=lc[0]
        gpldb=int(lc[12])
        gwonb=int(lc[13])

    #['P1','A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11']
    #['P2','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11']

    T1=la[0]
    T2=lc[0]

    A1=la[1]
    A2=la[2]
    A3=la[3]
    A4=la[4]
    A5=la[5]
    A6=la[6]
    A7=la[7]
    A8=la[8]
    A9=la[9]
    A10=la[10]
    A11=la[11]

    B1=lc[1]
    B2=lc[2]
    B3=lc[3]
    B4=lc[4]
    B5=lc[5]
    B6=lc[6]
    B7=lc[7]
    B8=lc[8]
    B9=lc[9]
    B10=lc[10]
    B11=lc[11]
        
def innFirst():
    print("First Innings")
    sa=0
    btindex=[A1,A3,A4,A5,A6,A7,A8,A9,A10,A11,A2]
    player1=batterChoice(btindex,0,inig,za)
    player2=batterChoice(btindex,player1,inig,za)
    baindex={A1:[0,0,0,0], A2:[0,0,0,0], A3:[0,0,0,0], A4:[0,0,0,0], A5:[0,0,0,0], A6:[0,0,0,0], A7:[0,0,0,0], A8:[0,0,0,0], A9:[0,0,0,0], A10:[0,0,0,0], A11:[0,0,0,0]}
    bindex={B1:[0,0,0,0], B2:[0,0,0,0], B3:[0,0,0,0], B4:[0,0,0,0], B5:[0,0,0,0], B6:[0,0,0,0], B7:[0,0,0,0], B8:[0,0,0,0], B9:[0,0,0,0], B10:[0,0,0,0], B11:[0,0,0,0]}
    bowlerlist=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11]
    b=['']
    score=0
    wicket=0
    onstrike=player1
    gameIsPlaying=True
    while gameIsPlaying:
        for i in range (1, opchoice+1):
            if i==opchoice:
                gameIsPlaying=False
            if wicket==wa:
                gameIsPlaying=False
            else:
                over=i
                print("Over", i)
                bowler=fieldChoice(bowlerlist,inig,za)
                if bindex[bowler][0]>=(opchoice/5) or bowler == b[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bindex[bowler][0]<(opchoice/5):
                        bowlerlist.append(b[i-1])
                for j in range (1, 7):
                    if wicket==wa:
                        gameIsPlaying=False
                    else:
                        print("Ball", j)
                        if za == "bat":
                            ra=playIn(bowler,onstrike)
                        else:
                            ra=playOut(bowler,onstrike)
                        if ra != 'W':
                            run=int(ra)
                        else:
                            ra='W'
                            run=0
                            wicket+=1
                            bindex[bowler][3]+=1
                        score=score+run
                        bindex[bowler][2]+=run
                        baindex[onstrike][0]+=run
                        baindex[onstrike][1]+=1
                        if run==4:
                            baindex[onstrike][2]+=1
                        if run==6:
                            baindex[onstrike][3]+=1
                        scoreRun(ra,bowler,onstrike)
                        if ra == 'W':
                            if onstrike == player1:
                                player1=''
                            elif player2 == onstrike:
                                player2=''
                            
                            if za == 'bat':
                                btindex.append('')
                            if player1 == '':
                                onstrike=batterChoice(btindex,player2,inig,za)
                                player1=onstrike
                            elif player2 == '':
                                onstrike=batterChoice(btindex,player1,inig,za)
                                player2=onstrike
                        m.append(ra)
                        l.append(ra)
                        lq.append(run)
                        if run%2 != 0:
                                if onstrike==player1:
                                    onstrike=player2
                                else:
                                    onstrike=player1  
                b.append(bowler)
                bindex[bowler][0]+=1
                if lq==[0,0,0,0,0,0]:
                    bindex[bowler][1]+=1
                print("This over:", m)
                print("Batting:")
                print(player1,":", baindex[player1][0],"(",baindex[player1][1],")")
                print(player2,":", baindex[player2][0],"(",baindex[player2][1],")")
                print("Bowling:")
                print(bowler,":",bindex[bowler][0],"-",bindex[bowler][1],"-",bindex[bowler][2],"-",bindex[bowler][3])
                print("Score: ", score, "/", wicket)
            if onstrike==player1:
                onstrike=player2
            else:
                onstrike=player1
            m.clear()
            lq.clear()
            yx=input()
    print("End of 1st innings")
    scorecard.scoreCard(baindex,bindex,la,lc,inig)
    return score

if pwod == pchek:
    sa=innFirst()
    inig+=1

def innSecond():
    print("Second Innings")
    print("Target:", sa+1)
    btindex=[B1,B3,B4,B5,B6,B7,B8,B9,B10,B11,B2]
    player1=batterChoice(btindex,0,inig,za)
    player2=batterChoice(btindex,player1,inig,za)
    baindex={B1:[0,0,0,0], B2:[0,0,0,0], B3:[0,0,0,0], B4:[0,0,0,0], B5:[0,0,0,0], B6:[0,0,0,0], B7:[0,0,0,0], B8:[0,0,0,0], B9:[0,0,0,0], B10:[0,0,0,0], B11:[0,0,0,0]}
    bindex={A1:[0,0,0,0], A2:[0,0,0,0], A3:[0,0,0,0], A4:[0,0,0,0], A5:[0,0,0,0], A6:[0,0,0,0], A7:[0,0,0,0], A8:[0,0,0,0], A9:[0,0,0,0], A10:[0,0,0,0], A11:[0,0,0,0],}
    bowlerlist=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]
    b=['']
    score=0
    wicket=0
    onstrike=player1
    gamebIsPlaying=True
    while gamebIsPlaying:
        for i in range (1, opchoice+1):
            if i==opchoice:
                gamebIsPlaying=False
            if wicket==wa or score>sa:
                gamebIsPlaying=False
            else:
                over=i
                print("Over", i)
                bowler=fieldChoice(bowlerlist,inig,za)
                if bindex[bowler][0]>=(opchoice/5) or bowler == b[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bindex[bowler][0]<(opchoice/5):
                        bowlerlist.append(b[i-1])
                for j in range (1, 7):
                    if wicket==wa or score>sa:
                        gamebIsPlaying=False
                    else:
                        print("Ball", j)
                        if za == "bat":
                            ra=playOut(bowler,onstrike)
                        else:
                            ra=playIn(bowler,onstrike)
                        if ra != 'W':
                            run=int(ra)
                        else:
                            ra='W'
                            run=0
                            wicket+=1
                            bindex[bowler][3]+=1
                        score=score+run
                        bindex[bowler][2]+=run
                        baindex[onstrike][0]+=run
                        baindex[onstrike][1]+=1
                        if run==4:
                            baindex[onstrike][2]+=1
                        if run==6:
                            baindex[onstrike][3]+=1                        
                        scoreRun(ra,bowler,onstrike)
                        if ra == 'W':
                            if onstrike == player1:
                                player1=''
                            elif player2 == onstrike:
                                player2=''
                            
                            if za == 'field':
                                btindex.append('')
                            if player1 == '':
                                onstrike=batterChoice(btindex,player2,inig,za)
                                player1=onstrike
                            elif player2 == '':
                                onstrike=batterChoice(btindex,player1,inig,za)
                                player2=onstrike
                        mb.append(ra)
                        lb.append(ra)
                        lp.append(run)
                        if run%2 != 0:
                                if onstrike==player1:
                                    onstrike=player2
                                else:
                                    onstrike=player1  
                b.append(bowler)
                bindex[bowler][0]+=1
                if lp==[0,0,0,0,0,0]:
                    bindex[bowler][1]+=1
                print("This over:", mb)
                print("Batting:")
                print(player1,":", baindex[player1][0],"(",baindex[player1][1],")")
                print(player2,":", baindex[player2][0],"(",baindex[player2][1],")")
                print("Bowling:")
                print(bowler,":",bindex[bowler][0],"-",bindex[bowler][1],"-",bindex[bowler][2],"-",bindex[bowler][3])
                print("Score: ", score, "/", wicket)
                print("Need", sa+1-score, "runs to win off", opchoice-i, "overs")
                if onstrike==player1:
                    onstrike=player2
                else:
                    onstrike=player1
                lp.clear()
                mb.clear()
                yx=input()
    scorecard.scoreCard(baindex,bindex,la,lc,inig)
    return [score, wicket]

if pwod == pchek:        
    sb=innSecond()
    sba=sb[0]
    sbb=sb[1]
    if sa>sba:
        if za == "bat":
            print("Congratulations, you won!")
            zza=1
        else:
            print("Sorry, you lost this game. Better luck next time.")
            zza=0
        print(T1, "wins by", sa-sba, "runs")
    elif sa<sba:
        if za == "bat":
            print("Sorry, you lost this game. Better luck next time.")
            zza=0
        else:
            print("Congratulations, you won!")
            zza=1
        print(T2, "wins by", 10-sbb, "wickets")
    else:
        print("Tied")
        zza=0
        print("You are eligible to play Super Over to decide the tie! Win the super over and then see the number of games won!")
        xzzzint = random.randint(0,1000000000)
        print("Your Super over key is ", xzzzint, " Keep it safe since you need it to play the super over.")
        xzzzza=open("tiepascd.txt","w")
        xzzzzl=[pchek,xzzzint,za]
        xzzzza.write(str(xzzzzl))
        xzzzza.close()

    gwona="team"+str(T3)+".txt"
    gplda=open(gwona, "r")
    gpldh=gplda.read()
    gplda.close()
    dtja=ast.literal_eval(gpldh)
    print()
    gpldc=int(int(dtja[12])+1)
    gwonb=int(dtja[13])

    if zza==0:
        gwonc=gwonb
    else:
        gwonc=gwonb+1
    dtja[12]=gpldc
    dtja[13]=gwonc
    gwonf=open(gwona, "w")
    gwonf.write(str(dtja))
    gwonf.close()

        
    winpercentage=(gwonc*100)/gpldc
    print("Games played: ", gpldc)
    print("Games won: ", gwonc)
    print("Win Percentage", winpercentage)
    end_game_notify=input()

if pwod != pchek:
    wrong_password_notify=input("Sorry, wrong password! Make sure that you enter the correct password before proceeding")
