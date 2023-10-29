#Modules used:
   #Test display speed
import sys
from time import sleep
from tkinter import *     #importing everything from tkinter
root=Tk()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#global variable ini.
global floor
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#variable ini.
x=""     #variable for buttons and their functions
floor=1
r=0   #right
l=0   #left
u=0   #up
d=1   #down
b=1   #turn back
i=0   #inspect
j=0   #jump
e=None   #exit

file_name="F1T2Da.txt"       #file_name="F"+str(position["floor"])+"T"+str(position["door type"])
file_name_open="openF1T2Da.txt"           #open + file_name 
file_object=open(file_name,"r")                #file object 
file_object_open=open(file_name_open,"r")          #file object open     
file_bin=None           #file bin
door_question=file_object.readline()          #door question
file_bin=file_object.readline()
door_answer=int(file_object.readline())          #door answer
file_bin=file_object.readline()
possible_moves=file_object.readline()          #possible moves
file_bin=file_object.readline()
door_view=file_object.read()          #door view
file_bin=file_object.readline()
door_answer=int(file_object.readline())     #door answer
possible_moves_open=file_object_open.readline()    #possible moves open
file_bin=file_object.readline()
door_view_open=file_object_open.read()   #door view open
      
user_answer=None        


door=[0,1,0,0,0,0,0]
hatch=[0,1,0,0]      #floor 1,5=0 ; floor 2,3,4=0 or 1
d_i=[0,0]

