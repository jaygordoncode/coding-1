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