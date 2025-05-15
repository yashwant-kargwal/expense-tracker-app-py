# Yashwant Kargwal
# Expense Tracker App Using Local Storage

import os
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")     #join download path with your system
file_path = os.path.join(downloads_path, "data_record.ety")     #join download path with 'data_record.ety' file

if not os.path.exists(file_path):   #check and generate if file not found
    open(file_path,'x')


# fetch data form 'data_record.ety' file
def fetchData():
    with open(file_path,'r') as file:   # reading the file data
        data = file.readlines()
        return data
        
# fetch date 
def fetchDate():
    while True:
        try:    #check correct date
            dd = int(input("Enter Day(1-31) : "))
            if 1 <= dd <= 31 :
                break
            print("Enter Day in Range of 1 to 31!")
        except ValueError:
            print("Enter Valid Day!")
            continue

    while True:
        try:    #check correct month
            mm = int(input("Enter Month(1-12) : "))
            if 1 <= mm <= 12:
                break
            print("Enter Month in Range of 1 to 12!")
        except ValueError:
            print("Enter Valid Month!")
            continue
            
    while True:
        try:    #check correct year
            yyyy = int(input("Enter Year(2000-2100) : "))
            if yyyy in range(2000,2101):
                break
            print("Enter Year in Range of 2000 to 2100!")
        except ValueError:
            print("Enter Valid Year!")
            continue

    date = f'{dd}/{mm}/{yyyy}'      #format date in (dd/mm/yyy)
    return date 

# Function to add expense in 'data_record.ety' file
def addExpense(date,category,item,amount,description):
    with open(file_path,'a') as file:
        content = f'{date},{category},{item},{amount},{description}\n'      #generate entry data of expense
        file.writelines(content)
        print("\n\t Expense Added!")    #recod successfull appended

# function to show all expenses from 'data_record.ety' file data
def showAllExpenses(data):
    num = 1
    entries = 0
    print("{:<5}{:<16}{:<15}{:<15}{:<15}{:<50}".format("Sr.","Date","Category","Item","Amount","Description"))      #formated cation of table
    for lines in data:
        listdata = lines.strip().split(',')     #split string data

        listDate = listdata[0]
        listCategory = listdata[1]
        listItem = listdata[2]
        listAmount = listdata[3]
        listDescription = listdata[4]
        print("{:<5}{:<16}{:<15}{:<15}{:<15}{:<50}".format(num,listDate,listCategory,listItem,listAmount,listDescription))
        num += 1
        entries += 1

    if entries ==0:
        print("\n\t\tNo Record Found!")

# function to show total spent amount form 'data_record.ety' file data
def showTotalSpent(data):
    totalSpent = 0
    for lines in data:
        listdata = lines.strip().split(',')

        listAmount = listdata[3]
        totalSpent += int(listAmount)
    return totalSpent
        
# function to show average spent amount form 'data_record.ety' file data
def averagePerItem(total,data):
    num = 0
    for lines in data:
        num +=1
    avg = total/num if num != 0 else 0
    return avg
        
# function to show date wise expense track form 'data_record.ety' file data
def filterByDate(data,date):
    num = 1
    entries = 0
    print("{:<5}{:<16}{:<15}{:<15}{:<15}{:<50}".format("Sr.","Date","Category","Item","Amount","Description"))
    for lines in data:
        listdata = lines.strip().split(",")

        if listdata[0] == date:     #check input date and list date by index 0

            listDate = listdata[0]
            listCategory = listdata[1]
            listItem = listdata[2]
            listAmount = listdata[3]
            listDescription = listdata[4]
            print("{:<5}{:<16}{:<15}{:<15}{:<15}{:<50}".format(num,listDate,listCategory,listItem,listAmount,listDescription))
            num += 1
            entries += 1

    if entries == 0:
        print(f'\n\t\tNo Record Found on {date}!')

