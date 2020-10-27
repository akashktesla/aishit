"""
this is a decision making algo by calculating emotions of current state with future state
total human emotions
in 2020 according to a study there are total of 27 emotions
since it is for a simple assignnment in this algo we are calculating main 6 emotions
those are
1.happiness
2.sadness
3.fear
4.anger
5.surprise
6.disgust
"""

from decision import decision
#import items
import random

#assign things
ha=[]      #happiness
sa=[]      #sadness
fe=[]      #fear
an=[]      #anger
sur=[]     #surprise
di=[]      #disgust

hat=[]      #happiness tolerance
sat=[]      #sadness tolerance
fet=[]      #fear tolerance
ant=[]      #anger tolerance
surt=[]     #surprise tolerance
dit=[]      #disgust tolerance

#---------------------------------------------------functions---------------------------------------------------
#happines
def h():
        g= (input("how happy are you on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                ha.append(g)
            if(g>100):
                ha.append(100)

            if(g<0):
                ha.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            h()

#sadness
def s():
        g= (input("how sad are you on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                sa.append(g)
            if(g>100):
                sa.append(100)

            if(g<0):
                sa.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            s()

#fear
def f():
        g= (input("how feared are you on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                fe.append(g)
            if(g>100):
                fe.append(100)

            if(g<0):
                fe.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            f()

#angry
def a():
        g= (input("how angry are you on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                an.append(g)
            if(g>100):
                an.append(100)

            if(g<0):
                an.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            a()

#surprise
def su():
        g= (input("how surprised are you on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                sur.append(g)
            if(g>100):
                sur.append(100)

            if(g<0):
                sur.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            sur()

#disgust
def d():
        g= (input("how disgusted are you on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                di.append(g)
            if(g>100):
                di.append(100)

            if(g<0):
                di.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            d()

#---------------------------------------tolerance---------------------------------------------------------
#happines tolerance
def ht():
        g= (input("how happy can you tolerate on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                hat.append(g)
            if(g>100):
                hat.append(100)

            if(g<0):
                hat.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            ht()

#sadness
def st():
        g= (input("how sadness can you tolerate 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                sat.append(g)
            if(g>100):
                sat.append(100)

            if(g<0):
                sat.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            st()

#fear
def ft():
        g= (input("how fear can you tolerate on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                fet.append(g)
            if(g>100):
                fet.append(100)

            if(g<0):
                fet.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            ft()

#angry
def at():
        g= (input("how angry can you tolerate on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                ant.append(g)
            if(g>100):
                ant.append(100)

            if(g<0):
                ant.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            at()

#surprise
def sut():
        g= (input("how surprise can you tolerate on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                surt.append(g)
            if(g>100):
                sur.append(100)

            if(g<0):
                sur.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            sut()

#disgust
def dt():
        g= (input("how disgust can you tolerate on 0-100% "))

        if(g.isdigit()):
            g=int(g)
            if(g>0 and g<100):

                dit.append(g)
            if(g>100):
                dit.append(100)

            if(g<0):
                dit.append(0)


        else:
            print("input a valid number from 1 - 100 ")
            dt()

#-------------------------------first assignment---------------------------------
#happiness

h()
f()
s()
a()
su()
d()
ht()
st()
ft()
at()
sut()
dt()
#----------------------------finidhed assigneng for the first time-------------------------------------
# decision making function


dec_counter=0

def mk_decision():
    a = decision(0, 0, 0, 0, 0, 0,"name")
    a.name = input("what decision are you going to make ")
    gh = (input("how happy can you tolerate on 0-100% "))

    if (gh.isdigit()):
        gh = int(gh)
        if (gh > 0 and gh < 100):
            a.h=gh
        if (gh > 100):
            a.h=100

        if (gh < 0):
            a.h=0
    else:
        print("enter a valid number from 1-100")


    gh = input(" how much happy this decision makes you ")

    if (gh.isdigit()):
        gh = int(gh)
        if (gh > 0 and gh < 100):
            a.h=gh
        if (gh > 100):
            a.h=100

        if (gh < 0):
            a.h=0
    else:
        print("enter a valid number from 1-100")

    gf = input(" how much fear this decision makes you ")

    if (gf.isdigit()):
        gf = int(gf)
        if (gf > 0 and gf < 100):
            a.f=gf
        if (gf > 100):
            a.f=100

        if (gf < 0):
            a.f=0
    else:
        print("enter a valid number from 1-100")



    gs = input(" how much sadness this decision makes you ")

    if (gs.isdigit()):
        gs = int(gs)
        if (gs > 0 and gs < 100):
            a.s=gs
        if (gs > 100):
            a.s=100

        if (gs < 0):
            a.s=0
    else:
        print("enter a valid number from 1-100")



    ga = input(" how much angry this decision makes you ")
    if (ga.isdigit()):
        ga = int(ga)
        if (ga > 0 and ga < 100):
            a.a=ga
        if (ga > 100):
            a.a=100

        if (ga < 0):
            a.a=0
    else:
        print("enter a valid number from 1-100")


    gsu = input(" how much surprise this decision makes you ")

    if (gsu.isdigit()):
        gsu = int(gsu)
        if (gsu > 0 and gsu < 100):
            a.su=gsu
        if (gsu > 100):
            a.su=100

        if (gsu < 0):
            a.su=0
    else:
        print("enter a valid number from 1-100")

    gd = input(" how much disgust this decision makes you ")

    if (gd.isdigit()):
        gd = int(gd)
        if (gd > 0 and gd < 100):
            a.d=gd
        if (gd > 100):
            a.d=100

        if (gd < 0):
            a.d=0
    else:
        print("enter a valid number from 1-100")

    return a

def decide(decisions):
    prioritii = []
    l=len(decisions)
    aki = 0
    for i in range(0,l-1):
        prioritii.append(priority(decisions[i]))

    maxxx = max(prioritii)

    for j in range(0,l-1):
        if prioritii[j] == maxxx:
            aki = j
    return aki

def shinterminal():
    decisions = []
    flagd=True
    while(flagd):
        adapoda = input(">>>")
        if adapoda=="stop" :
            print("exiting this program , soyanara senpai")
            flagd=False

        if adapoda == "help":
            help()

        if adapoda=="mk_dec" :
            t=mk_decision()
            decisions.append(t)

        if adapoda=="dis_dec":
              for i in range(0, len(decisions) ):
                    print(decisions[i].name)
                    print(decisions[i].h)
                    print(decisions[i].f)
                    print(decisions[i].s)
                    print(decisions[i].a)
                    print(decisions[i].su)
                    print(decisions[i].d)


        if adapoda=="decide":
             asi = decide(decisions)
             print(decisions[asi].name)


        if adapoda=="h" :
             h()

        if adapoda == "f":
             f()

        if (adapoda == "s"):

            s()

        if (adapoda == "a"):

            a()

        if (adapoda == "su"):

            su()

        if(adapoda == "d"):

            d()
    #--------------------------------------------------------------------------------------------------------------------
        if(adapoda =="ht"):

            ht()

        if(adapoda == "ft"):

            ft()

        if (adapoda == "st"):

            st()

        if (adapoda == "at"):

            at()

        if (adapoda == "sut"):

            sut()

        if (adapoda == "dt"):

            dt()

def priority(decisions):
     priority_value = 0

     eh=ha.pop()+decisions.h
     if eh>100 :
         eh=100
     th= hat.pop()

     if eh >= th:
         priority_value += ((eh-th)/100)+1

     if eh<th :
         priority_value += (th-eh)/100

#------------------------------------------s----------------------------

     es=sa.pop()+decisions.s
     ts= sat.pop()
     if es >= ts:
         priority_value += ((es-ts)/100)+1

     if es<ts :
         priority_value += (ts-es)/100

#--------------------------------------------f----------------------------


     ef=fe.pop()+decisions.f
     tf= fet.pop()
     if ef >= tf:
         priority_value += ((ef-tf)/100)+1

     if ef<tf :
         priority_value += (tf-ef)/100

 #---------------------------------------------a------------------------

     ea=an.pop()+decisions.a
     ta= ant.pop()
     if ea >= ta:
         priority_value += ((ea-ta)/100)+1

     if ea<ta :
         priority_value += (ta-ea)/100

#-------------------------------------su--------------------------------
     esu = sur.pop()+decisions.su
     tsu= surt.pop()
     if esu >= tsu:
         priority_value += ((esu-tsu)/100)+1

     if esu<tsu :
         priority_value += (tsu-esu)/100

#-------------------------------d-----------------------------------------

     ed=di.pop()+decisions.d
     td= dit.pop()
     if ed >= td:
         priority_value += ((ed-td)/100)+1

     if ed<td :
         priority_value += (td-ed)/100


     return priority_value



def help():
    print("my name is rin agasthu a decision making algorithm \n "
          "here are your basic commands \n"
          "h - to update your happiness \n"
          "s - to update your sadness\n"
          "f - to update your fear\n"
          "a - to update your angry \n"
          "su- to update your surprise\n"
          "d - to update your disgust\n"
          "ht - to update your happiness tolerance \n"
          "st - to update your sadness tolerance \n"
          "ft - to update your fear tolerance  \n"
          "at - to update your angry tolerance  \n"
          "sut- to update your surprise tolerance  \n"
          "dt - to update your disgust tolerance  \n"
          "mk_dec - to make a dec \n"
          "dis_dec - to display all your dec    \n"
          "decide - decide from your prev decisions  \n"
          "stop - to exit the program\n"
          "help- to call help\n")

#welcome message
print("welcome iam rin agasthu ... a desicision making bot made by akash k tesla"
      "\n these are your basic commands " )
help()
shinterminal()




