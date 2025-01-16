#what are loops 
#python loop is a programming concept where code repeats itself under specific conditons 

# In, python, there are 2 versiosn of loops; forr loop and while loop 

# while loops - a type of loop that will repeat a set of insturctions as long as some condition is true 

hp = 100 
normalAttack =2
specialAttack = 4
increaseHealth = 3
def battleFunction():
    hp = 10
while hp >0:
    print('do you want to attack?')
    print(hp) 
    hp -= normalAttack
    if hp == 0:
        print('game over"')     
        ')