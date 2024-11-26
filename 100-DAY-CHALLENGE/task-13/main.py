import game_data
import art
import random


def randomize():
    return game_data.data[random.randint(0, 49)]


correct = True
score = 0
correct_ans = ''
a = randomize()
a_fol_count = a['follower_count']

while correct:
    b = randomize()
    b_fol_count = b['follower_count']
    while a == b:
        b = randomize()

    if a_fol_count > b_fol_count:
        correct_ans = 'a'
    elif b_fol_count > a_fol_count:
        correct_ans = 'b'

    print(art.logo)
    print(correct_ans)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f'Compare A: {a['name']}, a {a['description']}, from {a['country']}')
    print(art.vs)
    print(f'Against B: {b['name']}, a {b['description']}, from {b['country']}')
    user_inp = input('Who has more followers? Type A or B: ').lower()
    if user_inp == str(correct_ans):
        score += 1
        a_fol_count = a['follower_count']
        print('\n' * 25)
        if correct_ans == 'b':
            a = b
    else:
        print('\n' * 30)
        correct = False
        print(art.logo)
        print(f'Sorry, that is wrong! Final score: {score}')

