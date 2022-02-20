import pandas

data= pandas.read_csv("Python/#100DaysOfCode/Day 26/NATO Alphabet Project/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word to convert to phonetic: ").upper()
final_list = [phonetic_dict[user_letter] for user_letter in user_word if user_letter in phonetic_dict]
print(final_list)