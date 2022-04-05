import requests

print("Welcome to charades!")

playAgain = "y"

choice = input("Type '1' for the random word version, or '2' for the random animal version: ")
if(choice == "1"):
        print("You have chosen the word version.")
if(choice == "2"):
        print("You have chosen the animal version.")

while(playAgain == "y"):
    playAgain = " "
    if(choice == "1"):
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if(choice == "2"):
        response = requests.get("https://random-word-form.herokuapp.com/random/animal")
    print("Your word is:")
    print(response.text)
    playAgain = input("Would you like another word? If yes, enter 'y' or if no, press enter: ")
