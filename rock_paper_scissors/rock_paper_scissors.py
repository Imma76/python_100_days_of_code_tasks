import random
options = ['rock', 'paper','scissors']
system = random.choice(options)
end = False
while not end:
    my_choice = int(input('enter a number, 0 for rock, 1 for paper, 2 for scissors'))
    print(my_choice)
    print(system)
    if my_choice == 0 and system  == 'scissors':
        end = True
        print('you win')
    elif my_choice == 2 and system == 'paper':
        end = True
        print('you win')
    elif my_choice == 1 and system == 'rock':
        end = True
        print('You win')
    elif system == 'scissors' and my_choice  == 0:
        end = True
        print('you loose')
    elif system == 'paper' and my_choice == 2:
        end = True
        print('you loose')
    elif system == 'rock' and my_choice  == 1:
        end = True
        print('You loose')
