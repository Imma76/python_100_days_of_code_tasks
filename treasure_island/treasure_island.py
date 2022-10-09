print("Welcome to treasure Island, your mission is to find the treasure")
direction = input("left or right").lower()


if direction == 'left':
    direction2 = input('swim or wait').lower()
    if direction2 == 'wait':
        direction3 = input('Which door? Red, blue or yellow').lower()
        if direction3 == 'red':
            print('Burned by fire, game over!!')
        elif direction3 == 'blue':
            print('Eaten by beasts game over')
        elif direction3 == 'yellow':
            print('you win!')
        else:
            print('Game Over!')
    else:
        print('Attacked by trout game over!')
else:
    print('Fell into a hole game over!!')
