import random
import time
import os

# Console clear commands:   
# os.system("clear")  Linux - OSX
# os.system("cls")  Windows


#Start game code

print("*****WELCOME TO THE DUNGEON OF (G)ECHOES*****")
print()

#Lists for rooms & creatures
roomadj = ('freezing cold','very warm','damp and wet','almost too dark to see anything')
creatures = ('goblin','huge rat','giant spider')

#Dictionary for the user's info
userstats = {'Name': '','HP': 10,'Gold': 0, 'Weapon': ''}


#Get user input for name & weapon, clean it up, update dict
tempname = input("What is your name, adventurer?  ")
userstats['Name'] = str(tempname).upper().strip()
print()
print("And what weapon are you carrying today?")
tempweap = input("I have a :  ")
userstats['Weapon'] = str(tempweap).lower().strip()

print()
userchoice = input("Are you ready to begin, " + str(userstats['Name']) + "? Yes or No:  ")


#Combat function, pass in the random creature, the userstats dictionary
def combat(fightwhat,userstats):
    #initialize turn counter
    turncount = 0
    #Assign creature random number of hit points
    creaturehit = random.randint(3,9)
    #Begin combat while loop, controlled by user hit points
    while userstats['HP'] >= 1:
        #update turn counter
        turncount = turncount + 1
        print()
        print("-------Round " + str(turncount) + "-------")
        print("Your hit points: " + str(userstats['HP']))
        #User combat turn, programmed to auto-hit creature
        print("You attack the " + fightwhat + " with your " + userstats['Weapon'] + ".")
        time.sleep(1)
        #Random damage amount calculated & creature hit points updated
        damage1 = random.randint(1,4)
        print("You do " + str(damage1) + " damage.")
        creaturehit = creaturehit - damage1
        time.sleep(1)
        #Check to see whether creature is still "alive" or not
        if creaturehit >= 1: #If creature is alive, start creature combat turn
            #Creature combat turn, programmed to randomly hit or miss
            print("The " + fightwhat + " attacks.")
            time.sleep(1)
            #Coin flip to hit or miss
            attacksuccess = random.randint(1,2)
            if attacksuccess == 1: #If attack is successful, calculate random damage and update user HP
                damage2 = random.randint(1,4)
                print("The " + fightwhat + " hurts you for " + str(damage2) + " damage.")
                userstats['HP'] = userstats['HP'] - damage2
            else: #If attack is unsuccessful, begin the next round of combat
                print("The " + fightwhat + " missed you!")
        else: #If creature is not alive, end combat
            print("You killed the " + fightwhat + "! Hooray!")
            #Loot drop, random amount
            golddrop = random.randint(1,5)
            #Update user dictionary loot amount
            userstats['Gold'] = userstats['Gold'] + golddrop
            print("It drops " + str(golddrop) + " gold!")
            return #hitpts #return HP at the end of combat to createroom function
    return #hitpts #while loop not entered if HP < 1, return to createroom function



#Declare while loop control variable
userchoice = ''

#Begin main game while loop
while userchoice.lower() != 'no':
    #Clear the console
    os.system("cls")
    #Create room fuction, pass in the userstats dictionary
    def createroom(userstats):
        #Print user stats at top of the screen
        print("    " + userstats['Name'] + "   |  Weapon: " + userstats['Weapon'] + "  |  HP: " + str(userstats['HP']) + "  |  Gold: " + str(userstats['Gold']))
        #Update user hit points in dictionary to pass in to combat function
        #HP = userstats['HP']
        #assign random room description and random creature encounters
        room = str(roomadj[random.randint(0,3)])
        size = str(random.randint(10,30))
        fightwhat = str(creatures[random.randint(0,2)])
        print("----------------------------------------------------------")
        print()
        print("You walk into the room. It is " + room + "..." )
        time.sleep(1)
        print("It looks like it is " + size + " feet to the far wall with the next door.")
        time.sleep(1)
        print("There is a " + fightwhat + " in the room!")
        time.sleep(1)
        print()
        #Begin combat decision tree with user decision
        fightchoice = input("Do you attack? Yes or No: " )
        if fightchoice.lower() == 'yes': # If the user choses to fight...
            #combat function call, pass in HP, random creature, and userstats dict: updated HP is returned & assigned
            combat(fightwhat,userstats)
            if userstats['HP'] >= 1: #If the user has 1 or more hit point, they may continue
                print()
                #Ask user if they want to continue...if yes, while loop continues
                return input('Do you want to walk into the next room? Yes or No:  ')
            else: #If user does not have 1 or more hit points, they are kicked out of combat function & game ends
                print()
                print("You are too weak to keep fighting and run away.")
                keepgoing = 'no'
                return keepgoing #update userchoice to end the while loop
        else: #update userchoice to end the while loop
            print("You decide you are done adventuring for today.")
            return fightchoice
    #create room function call, pass in userstats dict, update control value to continue or end while loop 
    userchoice = createroom(userstats)

#End while loop

#Game is over, say goodbye to user
time.sleep(1)
print()        
print()
print("----------------GAME OVER---------------")
print()
print('Goodbye!')
time.sleep(5)

#End game code

