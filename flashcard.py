import os, random

count = 0
score = 0

file1 = open('series.txt', 'r')
file2 = open('character.txt', 'r')

f1content = file1.readlines()
f2content = file2.readlines()

while count < 8:
    os.system('clear')

    cardnum = random.randint(0, len(f1content)-1)

    print ('Series:', f1content[cardnum], '')

	#possibility of the same option many times?
    options = [random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1)]

    options[random.randint(0, 2)] = cardnum

    print ('1 -', f2content[options[0]],)
    print ('2 -', f2content[options[1]],)
    print ('3 -', f2content[options[2]],)

    answer = input('\nYour choice: ')

    if options[answer-1] == cardnum:
        raw_input('\nCorrect! Hit enter...')
        score = score + 1
    else:
        raw_input('\nWrong! Hit enter...')

    count = count + 1

print ('\nYour score is:', score)
