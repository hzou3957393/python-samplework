import csv
import datetime

# 1 Question: Day of the Week Placeholder

# To display the full name of the day of the week using strftime, I would use "%A" as the placeholder.

# 2 Algorithm

# 1. Import csv and datetime modules.
# 2. Read data from the ShopRecords csv file and store data in variable called transactions.
# 3. Set a list called weekend to store the names of the day of the week that are considerred a part of the weekend each in their separate string in a list.
# 4. Iterate through the entries in the transactions data.
# 5. For each entry, split the date entry by the "/" to get the month, day, and year as elements in a list.
# 6. Use datetime.date() to get the date stored as a date data type
# 7. Get the name of the day of week for that date using strftime and the "%A" placeholder, and store this to a variable.
# 8. Check if that day of the week is in the list of weekend days of the week.
# 9. If so, print the "Item" in the entry.

# The for loop will iterate through the entire list of transactions and only print the Item name if it is purchased on a weekend.



# 3 Script to print out the items purchased on a weekend from ShopRecords.csv

# Reading data from csv file and storing into transactions
transactions = csv.DictReader(open("ShopRecords.csv", "r"))
# Storing names of the days of week that are considered part of the weekend
weekend = ["Saturday", "Sunday"]
# Iterate through transactions entry by entry
for entry in transactions:
    # Getting month, day, and year in a list
    m_d_y = entry["Date"].split("/")
    # Getting the date data type using that list with month, day, year
    trans_date = datetime.date(int(m_d_y[2]), int(m_d_y[0]), int(m_d_y[1]))
    # Getting the name of the day of week for this date of purchase entry
    week_day = trans_date.strftime("%A")
    # Check if the week day is during a weekend
    if week_day in weekend:
        # If so, pring the Item in entry
        print(entry["Item"])
