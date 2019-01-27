import sys
def addroom():
    newroomname = input("What's the room's name? \n")
    newroomminadults = int(input("How many adults can sleep in this room at minimum? \n"))
    newroommaxadults = int(input("How many adults can sleep in this room at maximum? \n"))
    newroomminkids = int(input("How many kids can sleep in this room at minimum? \n"))
    newroommaxkids = int(input('How many kids can sleep in this room at maximum? \n'))
    newroombeds = int(input("How many beds are there? \n"))


def menu():
    print("[1] Restart")
    print("[2] Start the wizard")
    print("[3] Quit \n")
    menuchoice = int(input("What do you want to do? "))
    if  menuchoice == 1:
        menu()
    elif menuchoice == 2:
        print("\n")
        addroom()
    else:
        sys.exit()


menu()