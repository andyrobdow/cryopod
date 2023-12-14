gameName = "Cryo Pod"
player1 = ""

#function definitions for different rooms begin here
def game_launch():
  print("Welcome " + player1 + ", are you ready to play " + gameName + "?")

  introMessage = "You awake from cryo-sleep still stretched out in the recently unsealed cryo-bed. There is an acrid smell in the air and noone is around. \nSomething is very wrong. You quickly come to your senses and leap from the bed onto the cold floor."
  print(introMessage)

  #call the function that defines the first room
  cryoChamber()

def cryoChamber():
    description = "The cryo chamber is cold. Open beds line the walls. The floor has been mopped clean and dried some time ago. \nThe lights flicker, never quite reaching their full brightness."
    print(description)
    options = ["look", "exit"]

    playerInput = ""
    while playerInput not in options:
        print("Options: look, exit")
        playerInput = input(">>> ")
        if playerInput == "look":
            print("All of the other cryo-beds are open and empty. It looks like all of the rest of the crew are awake. Strange.")
            cryoChamber()
        elif playerInput == "exit":
            sickBay()
        else:
            print("You can't do that")

def sickBay():
    description = "This is the sickbay. Cold steel and medical supplies are all around, many scattered on the floor or broken. \nThe flickering lights make the shadows dance. The doctor's medical log blinks on a screen in the corner."
    print(description)
    options = ["up", "left", "read"]

    playerInput = ""
    while playerInput not in options:
        print("Options: You can go up to the cryochamber, left into the hall or read the medical log")
        playerInput = input(">>> ")
        if playerInput == "read":
            print(
                "MEDICAL LOG - FINAL ENTRY: The crew have escaped disaster on this lifepod only to wake to a terrible sickness. \nIt begins with a burning hunger and does not stop until the host becomes zombie-like. " + player1 + " is still \nasleep in the cryo bed but there is not time to wake them. We must find safety!")
            sickBay()
        elif playerInput == "up":
            cryoChamber()
        elif playerInput == "left":
            mainJunction()
        else:
            print("You can't do that")

def mainJunction():
    description = "It's the main junction connecting to all the other parts of the ship.\nYou hear a shuffling in the dark. Cold hands come grabbing at your vulnerable form.\nYou are killed. GAME OVER"
    print(description)

#the procedure controlling the game starts from here
if __name__ == "__main__":
    player1 = input("Enter a name for player 1 >>> ")
    #the command below starts the game by calling the game launch function
    game_launch()



