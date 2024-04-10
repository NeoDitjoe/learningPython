num = int(input('enter number? '))
tries = 0
limit = 3

while tries < limit:
    guess_num = int(input('Guess: '))
    if tries >= 3:
        print('GameOver You lose!')
        break
    elif num == guess_num:
        print('Good Game You WIN!!!')
        break
    else:
        tries += 1