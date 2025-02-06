# 1. The problem asks me to create a program where students can input numerical grades, 
# convert them to letter grades, and calculate the average of all grades entered. 
# The program should repeat this process until the user decides to stop.

# the keywords and phrases are 
# Numerical grade
#Letter grade
#Average of grades
#Continuous input
#Convert numerical grade to letter grade
#Repeat process
#Show updated average and letter grade

# The program needs to take in numerical grades like  70 and 80 and 100 

# output: grade should match the number grade 

#  Initialize an empty list to store grades.
#Start a loop that runs indefinitely (until the user decides to exit).
#Prompt the user to enter a numerical grade.
#validate the input:
# - If the input is not a number or is outside the range 0-100, display an error message and ask for input again.
#Convert the numerical grade to a letter grade using the following scale:
# - 90-100: A
#- 80-89: B
# 70-79: C
#- 60-69: D
#- Below 60: F
#Display the letter grade for the entered numerical grade.
#Add the numerical grade to the list of grades.
#Calculate the average of all grades in the list.
#Convert the average to a letter grade using the same scale as above.
#Display the updated average and its corresponding letter grade.
#Ask the user if they want to enter another grade or exit.
#If the user chooses to exit, break the loop and end the program.



#make a 3-round Rock, Paper, Scissors game, figure out who wins each round, and say who wins overall.

# Key words 
# Rock, Paper, Scissors
#Random choice
#Best of 3

# Input: the player picks  rock, paper, or scissors.

# Output: gather results and declare the winner simple 

# Initialize user_score and computer_score to 0.
# Loop for 3 rounds:
#a. Ask the user to input "rock," "paper," or "scissors."
#b. Validate the input. If invalid, ask again.
#c. Randomly select "rock," "paper," or "scissors" for the computer.
#d. Compare user and computer choices:
#   - Rock beats scissors, scissors beats paper, paper beats rock.
#  - Update the score for the winner of the round.
#  - If it's a draw, do not update the score.
#e. Display the result of the round (win, loss, or draw).
# After 3 rounds, compare scores:
#a. If user_score > computer_score, declare the user as the winner.
#b. If computer_score > user_score, declare the computer as the winner.
#c. If scores are equal, declare it a tie.
# Game over and restart 
