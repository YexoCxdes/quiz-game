print('Welcome to my computer quiz! -- Yexo')

playing = input('Would you like to play? (y/n) : ')
count = 0
if playing != 'y':
    exit()

answer = input('What does RAM stand for?\n')

if answer == 'random access memory':
    count += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('What does CPU stand for?\n')

if answer == 'central proccessing unit':
    count += 1
    print('Correct!')
else:
    print('Incorrect!')