# function to show Category wise expense track form 'data_record.ety' file data
def filterByCategory(data,Category):
    num = 1
    entries = 0     
    print("{:<5}{:<16}{:<15}{:<15}{:<15}{:<50}".format("Sr.","Date","Category","Item","Amount","Description"))
    for lines in data:
        listdata = lines.strip().split(",")

        if listdata[1] == Category:

            listDate = listdata[0]
            listCategory = listdata[1]
            listItem = listdata[2]
            listAmount = listdata[3]
            listDescription = listdata[4]
            print("{:<5}{:<16}{:<15}{:<15}{:<15}{:<50}".format(num,listDate,listCategory,listItem,listAmount,listDescription))
            num += 1
            entries += 1

    if entries == 0:    #if entries are zero
        print(f'\n\t\tNo Record Found on {Category}!')

# function to show Highest Spent form 'data_record.ety' file data
def findHighestSpent(data):
    maxSpent = 0
    date = ""
    category = ""
    item = ""
    amount = ""
    description = ""
    entries = 0
    for lines in data:
        listData = lines.strip().split(",")
        if int(listData[3]) > int(maxSpent):    #compare both int data
            maxSpent = listData[3]
            date = listData[0]
            category = listData[1]
            item = listData[2]
            amount = listData[3]
            description = listData[4]
            entries +=1
    
    if entries == 0:
        return "\n\tNo Record Found!"
    else:
        return f'Your Highest spent is ₹{amount} on {date} for {item} in Category of {category} and You Describe it as : {description}'

# fuction to clear all data form 'data_record.ety' file
def clearAllData():
    with open(file_path,'w') as file:   #this w mode overwrite the data with nothing
        pass




# Welcome message 
print("\n\tWelcome to Expense Tracker")

while True:     #infinite loop for repeat ask
    print("\nSelect Below Option : ")   #Menu Bar
    print("\n1. Add New Expense \n2. Show All Expenses \n3. Show Total Spent \n4. Filter by Date \n5. Filter by Category \n6. Show Highest Expense \n7. Reset All Data \n8. Exit")

    try:    #Handle ValueError
        userChoice = int(input("Enter Your Choice : "))
    except ValueError :
        print("\n\tEnter Int Values Please!")
        continue

    if userChoice == 1:     #Add Expense
        print("\nFirst We Add Date (DD/MM/YYYY) :- ")
        date = fetchDate()      #calling fetchDate function
        
        print("\nTime to Add Category (Food, Work, Bills etc.) or Enter to 'Unknown'! : ")
        category = input("Enter Category : ").title().strip()   #input category

        print("\nTime to Name of Item or Enter to 'Unknown' : ")
        item = input("Enter Name Of Item : ").title().strip()   #input category

        print("\nTime To Add Amount of Item : ")
        while True:
            try:    #check int value or not
                amount = int(input("Enter Amount : "))
                if amount <= 0:
                    print("Enter Greater than 0 Amount!")
                    continue
            except ValueError:
                print("Enter Number Value!")
                continue
            break

        print("Time to Add Description (optional : Enter to Skip!) : ")
        description = input("Enter Descrption of Item : ").title().strip()

        
        # we use 'or' to send true value
        addExpense(date,category or "Unknown",item or "Unknown",amount,description or "No Description!")

    elif userChoice == 2:   #Show Expense
        data = fetchData()
        showAllExpenses(data)

    elif userChoice == 3:   #Show Total Spent
        data = fetchData()
        total = showTotalSpent(data)
        average = averagePerItem(total,data)
        print(f'Dear User, You Spent Total ₹{total} Amount and Your Average Spent on Per Item : ₹{average}')

    elif userChoice == 4:   #Filter by Date
        data = fetchData()
        date = fetchDate()
        filterByDate(data,date)


    elif userChoice == 5:   #Filter by Category
        data = fetchData()
        category = input("Enter Category : ").strip().title()
        filterByCategory(data,category)

    elif userChoice == 6:   #Show Highest Expense
        data = fetchData()
        highest = findHighestSpent(data)
        print(highest)

    elif userChoice == 7:   #Reset All Data
        clearAllData()
        print("\n\t Clear All Expense Track From 'data_record.ety' file!")

    elif userChoice == 8:   #Exit Button
        print("\n\tYour Data safed in 'data_record.ety' file!")     #Ending Message with safe file
        print("\t\tThanks For Using!\n")
        break

    else:                   #Error Message
        print("\n\tEnter Valid Choice!")