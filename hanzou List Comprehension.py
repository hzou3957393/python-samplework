## Algorithm

## 1. Store filename in variable
## 2. Get list of lines from the file by opening the file under the stored filename. This lines in this list further split into lists of strings storing team name and score.
## 3. Creating empty dictionary stored in variable
## 4. Loop through the list of lines to get a dictionary pairing the team name with their number of wins.
## 5. Loop through the dictionary to print a statement about ever team and their wins.
## 6. Create list that only includes the team name if the length of the name is less than 5 characters long.
## 7. Print statement to display list of teams with less than 5 character long names.
## 8. Create list that contains only the name of every team and are ordered by the number of wins in descending order (from team with most wins to least)
## 9. Print statement to display the first three teams in the list of team names based on number of wins.


## storing filename in variable
filename = "teams.txt"
## taking every line from the file, splitting the line further into lists of strings including team name and number of wins
list_lines = [line.strip().split(" ") for line in open(filename, "r")]

## creating empty dictionary to store team information
team_info = {}

## looping through the list of lines to get values to enter into dictionary, team name as key and number of wins as value
for line in list_lines:
    if line[0] not in team_info:
        team_info[line[0]] = int(line[1])

## looping through dictionary, printing one statement per team stating their name and number of wins
for team in team_info:
    print("The " + team + " have won " + str(team_info[team]) + " games.\n")

## creating list of team names, including only the names of teams whose name has length less than 5
## because we only include the items meeting the requirement, the if statement goes after the iteration (for loop)
team_letters = [line[0] for line in list_lines if len(line[0]) < 5]

## print statement to display the list of team names with less than 5 characters
print("\nTeams with names shorter than 5 letters: " + str(team_letters))

## creating list of team names sorted in descending order based on the respective number of wins
## using nested list comprehension
## inner list sorts the list_lines based on wins
## outer list goes through the sorted list and only includes the team name
score_sort = [team[0] for team in sorted([line for line in list_lines], key = lambda line: int(line[1]), reverse = True)]

## print statement displaying the first three teams with most wins (first three elements of score_sort list)
print("\nThe three teams with the most wins are:", score_sort[0:3])









