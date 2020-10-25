"""
this is a decision making algo by calculating emotions of current state with future state
total human emotions
in 2020 according to a study there are total of 27 emotions
since it is for a simple assignnment in this algo we are calculating main 6 algorithms
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
h=[]      #happiness
s=[]      #sadness
f=[]      #fear
a=[]      #anger
su=[]     #surprise
d=[]      #disgust

ht=[]      #happiness tolerance
st=[]      #sadness tolerance
ft=[]      #fear tolerance
at=[]      #anger tolerance
sut=[]     #surprise tolerance
dt=[]      #disgust tolerance

#---------------------------------------------------functions---------------------------------------------------

def h(g):
    if(g>0 and g<100):
        h.append(g)
    elif(g>100):
        h.append(100)
    elif(g<0):
        h.append(0)
    else:
        print("input a valid number from 1 - 100 ")

def s(g):
    if(g>0 and g<100):
        s.append(g)
    elif(g>100):
        s.append(100)
    elif(g<0):
        s.append(0)
    else:
        print("input a valid number from 1 - 100 ")

def f(g):
    if(g>0 and g<100):
        f.append(g)
    elif(g>100):
        f.append(100)
    elif(g<0):
        f.append(0)
    else:
        print("input a valid number from 1 - 100 ")

def a(g):
    if(g>0 and g<100):
        a.append(g)
    elif(g>100):
        a.append(100)
    elif(g<0):
        a.append(0)
    else:
        print("input a valid number from 1 - 100 ")

def su(g):
    if(g>0 and g<100):
        su.append(g)
    elif(g>100):
        su.append(100)
    elif(g<0):
        su.append(0)
    else:
        print("input a valid number from 1 - 100 ")

def d(g):
    if(g>0 and g<100):
        d.append(g)
    elif(g>100):
        d.append(100)
    elif(g<0):
        d.append(0)
    else:
        print("input a valid number from 1 - 100 ")

#----------------------------------------------------------------------------------------------------------------
def ht(g):
    if (g > 0 and g < 100):
        ht.append(g)
    elif (g > 100):
        ht.append(100)
    elif (g < 0):
        ht.append(0)
    else:
        print("input a valid number from 1 - 100 ")


def s(g):
    if (g > 0 and g < 100):
        st.append(g)
    elif (g > 100):
        st.append(100)
    elif (g < 0):
        st.append(0)
    else:
        print("input a valid number from 1 - 100 ")


def ft(g):
    if (g > 0 and g < 100):
        ft.append(g)
    elif (g > 100):
        ft.append(100)
    elif (g < 0):
        ft.append(0)
    else:
        print("input a valid number from 1 - 100 ")


def at(g):
    if (g > 0 and g < 100):
        at.append(g)
    elif (g > 100):
        at.append(100)
    elif (g < 0):
        at.append(0)
    else:
        print("input a valid number from 1 - 100 ")


def sut(g):
    if (g > 0 and g < 100):
        sut.append(g)
    elif (g > 100):
        sut.append(100)
    elif (g < 0):
        sut.append(0)
    else:
        print("input a valid number from 1 - 100 ")


def dt(g):
    if (g > 0 and g < 100):
        dt.append(g)
    elif (g > 100):
        dt.append(100)
    elif (g < 0):
        dt.append(0)
    else:
        print("input a valid number from 1 - 100 ")



#----------------------------first assignment---------------------------------
#happiness
htemp=input("how happy are you on 0-100%")
h(htemp)
#fear
ftemp=input("how feared are you on 0-100%")
f(ftemp)
#sadness
stemp=input("how sad are you on 0-100%")
s(stemp)
#angry
atemp=input("how angry are you on 0-100%")
a(atemp)
#surprise
sutemp=input("how surprised are you on 0-100%")
su(sutemp)
#disgust
dtemp=input("how disgusted are you on 0-100%")
d(dtemp)

#  emotion tolarance values intialization

#happiness tolarance
httemp=input("how happiness can  you tolerate on 0-100%")
ht(httemp)
#fear tolarance
fttemp=input("how fear can  you tolerate on 0-100%")
ft(fttemp)
#sadness tolarance
sttemp=input("how sadness can  you tolerate on 0-100%")
st(sttemp)
#angry tolarance
attemp=input("how angry can  you tolerate on 0-100%")
at(attemp)
#surprise tolarance
suttemp=input("how surprise can  you tolerate on 0-100%")
sut(suttemp)
#disgust tolarance
dttemp=input("how disgust can  you tolerate on 0-100%")
dt(dttemp)


#----------------------------finidhed assigneng for the first time-------------------------------------
# decision making function
def mk_decision():
    a = decision(110, 10, 10, 10, 10, 10)
    a.h = input(" how much happy this decision makes you")
    a.f = input("iout how much fear this decision makes you")
    a.s = input("iout how much sadness this decision makes you")
    a.a = input("iout how much angry this decision makes you")
    a.su.= input("iout how much surprise this decision makes you")
    a.d = input("iout how much disgust this decision makes you")
    return a

flagd=True
while(flagd):
    adapoda = input(">>>")
    if(adapoda=="s")


#welcome message
print("welcome iam rin agasthu ... a desicision making bot made by akash k tesla"
      "\n these are your basic commands " )

'''
(*&^%$@#$%^&*&^%$$%^&*(*&^%$%^&*(*&^%%^&*()(*&^%$%^&*()(*&^%$%^&*(*&^%$%^&*()(*&^%$$%^&*((*&^%$%^&*&$%^*&%^
----------------------------------                    ----------------------------------------



                        -----------------------------------------------
'''



#assign values
a=[]
flag=True
#input function
while(flag):
    temp= input("emotional input  ")
    a.append(temp)
    aki=True

    while(aki):
         asi = input("do you want to continue y/n  ")
         print(asi)
         if(asi=='y'):
             aki=False
             flag=True

         elif(asi=='n'):
             aki=False
             flag = False

         else:
             print("please give answers in y/n  ")

print(a)
decision(a.pop())