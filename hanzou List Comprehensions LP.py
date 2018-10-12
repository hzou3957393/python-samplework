
## Section 2
## Algorithm:
## 1. Store filename containing possible passwords in a variable as a string.
## 2. Create a list that opens and iterates through file to store every line of file as string in list. Every line is stripped. The list is stored as a variable.

filename = "passwords.txt"
passwords = [line.strip() for line in open("passwords.txt", "r")]

##print(passwords)

## Section 3

## Algorithm:
## 1. Define function show_list that takes one argument, a list of possible passwords.
## 2. Print the message telling user that the following are the possible passwords and line of hyphens.
## 3. Iterate through list starting at the beginning, ending at the the last item, and checking every five elements in between.
## 4. For every fifth element, print that element along with the four seceding elements, joining the list into one string separated by spaces.
## 5. Print statement that displays the number of possible passwords in the list using the length of the list.

def show_list(password_list):
    print("The current possible passwords are:")
    print("-"*30)
    for i in range(0,len(password_list),5):
        line = " ".join(password_list[i:i+5])
        print(line)
    print("\n(" + str(len(password_list)) + " possible)")

show_list(passwords)

## Section 4

## Clue 1
## For the list comprehension, I am creating a new list by iterating through every work and including only the passwords with length greater than or equal to 6
print("\nClue 1: The password is at least 6 characters long.\n")

clue1_lst = [word for word in passwords if len(word) >= 6]

show_list(clue1_lst)

## Clue 2
## For this list comprehension, I am iterating through the list of passwords from clue one.
## For each password within that list, I have a list including only the characters that are alphabetical letters, and we calculate the length of that list.
## I am including the password if the list of letters is at least 1.
print("\nClue 2: The password contains at least one letter.\n")

clue2_lst = [word for word in clue1_lst if len([char for char in word if char.isalpha()]) >= 1]

show_list(clue2_lst)

## Clue 3
## For this list comprehension, I am iterating through the list of passwords from clue 2
## I include the word in this new list if the first lower case of the first character (index 0) is not a vowel AND the lower case second character (index 1) is a vowel.
print("\nClue 3: The password does not start with a vowel, but the second character is a vowel.\n")

clue3_lst = [word for word in clue2_lst if word[0].lower() not in "aeiou" and word[1].lower() in "aeiou"]

show_list(clue3_lst)

## Clue 4
## For this list comprehension, I am iterating through the list of passwords from clue 3
## There are two lists within this list comprehension. One of the lists are all the lower case version of the characters from the respective password that are not vowels, and the other is the list of the words vowels.
## The if statement in the outer list tests if the length of the list of consenants is greater than or equal to 2 times the length of the list of vowels
## if so, the word is included in the list for clue 4

print("\nClue 4: The password has at least twice as many consonants as vowels.\n")

##clue4_lst = [word for word in clue3_lst if 2*len([char for char in word if char.lower() not in "aeiou"]) >= len([char for char in word if char.lower() in "aeiou"])]
clue4_lst = [word for word in clue3_lst if len([char for char in word if char.lower() not in "aeiou"]) >= 2*len([char for char in word if char.lower() in "aeiou"])]

show_list(clue4_lst)

## Clue 5: Bonus Clue
## For this list comprehension, the outer list iterates through the list of passwords from clue 4.
## The inner list is a list of all the vowels from the respective word
## That inner list is sorted, then compared to the unsorted list of vowels.
## If those two lists are the same, that means that the vowels were already in order.
## In that case, if the two lists are the same, the password is included in the clue 5 list.
print("\nClue 5: The password has all of its vowels in alphabetical order.\n")

clue5_lst = [word for word in clue4_lst if sorted([char for char in word if char in "aeiou"]) == [char for char in word if char in "aeiou"]]

show_list(clue5_lst)








                                                

