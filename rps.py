print("RPS Game Created By: Mohonrey")
print("1: play")
print("2: exit")
isPlayerPick = "False"

while isPlayerPick == "False" :
    try :
        playerChoice = int(input())

        if playerChoice >= 3 :
            isPlayerPick = "False"
            print("Please Enter 1 or 2 number only!")
        else :
            isPlayerPick = "True"
    except :
        print("Invalid! Please type 1 or 2 only")
        isPlayerPick == "False"

# print("The is Choosing", playerChoice)
play = "False"

if playerChoice == 1 :
    play = "True"
else :
    print("Exit Successfully!")

if play == "True" :
    # print("Lets play")
    print("                   ")
    print("Please Enter your name")
    playerName = input("Name: ")

    # This is to set Default Player name if player decide not to type anything
    if playerName == "" :
        #This is the player default name
        playerName = "Player 1"

    playerSetName = playerName

    #This is to determine if Player Type his name or not!
    if playerSetName == "Player 1" :
        #A simple Greet if player decide not to type his name
        print("                   ")
        print("Hello",playerSetName,"My name is Mohonrey! you didn't say your name But it's fine")
    else :
        #A simple Greet if player decide to type his name
        print("                   ")
        print("Hello",playerSetName,"Welcome to my game my name is Mohonrey!")

    #This is when player decide to type invalid keywords
    invalid = "True"

    while invalid == "True":
        #A simple instruction for Players
        print("Let's play RPS Game")
        print("1:Rock")
        print("2:Paper")
        print("3:Scissors")
        
        #This is to check if Player Type the right numbers 
        rounds = 1
        humanScore = 0
        botScore = 0

        while rounds <= 5 :
            
            try :
                humanPick = int(input())

                #This is if Player Decide to type number more than 3
                if humanPick >= 4 :
                    print(playerSetName,"Enter 1,2 or 3 number not", humanPick,"Do you Understand?")
                    invalid = "True"
                else :
                    invalid = "False"

                    # print("This is What player Pick", humanPick)
                    if humanPick == 1 :
                        print("                   ")
                        print("------------------------------------------- Round",rounds,"------>")
                        print(playerSetName, "pick number 1 : Rock")
                    if humanPick == 2 :
                        print("                   ")
                        print("------------------------------------------- Round",rounds,"------>")
                        print(playerSetName, "pick number 2 : Paper")
                    if humanPick == 3 :
                        print("                   ")
                        print("------------------------------------------- Round",rounds,"------>")
                        print(playerSetName, "pick number 3 : Scissors")

                    #Create Random Generator For Bot
                    import random 
                    botChoice = random.randint(1, 3)

                    if botChoice == 1 :
                        print("Bot pick number", botChoice, ":", "Rock")
                    if botChoice == 2 :
                        print("Bot pick number", botChoice, ":", "Paper")
                    if botChoice == 3 :
                        print("Bot pick number", botChoice, ":", "Scissors")

                    #Rules for Rock
                    if humanPick == 1 and botChoice == 1 :
                        print("Draw")
                    if humanPick == 1 and botChoice == 2 :
                        print("You Loss!")
                        botScore += 1
                    if humanPick == 1 and botChoice == 3 :
                        print("You Win!")
                        humanScore += 1

                    #Rules for Paper
                    if humanPick == 2 and botChoice == 1 :
                        print("You Win!")
                        humanScore += 1
                    if humanPick == 2 and botChoice == 2 :
                        print("Draw")
                    if humanPick == 2 and botChoice == 3 :
                        print("You Loss!")
                        botScore += 1

                    #Rules for Scissors
                    if humanPick == 3 and botChoice == 1 :
                        print("You Loss!")
                        botScore += 1
                    if humanPick == 3 and botChoice == 2 :
                        print("You Win!")
                        humanScore += 1
                    if humanPick == 3 and botChoice == 3 :
                        print("Draw")

                    rounds += 1
            except :
                print("Hey",playerSetName,"Type 1,2 or 3 number only!")
                invalid = "True"

            if rounds == 6 :
                print("                   ")
                print("-------( Final Score )-------")
                print(playerSetName,"Score:",humanScore)
                print("Bot Score:",botScore)

                if humanScore < botScore and humanScore != botScore :
                    print("You Loss Sorry")
                if humanScore > botScore and humanScore != botScore :
                    print("You Win Congrats")
                if humanScore == botScore :
                    print("It's a Draw")

            #This is for if player want to continue or not
            while rounds == 6 :
                print("                   ")
                print("////////////////////////////////////////////////////////")
                print("Do you Want to play more or Exit?")
                print("1: Play more")
                print("2: Exit")

                try :
                    con = int(input())

                    if con >= 3 :
                        print("Please Enter 1 or 2")
                    if con == 1 :
                        rounds = 1
                        print("                   ")
                        print("---------------------------------------------------------->")
                        print("Okay Let's Continue Pick 1,2 or 3 number")
                        print("1:Rock")
                        print("2:Paper")
                        print("3:Scissors")
                        humanScore = 0
                        botScore = 0
                    if con == 2 :
                        rounds = 10
                except :
                    print("Invalid keyword!")
print("                   ")
print("//////////////////////////////////////////////////////////")
print("-----(Thanks for playing my simple game)-----")
print("                   ")
print("-----(By: Mohonrey - Dec 1, 2023)-----")
input("Hit Enter ")