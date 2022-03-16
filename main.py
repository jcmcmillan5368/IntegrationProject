# Jayce McMillan
# This is a population simulator where the success of your population is
# determined by your population start number, the amount of generations
# you input, and the random seed number you provide. The 5 digit seed
# number determines the diseases, triumphs, and game ending scenarios
# your population may or may not experience.
print("Hello! Welcome to my population simulator!", end=' ')
print("In this simulation, you are")
print("able to input your starting population,", end=' ')
print("the number of generations your")
print("society will go through, and a", end=' ')
print("random five digit code that will determine")
print("the diseases, triumphs, and game", end=' ')
print("ending scenarios your population will")
print("endure through their lifetime. Good luck!")
print(" ")
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
#This was the website I used to gain a better understanding of end= statements
popNo = input("Enter Population Start Number: ")
# The while statements prevent the user to input some invalid inputs
while len(popNo) == 0:
    popNo = input("Enter Population Start Number: ")
# genNo = amount of generations the population will go through
genNo = input("Enter your Society's Generations: ")
while len(genNo) == 0:
    genNo = input("Enter your Society's Generations: ")
seed = input("Enter random 5 digit code: ")
while len(seed) != 5:
    seed = input("Code must be 5 digits: ")
# The seed is just something my code uses as a number to preform operations
#on that determine which predetermined scenario the population will go through
if int(genNo) == 0:
    print("Your population is ", (popNo), ". Not much progress...", sep='')
# https://www.geeksforgeeks.org/python-sep-parameter-print/
#This was the website I used to gain a better understanding of sep= statements
def defeatAliens(deaths, kidnapped):
    print("Hooray! Your people killed ", end='')
    print(str(int(deaths*2.6))+" of the aliens and")
    print("stole all their fancy equipment!", end='')
    print("You also took "+str(int(kidnapped)-450))
    print("of their people to conduct scientific research on.")

def loseToAliens(deaths, kidnapped):
    print("Uh oh, the aliens killed "+str(int(deaths*5.3))+" of your people,")
    print("kidnapped "+str(int(kidnapped)+1523)+" of them, and then left")
    print("out of boredom.")
def main():
    print("Aliens have invaded your planet! Type the number of weapons")
    weapons = int(input("you would like to use to fight them: "))
    print("Woah! Now they're destroying your buildings!")
    yesOrNo = input("Would you like to surender: ")
    while yesOrNo != ("Yes") and yesOrNo != ("No"):
        yesOrNo = input("Please type the words; Yes or No: ")
    if weapons >= 500 and yesOrNo == "No":
        defeatAliens(weapons,weapons)
    if weapons >= 500 and yesOrNo == "Yes":
        loseToAliens(weapons, weapons)
    if weapons < 500 and yesOrNo == "No":
        loseToAliens(weapons, weapons)
    if weapons < 500 and yesOrNo == "Yes":
        loseToAliens(weapons, weapons)
#I added some functions to simulate an alien invasion
if int(genNo) > 0:
    if int(popNo) <= 1:
        print("Your population was too small to sustain itself.")
    elif int(popNo) <= 7:
        print("Your society had to inbreed to sustain itself...")
        print("It didnt end well.")
    elif int(popNo) > 12000000000:
        print("You crammed your world with too many people. Everyone died.")
    else:
        yeOrNo = 1
        huh = 1
        if int(popNo) >= 8 and int(popNo) <= 12000000000:
            if int(seed) % 2 == 0:
                # I used the numeric operation % to differentiate between even
                # and odd numbers.
                newPop = (int(popNo) * int(genNo) ** 2)
            # I used the numeric operators * and ** to simulate rapid
            # population growth.
            if not int(seed) % 2 == 0:
                newPop=((int(popNo) * (int(genNo) / (2 ** int(genNo)))) + 100)
                # I used the / operator to simulate game ending
                # diseases.
        if (int(seed) % 3) == 0:
            newPop = int(newPop) - 100
        if (int(seed) % 3) == 1:
            newPop = int(newPop) // 2
            # I used the numeric operator // to simulate a scenario where
            # approximately half the population dies.
        if (int(seed) % 3) == 2:
            newPop = int(newPop) + 100
            #I used the numeric operator + to add 100 people to the population

        if (int(seed) % 4) == 0:
            print("Woah, your population developed birth control!")
            yeOrNo = input("Would you like to mass produce it? Yes or No: ")
            while yeOrNo != ("Yes") and yeOrNo != ("No"):
                yeOrNo = input("Please type the words ; Yes or No: ")
            if yeOrNo == "Yes":
                newPop = newPop * 3 / 4
                int(newPop)
            if yeOrNo == "No":
                newPop = newPop * 5 / 4
                int(newPop)

        if (int(seed) % 4) == 1:
            huh = (int(genNo)) // 10
            for x in range(huh):
                newPop += 123

        if (int(seed) % 4) == 2:
            main()
            # function call
            newPop += 1000
        if (int(seed) % 4) == 3:
            main()
            newPop += 10000
            # function call
        if (int(seed) % 12345) == 0:
            newPop = -1

        if int(newPop) >= int(popNo) * 10:
            print("Wowie, your society was very successful!")
            if yeOrNo == "No":
                print("Unfortunetaly, your population contracted")
                print("wide spread STDs.")
            print("Your final population is", str(int(newPop)) + "!")
            # I used the + string operator to combine a variable and text.
        if int(newPop) > int(popNo) * 1 and int(newPop) < int(popNo) * 10:
            print("Your society increased in population!")
            if yeOrNo == "No":
                print("Unfortunetaly, your population contracted")
                print("high high amounts of STDs.")
            print("Your final population is", str(newPop) + "!")
        if int(newPop) < int(popNo):
            if (int(seed) % 12345) == 0:
                print("Your population got hit with a meteor!", end=' ')
                print("Everyone died.")
            elif int(newPop) >= 0:
                int(newPop)
                print("Your population decreased to "+str(int(newPop)) + ".")
            else:
                print("Your population discovered nuclear physics!", end=' ')
                print("However, your society went ")
                print("into nuclear war and destroyed the planet...")
        if int(newPop) >= 12000000000:
            print("Unfortunetaly, you overloaded your world with too ")
            print("many people, causing global famine. Everone died.")
        if int(newPop) <= 1:
            print("Yikes!")
        elif int(newPop) <= 15:
            print("Thats pretty bad!")
else:
    print("I have no clue what happened. You", end=' ')
    print("broke" * 23)
    # I used the * string operator to say yhe word broke 23 times to
    # tell the user they inputted an "invalid" value.
    print(" ")
    print("..error")