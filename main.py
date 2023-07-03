import pandas

#TODO 1. Create a dictionary in this format:
nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row['letter']: row['code'] for (index, row) in nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input('Input a word to get it\'s nato phonetics ').upper()
output = [nato_alphabet_dict[letter] for letter in user_input]
print(output)

