
## 1. Hangman

## creating variable to store secret word. Here, I just chose the secret word, but I could also have some kind of list or file full of words to choose from randomly.
secret_word = "puppy"
## create empty list to store correctly guessed letters
reveal_letters = []
## variable to keep track of number of incorrect guesses by user
wrong_guesses = 0

## while loop to repeat asking user for guesses until too many wrong answers accumulate
while True:
    ## check to see if user already made too many wrong guesses
    ## Here, I am just setting that number to 10, since we are not given any criteria in the homework problem.
    if wrong_guesses < 10:
        ## If the user still has guesses left, ask for an input that is a single letter, not a number or string longer than 1 character
        ## I used the .lower() method to make sure that the letter is read as lower case, even if the user inputs an upper case letter
        guess = (input("Enter a guess that is a letter: ")).lower()
        ## check if the user's input is a letter. If so, proceed.
        if guess.isalpha() and len(guess) == 1:
            ## check if the letter is in secret_word
            if guess in secret_word:
                ## if so, we add the letter to list, and we create empty string to prepare for revealing letters and place of letters to user
                reveal_letters.append(guess)
                show_letters = ""
                ## to reveal correct letters, we iterate through the characters in the secret word
                ## if the current letter is in the correct guesses list, we concatenate that letter to show_letters
                ## if it is not in the guesses list, we concatenate an underscore to hold the place of that letter not yet guessed
                for letter in secret_word:
                    if letter in reveal_letters:
                        show_letters += letter
                    else:
                        show_letters += "_"
                ## if the user now has guessed all of the letters to the secret word, we let them know, reveal the word, and stop the game.
                if show_letters == secret_word:
                    print("You have all of the letters to the secret word!")
                    print("Secret word is: " + show_letters)
                    break
                ## if there are more letters to be guessed, we show them the letters they have guessed so far and let the game repeat
                else:
                    print("You guessed a correct letter.")
                    print("Here is what you have so far: " + show_letters)
                ## if their guess is not in the secret word, we add one to the wrong_guesses count and then go back to the top of while loop
            else:
                wrong_guesses += 1
                print("Your guess was incorrect. Number of incorrect guesses: " + str(wrong_guesses))
        ## if the guess was longer than one character or not a letter, then let the user know that the guess is invalid
        else:
            print("Your guess should be one letter. Try again.")
    ## if too many wrong guesses already occurred, the game is over
    else:
        print("You made too many wrong guesses. Game over.")
        break


## 2. Rock, Paper, Scissors

##Import the random module.
import random
##Set a variable storing "rock", "paper", "scissors" options as list.
rps_options = ["rock", "paper", "scissors"]

while True:
    ##Use random.choice() method to randomly choose computer's choice and store that choice as a separate variable.
    computer_choice = random.choice(rps_options)
    ##Ask for user to input choice of "rock", "paper", or "scissors".
    ##Store the choice in all lower case to compare to computer's choice, in case any letter in the user's input is uppercase
    user_choice = (input("Choose rock, paper, or scissors: ")).lower()
    ##Compare each combination of user and computer choices:

    ##	If computer chooses "rock" and user enters "rock":
    ##		Print that the game is tied.
    if computer_choice == "rock" and user_choice == "rock":
        print("Tie. Try again.")
    ##	If computer chooses "rock" and user enters "paper":
    ##		Print that the user wins.
    elif computer_choice == "rock" and user_choice == "paper":
        print("You win.")
    ##	If computer chooses "rock" and user enters "scissors":
    ##		Print that the user loses.
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You lose.")
    ##	If computer chooses "paper" and user enters "rock":
    ##		Print that the user loses.
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lose.")
    ##	If computer chooses "paper" and user enters "paper":
    ##		Print that the game is tied.
    elif computer_choice == "paper" and user_choice == "paper":
        print("Tie. Try again.")
    ##	If computer chooses "paper" and user enters "scissors":
    ##		Print that the user wins.
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You win.")
    ##	If computer chooses "scissors" and user enters "rock":
    ##		Print that the user wins.
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You win.")
    ##	If computer chooses "scissors" and user enters "paper":
    ##		Print that the user loses.
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lose.")
    ##	If computer chooses "scissors" and user enters "scissors":
    ##		Print that the game is tied.
    elif computer_choice == "scissors" and user_choice == "scissors":
        print("Tie. Try again.")
    ## if user says stop, game stops (while loop breaks)
    elif user_choice == "stop":
        break
    ## if it is none of the above scenarios, this means that the user did not choose one of the options in rock, paper, scissors
    ## we let the user know and let the loop continue
    else:
        print("Your choice was not one of the options.")

##Repeat.
            
