import random
import time
import os
     
    # os.system("clear")  Linux - OSX
    # os.system("cls")  Windows

#Dungeon room creator

print("*****WELCOME TO THE DUNGEON OF (G)ECHOES*****")
print()

roomadj = ('freezing cold','very warm','damp and wet','almost too dark to see anything')
creatures = ('goblin','huge rat','giant spider')
userstats = {'Name': '','HP': 10,'Gold': 0, 'Weapon': ''}

tempname = input("What is your name, adventurer?  ")
userstats['Name'] = str(tempname).upper().strip()
print()
print("And what weapon are you carrying today?")
tempweap = input("I have a :  ")
userstats['Weapon'] = str(tempweap).lower().strip()

userchoice = ''
gamechoice = ''

print()
userchoice = input("Are you ready to begin, " + str(userstats['Name']) + "? Yes or No:  ")

def combat(hitpts,fightwhat,userstats):
    turncount = 0
    creaturehit = random.randint(3,9)
    while hitpts >= 1:
        turncount = turncount + 1
        print()
        print("-------Round " + str(turncount) + "-------")
        print("Your hit points: " + str(hitpts))
        print("You swing your " + userstats['Weapon'] + " at the " + fightwhat)
        time.sleep(1)
        damage1 = random.randint(1,4)
        print("You do " + str(damage1) + " damage.")
        creaturehit = creaturehit - damage1
        time.sleep(1)
        if creaturehit >= 1:
            print("The " + fightwhat + " attacks.")
            time.sleep(1)
            attacksuccess = random.randint(1,2)
            if attacksuccess == 1:
                damage2 = random.randint(1,4)
                print("The " + fightwhat + " hurts you for " + str(damage2) + " damage.")
                hitpts = hitpts - damage2
            else:
                print("The " + fightwhat + " missed you!")
        else:
            print("You killed the " + fightwhat + "! Hooray!")
            golddrop = random.randint(1,5)
            userstats['Gold'] = userstats['Gold'] + golddrop
            print("It drops " + str(golddrop) + " gold!")
            return hitpts
    return hitpts


while userchoice.lower() != 'no':
    os.system("cls")
    def createroom(userstats):
        print("    " + userstats['Name'] + "   |  Weapon: " + userstats['Weapon'] + "  |  HP: " + str(userstats['HP']) + "  |  Gold: " + str(userstats['Gold']))
        HP = userstats['HP']
        room = str(roomadj[random.randint(0,3)])
        size = str(random.randint(10,30))
        fightwhat = str(creatures[random.randint(0,2)])
        print("-----------------------------------------------------")
        print()
        print("You walk into the room. It is " + room + "..." )
        time.sleep(1)
        print("It looks like it is " + size + " feet to the far wall with the next door.")
        time.sleep(1)
        print("There is a " + fightwhat + " in the room!")
        time.sleep(1)
        print()
        fightchoice = input("Do you attack? Yes or No: " )
        if fightchoice.lower() == 'yes':
            userstats['HP'] = combat(HP,fightwhat,userstats)
            if userstats['HP'] >= 1:
                print()
                return input('Do you want to walk into the next room? Yes or No:  ')
            else:
                print()
                print("You are too weak to keep fighting and run away.")
                keepgoing = 'no'
                return keepgoing
        else:
            print("You decide you are done adventuring for today.")
            return fightchoice
        
    userchoice = createroom(userstats)
time.sleep(1)
print()        
print()
print("----------------GAME OVER---------------")
print()
print('Goodbye!')
time.sleep(5)
