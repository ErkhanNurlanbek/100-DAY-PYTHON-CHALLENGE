import random
import art


def print_log(x, y):
    print(x)
    print(y)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score


playing = input('Do you want to play BlackJack? Type "y" for yes and "n" for no: ').lower()

if playing == 'y':
    print('\n' * 20)
    print(art.logo)

    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

    while True:
        if calculate_score(player_hand) == 21:
            print_log(calculate_score(player_hand), calculate_score(computer_hand))
            print("Blackjack! You win!")

        cont = input('Do you want to draw another card? Type "y" for yes and "n" for no: ').lower()
        if cont == 'y':
            player_hand.append(deal_card())
            print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
            if calculate_score(player_hand) > 21:
                print_log(calculate_score(player_hand), calculate_score(computer_hand))
                print("You went over. You lose!")
        else:
            break

    while calculate_score(computer_hand) < 17:
        computer_hand.append(deal_card())

    print_log(calculate_score(player_hand), calculate_score(computer_hand))

    if calculate_score(computer_hand) > 21 or calculate_score(player_hand) > calculate_score(computer_hand):
        print("You win!")
    elif calculate_score(player_hand) < calculate_score(computer_hand):
        print("You lose!")
    else:
        print("It's a draw!")

elif playing == 'n':
    print('Good choice mate, do not play this type of crap!')

