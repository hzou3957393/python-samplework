
import tools

##for my reference

##def table_print(headers, data, padding):
##    # We build up the output formatting string
##    # It has this general look, but for any number of columns
##    # output = "{0:>" + str(padding) + "} {1:>" + str(padding) + "}"
##    output = []
##    for i in range(len(headers)):
##        output.append("{" + str(i) + ":>" + str(padding) + "}")
##    output = " ".join(output)
##    
##    # Print the headers 
##    print(output.format(*headers))
##
##    # Print as many dashes as there are columns
##    # Times the padding value (plus 1 for each space)
##    print(("-" * (padding) * len(headers)) + ("-" * (len(headers) - 1)))
##
##    # Print out the data values
##    for item in data:
##        print(output.format(*item))
##    print()
    
## Section 2 (putting in while loop, repeats asking user for state until user input is "stop"
while True:
    import tools
    ## Section 1 (asking for file to load, print information)
    #ask user which state
    state = input("Which state's totals would you like to compute? ")
    #create dictionary to store villain and corresponding votes
    state_dictionary = {}
    #empty list to store list of votes to use for sorting later
    lst = []
    #if user types stop, the loop breaks, program ends
    if state.lower() == "stop":
        break
    #if user types state, add ".txt" at the end, and that is the file we open, store contents into string holding each line as element, close file
    else:
        filename = state.lower() + ".txt"
        state_file = open(filename, "r")
        state_info = state_file.readlines()
        state_file.close()

        ##print(state_info)
        ##creating dictionary with villain as key, vote as value
        ##split each line by tab to separate the key and value to store into villain, vote
        for line in state_info:
            villain, vote = line.split("\t")
            state_dictionary[villain] = int(vote.strip())
        print(state_dictionary)
    #appending each key's value into lst for all the votes
    for key in state_dictionary:
        lst.append(state_dictionary[key])
    ## Section 3
    ## making total votes into one list, sorting into order
    sorted_totals = [lst.pop()]
    while lst:
        #current list is the list where we put the first value at the end if it is smaller than next value
        current = lst.pop()
        for item in range(len(sorted_totals)):
            if current > sorted_totals[item]:
                sorted_totals.insert(item, current)
                current = ""
                break
        if current:
            sorted_totals.append(current)
    print(sorted_totals)   

    ## making table in order fromm highest to lowest votes row by row
    #storing table headings in labels
    #creating variables to store data
    #creating percents to store percentages of vote for each corresponding villain
    labels = ["Name", "Votes"]
    data = []
    percents = []
    #15 padding stored in spacing
    spacing = 15

    for vote_total in sorted_totals:
        #adding tuple with pair to data, first of the key for corresponding value in sorted total, then the vote
        data.append((state_dictionary.get(vote_total, ""), vote_total))
        #calculate percent of vote for villain out of sum of votes
        percent = 100 * (vote_total / sum(sorted_totals))
        #adding tuple with pair to percent data, first the key for the villain's vote, and the percentage
        percents.append((state_dictionary.get(vote_total, ""), percent))

    #using table_print function from tools module
    print("The candidates earned this many votes:")
    table_print(labels, data, spacing)

    ##bonus
    print("The breakdown by percent:")
    table_print(labels, percents, spacing)
    












    
