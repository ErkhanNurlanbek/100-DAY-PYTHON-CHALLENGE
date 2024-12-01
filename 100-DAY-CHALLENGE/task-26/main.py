import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = data.to_dict()
phonetic_alp = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_alp)

user_inp = input('What do you want to encrypt?')
users_list = [letter.upper() for letter in user_inp]
encrypted_input = [phonetic_alp[letter] for letter in users_list]
print(encrypted_input)