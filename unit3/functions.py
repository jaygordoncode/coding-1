# What is a function ?

# A function is a set of instructions that perfomrs a specific task or job. 

# here are two variations of functions in Python
# Built-in Functions- instructions that are pre-written in python progamming language
 
# print () is a bilt in fucntion. we pass it in data it will output it into the terminal automatically 
print('coding class')
# input() os a built in function. It allows us to write and pass in data into our program from the terminal.
name = input('what is your name?')

print(name)

number =int(input('please provide a number'))
print(23*number)

# User Defined Functions- custom functions written by engineers.

# Function Syntax - how it is written 

def sandwichInstructions():
    print('step 1. get 2 pieces  of bread ')
    print('step 2. putting ingredients inside of bread ')
    print(' step 3. put bread with ingredients together')
    
    # there are two states of a user defined function; the function definition, the function call
    
    #this is a fucntion call
    sandwichInstructions()