position={"floor":1,"door type":2,"door number":0} # outer=1 inner=2 hatches=3 door close-up=4
door_cycle={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
door_cycle_keys=[]
door_cycle_values=[]
door_cycle_position=None
column=[1,1,2]       #index 0: number of floors ; index 1: starting floor (SF) ; index 2: ending floor (EF) ; column name: <big>,<small> column
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Game starts
def game_start():
    print('Welcome To...')
    print('''████████╗██╗░░██╗███████╗  ████████╗░█████╗░░██╗░░░░░░░██╗███████╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ╚══██╔══╝██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗
░░░██║░░░███████║█████╗░░  ░░░██║░░░██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝
░░░██║░░░██╔══██║██╔══╝░░  ░░░██║░░░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║███████╗  ░░░██║░░░╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝''' )
    emptyinput=input("press any key to continue".center(225))
    game_turn()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
def bg_story(x):             #0:main story ; 1:outer door ; 2:inner door ; 3:floor hatch ; 5:wrong answer ; 6:game end ; 7:inspecting function keyboard
    print("bg story")        #stand in text 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Help
def help():
    print("The possible directions of a place are displayed under each image.")
    print("\nCode:")
    print("r is right \n l is left \n u is up \n d is down \n b is turn back \n i is inspect \n j is jump \n e is exit")
    print("\nPress enter to continue")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Door Management
def door_management(x):     #0:d to h and h to d; 1: door cycles
    if x==0:                #d to h and h to d
        if door[0]==0:
            door[0]=1
            hatch[0]=0
        else:
            hatch[0]=1
            door[0]=0
    else:                    #door cycles
        door_cycle["a"]=(door_cycle["a"]%6)+1
        door_cycle["b"]=(door_cycle["b"]%6)+1
        door_cycle["c"]=(door_cycle["c"]%6)+1
        door_cycle["d"]=(door_cycle["d"]%6)+1
        door_cycle["e"]=(door_cycle["e"]%6)+1
        door_cycle["f"]=(door_cycle["f"]%6)+1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def door_cycle():
    door_cycle_keys=list(door_cycle.keys())
    door_cycle_values=list(door_cycle.values())
    door_cycle_position=door_cycle_keys[door_cycle_values.index[position["door number"]-1]]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def position_display():
    file_name="F"+str(position["floor"])+"T"+str(position["door type"])
    if position["door type"]==1:             #outer doors
        door_cycle()
        file_name+="D"+door_cycle_position+".txt"
        r,l,u,d,b,i,j=1,1,0,1,1,1,0
        file_object=open(file_name,"r")
        door_question=file_object.readline()
        file_bin=file_object.readline()
        door_answer=int(file_object.readline())
        file_bin=file_object.readline()
        possible_moves=file_object.readline()
        file_bin=file_object.readline()
        door_view=file_object.read()
        file_name_open="open"+file_name
        file_object_open=open(file_name_open,"r")
        door_view_open=file_object_open.read()
            
    elif position["door type"]==2:         #inner door
        file_name+="D"+door_cycle_position+".txt"
        r,l,u,d,b,i,j=0,0,0,1,1,1,0
        file_object=open(file_name,"r")
        door_question=file_object.readline()
        file_bin=file_object.readline()
        door_answer=int(file_object.readline())
        file_bin=file_object.readline()
        possible_moves=file_object.readline()
        file_bin=file_object.readline()
        door_view=file_object.read()
        file_name_open="open"+file_name
        file_object_open=open(file_name_open,"r")
        door_view_open=file_object_open.read()
            
    elif position["door type"]==3:      #hatches
        file_name+="D"+str(position["door number"])+".txt"
        r,l,u,d,b,i,j=1,1,1,0,0,1,0
        file_object=open(file_name,"r")
        door_question=file_object.readline()
        file_bin=file_object.readline()
        door_answer=int(file_object.readline())
        file_bin=file_object.readline()
        possible_moves=file_object.readline()
        file_bin=file_object.readline()
        door_view=file_object.read()
        file_name_open="open"+file_name
        file_object_open=open(file_name_open,"r")
        door_view_open=file_object_open.read()
            
    else:              #door close up
        #file_name+="D"+str(position["door number"])+".txt"
        r,l,u,d,b,i,j=0,0,0,0,1,0,0
        #file_object=open(file_name,"r")
        #door_question=file_object.readline()
        #file_bin=file_object.readline()
        #door_answer=int(file_object.readline())
        #file_bin=file_object.readline()
        #possible_moves=file_object.readline()
        #file_bin=file_object.readline()
        #door_view=file_object.read()
        #file_name_open="open"+file_name
        #file_object_open=open(file_name_open,"r")
        #door_view_open=file_object_open.read()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Floor Change Function #0:main story ; 1:outer door ; 2:inner door ; 3:floor hatch ; 5:wrong answer ; 6:game end
def floor_change():
    if position["door type"]==2:
        if position["floor"]==1:
            position["floor"]=5
        else:
            position["floor"]=1
    elif position["door type"]==3:
        position["floor"]=column[2]
        column[1],column[2]=column[2],column[1]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Button functions
def one():
     global x
     x+="1"
     DISPLAY()

def two():
     global x
     x+="2"
     DISPLAY()

def three():
     global x
     x+="3"
     DISPLAY()

def four():
     global x
     x+="4"
     DISPLAY()

def five():
     global x
     x+="5"
     DISPLAY()

def six():
     global x
     x+="6"
     DISPLAY()

def seven():
     global x
     x+="7"
     DISPLAY()

def eight():
     global x
     x+="8"
     DISPLAY()

def nine():
     global x
     x+="9"
     DISPLAY()

def zero():
     global x
     x+="0"
     DISPLAY()
 
def BACKSPACE():
     global x
     length=len(x)-1
     x=x[0:length]
     DISPLAY()

def ENTER():
     global x
     global door_answer
     door_answer=x
     x=""
     root.destroy()

def DISPLAY():
     label=Label(root, text=x)
     label.grid(row=0, column=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Inspect function for the buttons
def INSPECT():
    button1=Button(root, text="1", command=one, padx=35, pady=10)
    button1.grid(row=1, column=0)

    button2=Button(root, text="2", command=two, padx=35, pady=10)
    button2.grid(row=1, column=1)

    button3=Button(root, text="3", command=three, padx=35, pady=10)
    button3.grid(row=1, column=2)

    button4=Button(root, text="4", command=four, padx=35, pady=10)
    button4.grid(row=2, column=0)

    button5=Button(root, text="5", command=five, padx=35, pady=10)
    button5.grid(row=2, column=1)

    button6=Button(root, text="6", command=six, padx=35, pady=10)
    button6.grid(row=2, column=2)

    button7=Button(root, text="7", command=seven, padx=35, pady=10)
    button7.grid(row=3, column=0)

    button8=Button(root, text="8", command=eight, padx=35, pady=10)
    button8.grid(row=3, column=1)

    button9=Button(root, text="9", command=nine, padx=35, pady=10)
    button9.grid(row=3, column=2)

    button0=Button(root, text="0", command=zero, padx=35, pady=10)
    button0.grid(row=4, column=1)

    buttonenter=Button(root, text="enter", command=ENTER, padx=25, pady=10)
    buttonenter.grid(row=4, column=0)

    buttonbackspace=Button(root, text="backspace", command=BACKSPACE, padx=10, pady=10)
    buttonbackspace.grid(row=4, column=2)

    root.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
def game_end(TYPE=None,SPECIFICATION=None):      #(type, specification); TYPES: j:jump ; e:exit ; SPECIFICATION: >>j:: a,b,c,d,e,f ;    
    print("ending sequence") #please finish!!!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def jump():
    choice3=input("Select key to continue")
    choice3=choice3.lower()
    if choice3=="j":
        end_game("j",door_cycle_position)
    elif choice3=="b":
        game_turn()
    elif choice3=="e":
        e=input("Are you sure you want to exit? Your progress will not be saved (Y/N)")
        if e.upper()=="Y":
            game_end()
        else:
            jump()
    else:
        print("incorrect response")
        jump()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Game Turn Starts
def game_turn():
    print(door_view)
    print("\n"+possible_moves)
    print("\n\n")
    choice2=input("Select key to continue")
    choice2=choice2.lower()
    
    if choice2=="r":
        if r==0:         #move right
            print("I can not move right")
            game_turn()
        if r==1:
            if position["door type"]==1:
                door[position["door number"]]=0
                position["door number"]=(position["door number"]%6)+1
                door[position["door number"]]=1
                position_display()
                game_turn()
            else:
                hatch[position["door number"]]=0
                if position["floor"]==1 or position["floor"]==5:
                    position["door number"]=(position["door number"]%2)+1
                    if column[1]==1:
                        if column[2]==2:
                            column[2]=3
                            column[0]=2
                        else:
                            column[2]=2
                            column[0]=1
                    else:
                        if column[2]==4:
                            column[2]=3
                            column[0]=2
                        else:
                            column[2]=4
                            column[0]=1
                else:
                    position["door number"]=(position["door number"]%3)+1
                    if position["floor"]==2:
                        if column[2]==1:
                            column[2]=3
                        elif column[2]==3:
                            column[2]=4
                            column[0]=2
                        else:
                            column[2]=1
                            column[0]=1
                    elif position["floor"]==3:
                        if column[2]==2:
                            column[2]=1
                            column[0]=2
                        elif column[2]==1:
                            column[2]=4
                            column[0]=1
                        elif column[2]==4:
                            column[2]=5
                            column[0]=2
                        else:
                            column[2]=2
                            column[0]=1
                    else:
                        if column[2]==3:
                            column[2]=5
                        elif column[2]==5:
                            column[2]=2
                            column[0]=2
                        else:
                            column[2]=3
                            column[0]=1
                hatch[position["door number"]]=1
                #column_change()
                position_display()
                game_turn()
                
    elif choice2=="l":         #move left
        if l==0:
            print("I can not move left")
            game_turn()
        if l==1:
            if position["door type"]==1:
                door[position["door number"]]=0
                if position["door number"]==1:
                    position["door number"]=6
                    door[position["door number"]]=1
                else:
                    position["door number"]=(position["door number"]-1)
                    door[position["door number"]]=1
                position_display()
                game_turn()
            else:
                hatch[position["door number"]]=0
                if position["floor"]==1 or position["floor"]==5:
                    position["door number"]=(position["door number"]%2)+1
                    if column[1]==1:
                        if column[2]==2:
                            column[2]=3
                            column[0]=2
                        else:
                            column[2]=2
                            column[0]=1
                    else:
                        if column[2]==4:
                            column[2]=3
                            column[0]=2
                        else:
                            column[2]=4
                            column[0]=1
                else:
                    if position["door number"]==1:
                        position["door number"]=3
                        hatch[position["door number"]]=1
                    else:
                        position["door number"]=(position["door number"]-1)
                        hatch[position["door number"]]=1
                    if position["floor"]==2:
                        if column[2]==1:
                            column[2]=4
                            column[0]=2
                        elif column[2]==3:
                            column[2]=1
                        else:
                            column[2]=3
                            column[0]=1
                    elif position["floor"]==3:
                        if column[2]==2:
                            column[2]=5
                            column[0]=2
                        elif column[2]==1:
                            column[2]=2
                            column[0]=1
                        elif column[2]==4:
                            column[2]=1
                            column[0]=2
                        else:
                            column[2]=4
                            column[0]=1
                    else:
                        if column[2]==3:
                            column[2]=2
                            column[0]=2
                        elif column[2]==5:
                            column[2]=3
                        else:
                            column[2]=5
                            column[0]=1
                hatch[position["door number"]]=1 
                position_display()
                game_turn()
                
    elif choice2=="u":           #see up
        if u==0:
            print('There is nothing to see up')
            game_turn()
        else:
            door_management(0)
            hatch[0]=0
            if d_i[0]==1:
                position["door number"]=door.index(1)
                position["door type"]==1
            else:
                position["door type"]==2
            position_display()
            game_turn()
            
    elif choice2=="d":            #see down
        if d==0:
            print('There is nothing to see down')
            game_turn()
        else:
            door_management(0)
            if position["door type"]==1:
                d_i[0],d_i[1]=1,0
            else:
                d_i[0],d_i[1]=0,1
            position["door type"]=3
            position["door number"]=hatch.index(1)
            position_display()
            game_turn()
            
    elif choice2=="b":          #turn back
        if b==0:
            print("I can not turn back")
            game_turn()
        else:
            if d_i[0]==1:
                position["door type"]=2
            else:
                position["door type"]=1
            position_display()
            game_turn()
            
    elif choice2=="i":        #inspect  
        if i==0:
            print("There is nothing to inspect")
            game_turn()
        else:
            position_display()
            print(door_question)
            INSPECT()
            bg_story(7)
            if user_answer==door_answer:
                if position["door type"]==1:
                    print(door_view_open) 
                    bg_story(1)
                    print(possible_moves_open)
                    print("\n"+possible_moves_open)
                    print("\n\n")
                    jump()
                elif position["door type"]==2:
                    print(door_view_open)
                    bg_story(2)
                    if door_cycle_position=="a":
                        floor_change()
                elif position["door type"]==3:
                    print(door_view_open)
                    bg_story(3)
                    floor_change()
            else:
                bg_story(5)
            game_turn()

    elif choice2=="e":      #exit
        e=input("Are you sure you want to exit? Your progress will not be saved (Y/N)")
        if e.upper()=="N":
            game_turn()
        else:
            print("**exiting game**")
            print("***game exited***")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Body:  #0:main story ; 1:outer door ; 2:inner door ; 3:floor hatch ; 5:wrong answer ; 6:game end
game_start()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


     






     




     



     


     


