#Author:      Sam Kyle
#Class:   CIT 135-03
#Assignment: Quest Adventure
#Date Assigned:
#Due Date: 
#Description: QUEST
###
#Certification of Authenticity:  I certify that this is entirely my own work,
#except where I have given fully-documented references to the work of others.
#I understand the definition and consequences of plagiarism and acknowledge
#that the assessor of this assignment may, for the purpose of assessing
#this assignment: - Reproduce this assignment and provide a copy
#to another member of academic staff; and/or Communicate a copy
#of this assignment to a plagiarism checking service (which may then retain
#a copy of this assignment on its database for the purpose of
#future plagiarism checking)
###

import random

###########FUNCTIONS##########
def status(inventory,money,health):
    print ("Our hero has the following kit: ", inventory)
    print ("Our hero has the following financial resources: ")
    for typem in list(money):
        print(typem,":",money[typem])
    print ("Our hero has", health, "% health\n")
    return 1

def fetch(inventory, money, health):
    print("\nI am in the fetch quest\n")
    return inventory, money, health

def dragon(inventory, money, health):
    print("\nI am in the dragon quest\n")
    return inventory, money, health

def eow(inventory, money, health):
    print("\nI am at the end of the world quest\n")
    health=0
    return inventory, money, health


def blacksmith(inventory, money, health, quests):
    print("\nI am at the blacksmith quest\n")
    return inventory, money, health, quests

def escapeTheGuards(inventory, money, health, quests):
    print("\nI am at the escapeTheGuards quest\n")
    return inventory, money, health, quests

def toBlacksmith(inventory, money, health, quests):#remove the ', quests'
    print("In the escape from the sewer, our hero stumbles upon a figure hidden behind a thick glass partition with this to say: \n")
    if "broken sword" in inventory:
        print("Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe:\nAll mimsy were the borogoves, \nAnd the mome raths outgrabe.\n\nBeware the Jabberwock, my son!\nThe jaws that bite, the claws that catch!\nBeware the Jubjub bird, and shun\nThe frumious Bandersnatch!\nHe took his vorpal sword... \nThe vorpal swORD the voRPAL SWORD IS AT HAND ONCE AGAIN HEHEHEHAHAHEHEHE\n")
        print("Clearly the troubled old man had suffered a severe mental break... but out hero can't help but notice the sword in their backpack begins to weigh heavier and heavier as the old man speaks")
        decision=input("What does our hero decide to do?\n[Inspect] the broken sword or [Continue] down the path?")
    else:
        print("`Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe:\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.\n\nBeware the Jabberwock, my son!\nThe jaws that bite, the claws that catch!\nBeware the Jubjub bird, and shun\nThe frumious Bandersnatch!\n\nHe took his vorpal sword in hand:\nLong time the manxome foe he sought --\nSo rested he by the Tumtum tree,\nAnd stood awhile in thought.\n\nAnd, as in uffish thought he stood,\nThe Jabberwock, with eyes of flame,\nCame whiffling through the tulgey wood,\nAnd burbled as it came!\n\nOne, two! One, two! And through and through\nThe vorpal blade went snicker-snack!\nHe left it dead, and with its head\nHe went galumphing back.\n\nAnd, has thou slain the Jabberwock?\nCome to my arms, my beamish boy!\nO frabjous day! Callooh! Callay!\n'He chortled in his joy.\n\n`Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.")
        decision="Continue"              
    if decision=="Continue"or decision=="continue":
        print ("Our hero continues on their merry way out of the sewer and into the free world to live their life as normal... or so our hero thought... Until he ran into some of the same guards that imprisoned him...")
        quests= ["escapeTheGuards" if x=="toBlacksmith" else x for x in quests]#remove
    if decision=="Inspect"or decision=="inspect":
        print("\nOur hero inspects the sword and comes to realize small markings had begun to glow on the swords hilt. Our hero kept listening to the ramblings of the man all the while mesmerized by the broken sword in his hand. Soon overcome with annoyance at the man in the cell he stalked off, his ramblings of a blacksmith and the Jabberwocky still echoing in our hero's mind.")
        print("\nEventually our hero stumbles his way out of the maze like sewer in a small town that can't be too far away from Archet with the intentions of finding the closest blacksmith.")
        inventory =  ["prophetic sword" if x=="broken sword" else x for x in inventory]
        quests= ["blacksmith" if x=="toBlacksmith" else x for x in quests]#remove
    #print (quests)
    return inventory, money, health, quests#comment before the comma


##############MAIN#############
play=input("Welcome, want to play?\n(Y/N) ".lower())
hero=""
inventory=[]
money={'gold':0,'silver':0,'copper':0}
health=100
quests=["toBlacksmith"]#move to under engine
if hero=="" and play=="y":
    hero= input("Who is our Hero? ")
    print(hero, "is in a sewer, under the town Archet on the planet Mars.")
    print("It is very dark and", hero, "trips over a large wooden box.")
    askit=input("Should he open the box?(y/n) ").lower()
    if askit=='y':
        print("\nthe box contains ale, a healing potion, a broken sword, sneakers, a backpack and 3 gold coins\n")
        inventory=["ale",  "healing potion", "broken sword", "sneakers", "backpack"]
        money['gold']=money['gold']+3
        status(inventory, money, health)
    else:
        print ("\nYou are empty handed you fool")
    
while play=='y':#######game engine###,"fetch", "dragon", "eow"]  
    select=random.choice(quests)
    undertake=select + "(inventory, money, health, quests)"
    inventory, money, health, quests=eval(undertake)#remove quests from the previous two lines and add in the other quests
    if health<5:
        print("You are dying")
        if"healing potion" in inventory:
            health=100
            print("You are lucky to have had a healing potion")
            inventory.remove("healing potion")
        else:
            print ("You died")
    if play=='y':
        status(inventory, money, health)
        play=input("Would you like to play on?\n(Y/N) ").lower()







print("Thanks for playing")





















               
