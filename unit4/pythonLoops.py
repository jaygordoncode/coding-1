def gradeToTitle(year):
year = input(What year are youn in?)
if year == 1:
    print('you are a freshman in undergrad')
elif year == 2:
    print('you are a sophmore in undergrad')
elif year == 3:
    print('you are a junior in undergrad')
elif year == 4:
    print('you are a senior in undergrad')
elif year == 5 or year == 6:
    print('you are in the masters program and in grad school')
elif year >= 7 and year <= 10: 
    print'you are in a doctorates program and in grad school)
elif year >11:
    print(' aye bro you need to get a job like you been in school too long broski')
else:
    print('Err: something went wrong. please check you in)')
gradeToTitle(3)