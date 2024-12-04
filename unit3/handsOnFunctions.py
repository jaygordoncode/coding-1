# Discuss the anatomy of a function 

# A function definition tells the computer the instructions on what we want to do with it


# data = just means data types

# curly brackets - passing in data into the function definition. this is formally called a parameter 

# parameter = placeholder 

def modifyMyName(name):
    print('Your new modified name is the great '+ name )

# when we pass data into a function call it is called an argument 
# argument - evidence , facts , real data
modifyMyName('Jaylen')    
    
    
    # Lesson on conditional statements 
    # conditional statements use the 'IF' and 'ELSE' keywords to filter and create specific outcomes based on data
    
def verifyAge(age):
    if age > 17:
        print( 'congrats: you can buy GTA VI! ')
    else:
        print( 'Sorry, you need an adult to buy this game for you. Try again when you get older! ')
        
verifyAge(15)
verifyAge(19)

#Activity

def driversLicense(age):
    if age > 18:
        print( 'You are now able to take your drivers test and achieve your drivers license!')
    if age == 16:
        print('You are not old enough for a drivers license but you can obtain your drivers permit')
    else:
        print('Sorry, you are too young to drive. Make sure you have an adult with you at all times in a vehicle!')
        
driversLicense(27)


# Conditional statements. if/else keywords; gives us the ability to control outcomes and make decisions on data 

# food expiration software is an example of using conditional statements. if the food expires it needs to be thrown away
#otherwise, or else it can be eaten 

def foodExpiration(date):
    expirationDate = '12/5/24'
    if date == expirationDate:
        print('throw food away')
    else;
        print('food is still good')
        
foodExpiration('12/5/24')