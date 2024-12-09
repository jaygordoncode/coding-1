def reverse_word(word):
    return word[::-1]
#using return word shoudl turn it to the backwords saying of the word. 
print(reverse_word("pet")) 

print(reverse_word("book")) 



def state_landmark(state):
    state = state.lower()  
    if state == 'pennsylvania':
        return "A landmark in Pennsylvania is the Liberty Bell."
    elif state == 'new york':
        return "A landmark in New York is the Statue of Liberty."
    elif state == 'california':
        return "A landmark in California is the Hollywood Walk of Fame."
    elif state == 'south carolina':
        return "A landmark in South Carolina is Fort Sumter, where the initial shots of the American Civil War took place."
    elif state == 'oregon':
        return "A landmark in Oregon is Crater Lake, the deepest lake in the United States and a popular destination for hiking and boating."
    else:
        return "Sorry ! the state you entered could not be found."