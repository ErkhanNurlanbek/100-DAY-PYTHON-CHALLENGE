import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]
r_p_s = random.randint(0,2)
comp_rand_choice = rps[r_p_s]
players_input = int(input('Type 0 for rock, 1 for paper, 2 for scissors '))
players_choice = -1
if players_input == 0:
    players_choice = rock
elif players_input == 1:
    players_choice = paper
else:
    players_choice = scissors

print(players_choice)
print(comp_rand_choice)
if comp_rand_choice < players_choice:
    if comp_rand_choice == 0 and players_choice != 2:
        print('You win!')
    print('You win!')
elif comp_rand_choice == players_choice:
    print('It is a draw!')
else:
    print('You lose!')
