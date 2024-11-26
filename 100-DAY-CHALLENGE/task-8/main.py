import art

print(art.logo)
auction = True
biddersl = {}

while auction:
    name = input('What is your name? ')
    bill = int(input('What is your bid? $'))

    # Save the bid in the bidders dictionary
    biddersl[name] = bill

    y_or_n = input('Are there other bidders? (y/n)\n').lower()

    if y_or_n == 'n':
        # Determine the winner and their bid
        highest = -1
        winner = ''

        for key in biddersl:
            if biddersl[key] > highest:
                highest = biddersl[key]
                winner = key

        # Display the winner and their bid
        print(f'The winner is {winner}, with the price {highest}!')
        auction = False
    elif y_or_n == 'y':
        print('\n' * 25)