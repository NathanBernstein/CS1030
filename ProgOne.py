'''
Nate Bernstein
Program Make Change
02/07/2022
CS1030
'''
print("How much is in your wallet?") #prompt the user
wallet = input("$") #read the user input
print("How much is the item you're buying?") #prompt the user
cost = input("$") #read the user input
if wallet.replace('.','',1).isnumeric(): #check if input is a number
    if cost.replace('.','',1).isnumeric(): #check if input is a number
        y = cost.split('.')
        x = wallet.split('.')
        if float(wallet) < 0: #check if wallet's value is less than 0, if it is, exit
            print("You can't buy anything negative money! Try again.")
            exit()
        elif len(y[-1]) != 2:
            print("Please enter a dollar amount in the format 0.00. Try again.")
            exit()
        elif len(x[-1]) != 2:
            print("Please enter a dollar amount in the format 0.00. Try again.")
            exit()
        elif float(wallet) == 0: #check if wallet's value is 0, if it is, exit
            print("You can't buy anything with no money! Try again.")
            exit()
        elif float(cost) <= 0: #check if cost's value is less than or equal to 0, if it is, exit
            print("The item has to cost something! Try again.")
            exit()
        elif float(cost) > float(wallet): #check if cost is more than wallet, if it is, exit
            print("You do not have enough money! Try again.")
            exit()
        else: #if all above is false, continue to calculations
            change = float(wallet)-float(cost) #calculate the user's change
            print("You will get $" + str(round(change,2)) + " in change") #print the user's change, rounded to 2 decimal points
            intchange = round(change*100,0) #make sure there is no loss by rounding, create an int from the decimal value
            dollars = int(intchange/100) #figure out how many whole dollars are possible
            intchange = int(intchange-(dollars*100)) #subtract the number of whole dollars from total
            quarters = int(intchange/25) #figure out how many whole quarters are possible
            intchange = int(intchange-(quarters*25)) #subtract the number of whole quarters from total
            dimes = int(intchange/10) #figure out how many whole dimes are possible
            intchange = int(intchange-(dimes*10)) #subtract the number of whole dimes from total
            nickels = int(intchange/5) #figure out how many whole nickels are possible
            intchange = int(intchange-(nickels*5)) #subtract the number of whole nickels from total
            pennies = int(intchange/1) #figure out how many whole pennies are possible
            intchange = int(intchange-(pennies*1)) #subtract the number of whole pennies from total
            print("You get " + str(dollars) +" dollar(s)") #print to user
            print("You get " + str(quarters) +" quarter(s)") #...
            print("You get " + str(dimes) +" dime(s)") #...
            print("You get " + str(nickels) +" nickel(s)") #...
            print("You get " + str(pennies) +" pennies") #...
            exit() #program is finished
    else: #If the input for cost is not a number, it exits
        print("Please enter a valid number! Try again.")
        exit()
else: #If the input for wallet is not a number, it exits
    print("Please enter a valid number! Try again.")
    exit()
