import random
import turtle
from turtle import *
setup(500, 500)
Screen()
title("Turtle Keys")
move = Turtle()
showturtle()


grid=[]
moles=[]
mallet=()

#Creating the Game

def create_game():
    global grid
    global moles
    global mallet
 #Making the major components of the game global variables
    

    t = turtle.Turtle()
    dot_distance = 80
    width = 5
    height = 5
    t.penup()
#Giving the grid it's dimensions


    for y in range (height):
        for i in range (width):
            t.dot()

            t.forward(dot_distance)
        t. backward(dot_distance *width)
        # point cursort down
        t.right(90)
        # point cursor to right
        t.forward (dot_distance)
        t.left(90)

    #Setting up the 5x5 grid



    for row in [0,80,160,240,320]:
        for column in [0,-80,-160,-240,-320]:
            point = (row, column)
            grid.append(point)
    a = list(grid)
#Making the rows by counting by +80 and making the columns by counting down by -80



    for i in range(0,9):
        point = a.pop(random.randint(0,len(a)-1))
        t.goto(point)
        t.dot(20,'red')
        moles.append(point)
#Out of the 25 dots, I am trying to make 9 of them red



    for i in range(0,1):
        point = a.pop(random.randint(0,len(a)-1))
        t.goto(point)
        t.dot(20,'blue')
        global mallet
        mallet = point
# Out of the 25 dots, I am trying to make only one blue


    for i in range(0,15):
        point = a.pop(random.randint(0,len(a)-1))
        t.goto(point)
        t.dot(20,'black')
#Out of the 25 dots, I am trying to make 15 black

    return t
        
def rand_coord():
 
    l=[0,80,160,240,320]
    z=[0,-80,-160,-240,-320]
    x=random.choice(l)
    y=random.choice(z)
    return (x,y)
   #Setting up the rand_coord function by using the same list used for rows/columns 
    



def compare (t1,t2):
    if t1[0]==t2[0] and t1[1]==t2[1]:
         return 1
    else:
        return 0

#Comparing mole and mallet positions

def make_mole(t):
    mallet_position=rand_coord()
    mole_position=rand_coord()
  #Setting up random positions for the mallot and moles

    while True:
        if compare(mallet_position,mole_position)==0 and mole_position not in moles:
            moles.append(mole_position)
            t.goto(mole_position)
            t.dot(20,'red')
            break

#Putting the moles as red and making sure that when a red dot is hit then it goes away

    

def move(t,direc):
    global mallet
    global grid
    global moles
    
    #For this new function, I am displaying the global variables again
    
    if direc==90:
        new_mallet = (mallet[0], mallet[1]+80)
    if direc==180:
        new_mallet= (mallet[0]-80,mallet[1])
    if direc==270:
        new_mallet= (mallet[0],mallet[1]-80)
    if direc==360:
        new_mallet= (mallet[0]+80,mallet[1])
#Setting up the directions for the mallet. 



    if new_mallet in moles:
        i=moles.index(new_mallet)
        print 'i=',i
       
        if i>-1:
            moles.pop(i)
#Now since user will be controlling the mallet, I am setting up the new mallet positions



    a = list(grid)

    for i in range(0,25):
        point = a[i]
        t.goto(point)
        t.dot(20,'black')

#making sure 15 of the dots are black
        


    for i in range(0,1):
        point = new_mallet
        t.goto(point)
        t.dot(20,'blue')
#making sure 1 of the dots is blue and that the blue dot is the cursor

        


    for i in range(0,len(moles)):
        point = moles[i]
        t.goto(point)
        t.dot(20,'red')
#Making sure that if a red dot is eliminated by the user then that is accounted for


    mallet=new_mallet


def k1():
    move(t,90)

def k2():
    move(t,180)

def k3():
    move(t,360)

def k4():
    move(t,270)

   #Defining the directions using angle degrees

    
t=create_game()            



onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
listen()
mainloop()

#making the directions for the user. The movements are labeled with angle degrees
