#!/usr/bin/env python3
#created by Regina Citra Pesela (reginapasela@gmail.com)

class Category:
    #instantiate objects with ledger variable
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.totalSpend = 0
        
    #this method will showed when the object is called
    def __str__(self):
        #header        
        #count the asterix needed based on category name length
        asterix_length = ((30 - len(self.name)) // 2)

        #print title line (********category********)
        if len(self.name) % 2 != 0:
            header = ("*" * (asterix_length + 1)) + str(self.name) + ("*" * asterix_length)
        else:
            header = ("*" * asterix_length) + str(self.name) + ("*" * asterix_length)

        #body
        #body variable to contains all transaction history (started with "\n")
        body = "\n"

        #loop for every transaction happen in ledger to get all transaction values
        for amounts in self.ledger:            

            #cut transaction description if its too long and add it to descLedger variable
            if len(str(amounts["description"])) >= 24:
                descLedger = amounts["description"][:23]
            #otherwise add any 
            else:
                descLedger = amounts["description"][:]

            #add 2 zero behind comas like xxx.00
            amountsLedger = format(amounts["amount"], ".2f")

            #print description and amount of transaction
            body += ((str(descLedger) + str(" " * (30 - len(descLedger) - len(str(amountsLedger)))) + str(amountsLedger))) + "\n"
        
        #delete last part "\n"
        body = body[:-1]

        #footer

        #format get_balance into 2 zero decimal
        balanceLedger = format(self.get_balance(),".2f")
        
        #return Total: XXXX.00
        footer = "\n" + "Total: " + str(balanceLedger)

        #output variable to contains all output
        output = header + body + footer

        #return output
        return output

    def deposit(self, amount, description = ""):
        #append deposit dictionary to ledger list
        self.ledger.append({"amount" : amount, "description" : description})
        
    def withdraw(self, amount, description = ""):
        #better check to make sure amount is a digit and negative (using try and except)
        if amount > 0:
            amount *= -1

        #if the balance is 0 then cancel the withdraw and return False
        if self.check_funds(abs(amount)):
            self.totalSpend += amount

            #append withdraw dictionary to ledger list and return true
            self.ledger.append({"amount" : amount, "description" : description})
            
            return True
        
        else:
            return False
        
    def get_balance(self):
        #first define balance as zero (0)
        self.currentBalance = 0

        #then loop for every transaction happen in ledger to get all transaction values
        for amounts in self.ledger:
            
            #then add those transaction values into balance variable
            self.currentBalance += (amounts["amount"])

        #return balance variable
        return self.currentBalance
    
    def transfer(self, amount, target):
        withdraw_desc = "Transfer to" + " " + str(target.name)
        deposit_desc = "Transfer from" + " " + str(self.name)

        #withdraw amount from self
        if self.withdraw(amount, withdraw_desc):

            #then deposit it to target
            target.deposit(amount, deposit_desc)

            #return True
            return True
        
        #return False if funds to withdraw isnt enough
        return False
    
    def check_funds(self, amount): #this methods should be use by withdraw and deposit method
        #check if amount inputted is bigger than current balance and return False
        if amount > self.get_balance():
            return False
        
        #otherwise return True
        return True

def create_spend_chart(categories): #list of categories
    
    #header
    header = "Percentage spent by category\n"

    #body
    body = str()

    #create variable to help creating chart
    totalAmount = 0
    totalCategories = 0
    longestName = 0
    percentCategory = list()

    name = str()
    #do looping to cou
    # nt totalAmount and totalCategories
    for category in categories:
        totalAmount += category.totalSpend
        totalCategories += 1
        
        #determine the longest name in list of categories
        if len(category.name) > longestName:
            longestName = len(category.name)

    #calculate percentage of spending in each categories
    for category in categories:
        percentCategory.append(category.totalSpend / totalAmount * 100)
        
    #create percentage chart y-axis
    valGraph = list()
    
    for i in range(100,-1,-10):
        for j in percentCategory:
            if j > i:
                valGraph.append("o")
            else:
                valGraph.append(" ")

    valGraph = [valGraph[i:i + totalCategories] for i in range(0, len(valGraph), totalCategories)] 

    #graph y-axis
    #100
    body += ("100" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[0][k]
        else:
            body += "  " + valGraph[0][k]
    body += "  \n"
    #90
    body += (" " + "90" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[1][k]
        else:
            body += "  " + valGraph[1][k]
    body += "  \n"
    #80     
    body += (" " + "80" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[2][k]
        else:
            body += "  " + valGraph[2][k]
    body += "  \n"
    #70
    body += (" " + "70" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[3][k]
        else:
            body += "  " + valGraph[3][k]
    body += "  \n"
    #60
    body += (" " + "60" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[4][k]
        else:
            body += "  " + valGraph[4][k]
    body += "  \n"
    #50
    body += (" " + "50" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[5][k]
        else:
            body += "  " + valGraph[5][k]
    body += "  \n"
    #40
    body += (" " + "40" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[6][k]
        else:
            body += "  " + valGraph[6][k]
    body += "  \n" 
    #30
    body += (" " + "30" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[7][k]
        else:
            body += "  " + valGraph[7][k]
    body += "  \n"
    #20
    body += (" " + "20" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[8][k]
        else:
            body += "  " + valGraph[8][k]
    body += "  \n"
    #10
    body += (" " + "10" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[9][k]
        else:
            body += "  " + valGraph[9][k]
    body += "  \n" 
    #0
    body += ("  " + "0" + "|")
    for k in range(totalCategories):
        if k == 0:
            body += " " + valGraph[10][k]
        else:
            body += "  " + valGraph[10][k]
    body += "  \n" 

    #create x-axis chart (---------------)
    body += (4 * " " + ((totalCategories * 3) + 1) * "-")

    #do second loop to assign name to x-axis
    for i in range(longestName):
        body += "\n     "
        for category in categories:
            #if string characters is out of range replace with space
            try:
                body += category.name[i] + "  "
            except:
                body += " " + "  "

    #combine all chart strings
    chart = header + body

    # print(percentCategory)
    #return chart
    return chart


#test
#create object
food = Category("Food")
entertainment = Category("Entertainment")
auto = Category("Auto")

#transaction on object 1
food.deposit(1, "first deposit")
food.deposit(3, "second depo")
food.deposit(5, "tamiya")
food.withdraw(-11,"test") #cant withdraw
food.withdraw(-5,"test")

#transaction on object 2
entertainment.deposit(100, "init")
entertainment.deposit(300, "SNSD")
entertainment.deposit(500, "IU")
entertainment.withdraw(2000, "Test") #cant withdraw

#transaction on object 2
auto.deposit(600, "init")
auto.deposit(900, "SNSD")
auto.deposit(200, "IU")
auto.withdraw(700, "Test")

#transfer test
food.transfer(4, entertainment)
entertainment.transfer(200, food)

print(food,entertainment,auto,sep="\n")
print(create_spend_chart([food, entertainment, auto]))