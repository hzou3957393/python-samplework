import urllib.request
import re

## 1. Regular expression patter for hex color:
## '#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}'

## 2. Algorithm

## Import necessary modules, urllib.request and re.
## Store the url in a variable, and use the url to open the link and store the contents of the source code. Close webpage.
## After looking at the source code, find the regular expression patter to match the game results.
## I am storing my results in two lists, one for the wins and one for the losses:
    ## Each game result is found after a div tag, immediately followed by either W or L, a space, and two (usually two-digit) numbers with a hypen in the middle. The results are followed by the beginning of another tag.
    ## The regular expression for the wins: '(?<=div>)W{1}\s[0-9]{1,2}-[0-9]{1,2}.*?(?=<)'
    ## The regular expression for the losses: '(?<=div>)L{1}\s[0-9]{1,2}-[0-9]{1,2}.*?(?=<)'
    ## The only difference between the two are the W and L right after the div tag, indicating if the game is a win or loss.
## To count the number of wins, I use the length of the list of wins.
## To count the number of losses, I use the length of the list of losses.
## Print number of wins and losses.

## 3

## Store url, open webpage for url, get contents, and close webpage
url = "http://cgi.soic.indiana.edu/~dpierz/mbball.html"
web_page = urllib.request.urlopen(url)
contents = web_page.read().decode(errors="replace")
web_page.close()

##file = open("game_code.html","w", encoding="utf-8")
##file.write(contents)
##file.close()

## Use regular expressions to find the wins and losses and store in separate lists.
wins = re.findall('(?<=div>)W{1}\s[0-9]{1,2}-[0-9]{1,2}.*?(?=<)', contents, re.DOTALL)
losses = re.findall('(?<=div>)L{1}\s[0-9]{1,2}-[0-9]{1,2}.*?(?=<)', contents, re.DOTALL)

## Print out the number of wins and losses based on the length of their respective lists.
print("Wins:", len(wins))
print("Losses:", len(losses))

## Bonus

## This time, I store all of the game results in one list using a similar regular expression. Instead of just W or L, I am indicating to include all results that start with either W or L.
all_games = re.findall('(?<=div>)[WL]{1}\s[0-9]{1,2}-[0-9]{1,2}.*?(?=<)', contents, re.DOTALL)

## Store total difference starting at 0
total_diff = 0
## Iterating through every result, I am splitting the score on either side of the hypen "-" after the first two characters (the W or L and space)
## I calculate the game's score difference by subtracting the first element of the split list (as an integer) with the second element (as an integer)
## Then I add this individual game's difference to the total difference
for game in all_games:
    game_info = game[2:].split("-")
    diff = abs(int(game_info[0]) - int(game_info[1]))
    total_diff += diff
## The total_diff then has all the games' differences added together.
## Print the total difference.
print("Total Difference:", total_diff)
    
