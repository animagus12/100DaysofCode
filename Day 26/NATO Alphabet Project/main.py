import pandas

data= pandas.read_csv("Python/#100DaysOfCode/Day 26/NATO Alphabet Project/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generator():
    user_word = input("Enter a word to convert to phonetic: ").upper()
    try:
        final_list = [phonetic_dict[user_letter] for user_letter in user_word]
    except KeyError:
        print("Sorry, only letters in the word. Please!")
        generator()
    else:
        print(final_list)

generator()