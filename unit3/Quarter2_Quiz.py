print ("A function is a type of code that completes a specific task.")

print("A function paramter is a varible in the def function that is used for when youre putting in data, while a function argument is the thing that is calling it essentially.")

print("A if/else conditional statement is a type of code that is used when theire can be diffrent outcomes.")

print("A integer data type is a numerical function used to place numbers.?")

print("A boolean data type is a form of comparing numbers in your code, whether its equal, greater than or less than")

print("I believe that the comparison operator is the best option because it is going to use the greater than or less than for the age. ")

print("Im pretty sure it is going to be the numeric operators as its using numbers. ?")

def passwordSystem(number):
    if number > 10:
        print( 'Your passowrd is too long, try again.')
    if number < 4:
        print('Your password is too short, try again.')
    if number > 4:
        print('Great, now that your passowrd is successfully created, you can move on!')
        
passwordSystem(7)

def federalTaxIncome(money):
    if money >= 0.00:
        print("You will be taxed 10% of your income and 3% for the state.")
    if money <= 12000.000:
        print("You will be taxed 10% of your income and 3% for the state")
    if money >= 12001.00:
        print("You will be taxed 12% of your income and 3% for the state")
    if money <= 500000.00:
        print("You will be taxed 12% of your income and 3% for the state")
    if money >= 500001.00:
        print("You will be taxed 22% of your income and 3% for the state")
    if money <= 103000.00:
        print("You will be taxed 22% of your income and 3% for the state")
    if money >= 103001.00:
        print("You will be taxe 23% of your income and 3% for the state")
    if money <= 198000.00:
        print("You will be taxed 23% of your income and 3% for the state")
        
federalTaxIncome(103222.00)