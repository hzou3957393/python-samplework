import urllib.request
import re
import webbrowser

## Section 1

## Storing url in variable, opening web page, obtaining/storing source code as string in contents, and closing webpage
url = "https://www.indiana.edu/news-events/index.html"
web_page = urllib.request.urlopen(url)
contents = web_page.read().decode(errors="replace")
web_page.close()

##file = open("lp2sourcecode.html","w")
##file.write(contents)
##file.close()

## Section 2
print("Searching:", url, "\n")

## Storing all headlines in list with findall
## Finding all headlines that start with <span> tag with itemprop="headline" in source code and ending with the closing tag
headlines = re.findall('(?<=<span itemprop="headline">).+?(?=<)', contents, re.DOTALL)
## Print each headline in a new line
for headline in headlines:
    print(headline + "\n")

## Section 3

print("Searching:", url, "\n")

## Ask user for input for a phrase to search for, store in phrase
phrase = input("Please enter a word to search for: ")
## In order for the pattern to recognize either lower case or capital letters, I am creating an variable that starts as an empty string
## This variable will hold a capitalized and lower case version of every letter in phrase, each pair between parentheses, meaning each letter of phrase will be either upper or lower case, but must be in the right order
## For example, if phrase is "Bloomington", then the pattern for that phrase is "[Bb][Ll][Oo][Oo][Mm][Ii][Nn][Gg][Tt][Oo][Nn]"
phrase_pattern = ""
for char in phrase:
    phrase_pattern = phrase_pattern + "[" + char.lower() + char.upper() + "]"
## Find list of all headlines that contain this phrase
withPhrase = re.findall('(?<=<span itemprop="headline">)[\w\s]*'+phrase_pattern+'.+?(?=</)', contents, re.DOTALL)
## Print each headline with phrase
for head in withPhrase:
    print(head + "\n")

## Section 4

## Ask user for word to search for in the headlines
search_browser = input("Please enter a word to search for: ")
print()
## Converting the search phrase into patter just like in part 3
search_pattern = ""
for char in search_browser:
    search_pattern = search_pattern + "[" + char.lower() + char.upper() + "]"
## Find all titles with this phrase
searchTitles = re.findall('(?<=<span itemprop="headline">)[\w\s]*'+search_pattern+'.+?(?=<)', contents, re.DOTALL)
## For every title found with the phrase, we want to get its link to the article
## For every found title, I will do a findall that looks for everything after "<a itemprop="url" href=" and stop when the current href tag closes immediately followed by the span tag for the headline with the headline title concatenated
## Then use webbrowser to open a new tab for that link
## Since findall is a list, and each link is stored as the only value in its separate list, I am just using indexing to get the string for the link's url
for title in searchTitles:
    print(title)
    link = re.findall('(?<=<a itemprop="url" href=).+?(?=><span itemprop="headline">'+title+')', contents)
    webbrowser.open_new_tab(link[0])

    



