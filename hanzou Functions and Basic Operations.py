import donation

# main

# Section 1 - get all of the donations and output the values

#gets a list of 200 random donation amounts from 1-20

donation_amounts = []
for i in range(200):
    amount = donation.get_donation()
    donation_amounts.append(amount)
print("The donation amounts: ", donation_amounts)
#puts donation amounts list in order
donation_amounts.sort()
print("The donation amounts in order: ", donation_amounts)

# As an example of how to get an amount, this gets 1 donation and prints it out
# Run the program a few times and notice that the amount changes.
# If the code won't run, did you put this file and donation.py in the same directory?
print("One donation was received, in the amount of:", amount)


# Section 2 - Compute basic categories

#initial counts for each donation type
small_donations = 0
medium_donations = 0
large_donations = 0
#go through, classify every donation to small, medium, large
#add 1 to count of corresponding type
for amount in donation_amounts:
    if amount <= 5:
        small_donations += 1
    elif amount >= 6 and amount <= 15:
        medium_donations += 1
    else:
        large_donations += 1
#print statements with count of small, medium, large
print("There were ", small_donations, " ($5 or less).")
print("There were ", medium_donations, "($6 - $15).")
print("There were ", large_donations, "($16 or more).")
      

# Section 3 - Compute success or failure

#calculate total funds from donations
total = sum(donation_amounts)
#print total in sentence

#make conditions, if statements, to see if total is greater than 2017
#print success message if > or = 2017, otherwise say goal not met
print("The total amount of money raise is: ", total)
if total >= 2017:
    print("The fundraising goal was met!")
else:
    print("The fundraising goal was not met.")

    
# Section 4 - What can you expect from the bank?

#using total, we see how to break cash
#assign variables to count each type of bill
#begin with 0 for each
hundred = 0
twenty = 0
ten = 0
five = 0
one = 0

#assign variable to decreasing total as we subtract bill amounts, starting from original total
minus_total = total

#I am using a while loop (learned in A211 and I101) to show that as long as minus_total, the running total decreasing every time a bill is used, is still greater than 0, there are still more bills to add
#the loop will continue until the minus_total is 0, meaning all funds have been accounted for in cash
#I tried sticking to what we learned in class with for loops and also tried with using range, but was not able to get the code to work
while minus_total > 0:
    #see if running total is greater than or equal to 100, if so, add an hundred bill and subtract 100 from this total
    if minus_total >= 100:
        hundred += 1
        minus_total -= 100
    #to see if we can use a 20, check if it is > or = 20
    #also check to see if it is less than 100 to avoid breaking five 20's when 100 could have been used
    elif minus_total < 100 and minus_total >= 20:
        twenty += 1
        minus_total -= 20
    #continue checking to make sure running total is less than previous but greather than or equal to current bill
    elif minus_total < 20 and minus_total >= 10:
        ten += 1
        minus_total -= 10
    #continue checking to make sure running total is less than previous but greather than or equal to current bill
    elif minus_total < 10 and minus_total >= 5:
        five += 1
        minus_total -= 5
    #continue checking to make sure running total is less than previous but greather than or equal to current bill
    elif minus_total < 5 and minus_total >= 1:
        one += 1
        minus_total -= 1
    #no more bills, none are worth less than 1 dollar
#while loop stops once the running total gets to 0

#print counts for each type of bill
print("The bank cashed this amount out as:")
print("-" * 40)
print("$100 bills: ", hundred)
print("20 bills: ", twenty)
print("$10 bills: ", ten)
print("$5 bills: ", five)
print("$1 bills: ", one)




