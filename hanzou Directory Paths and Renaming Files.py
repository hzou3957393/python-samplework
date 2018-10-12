
## 1. Standard Library Documentation
## https://docs.python.org/3.5/library/index.html

## 2. Algorithm

## Define a function that takes no arguments.
## Inside function definition body, first ask user to input a path to a directory
## Then we try the following:
    ## Iterate through the list of items in the directories (using listdir() function)
    ## If the item is a file, test if the file has the word "draft" in it. If it has "draft", then:
        ## Get the current date stored in variable
        ## Rename the file by replacing the word "draft" with "final"
        ## Use variable to store string of information about the current date
        ## Open the file and append that string/line into file
        ## Close file.
## If the "try" fails, then the user's input was not a valid path to a directory. So the "except" block prints out message to tell user that their input is not a valid directory path.


## 3

## os.rename(filename, filename.replace("test", ""))
## now_date = datetime.date.today()

import os
import datetime

def draft_final():

    path = input("Please enter a path to a directory: ")
    try:
        for item in os.listdir(path):
            if os.path.isfile(item):
                if "draft" in item:
                    now_date = datetime.date.today()
                    os.rename(os.path.join(path,item), os.path.join(path,item.replace("draft", "final")))
                    file = open(item.replace("draft", "final"), "a+")
                    line = now_date.strftime("Edited on %d %b %Y")
                    file.write(line)
                    file.close()
    except:
        print("Invalid path for directory.")
                



