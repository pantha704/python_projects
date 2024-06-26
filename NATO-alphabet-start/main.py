student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato[nato.letter == "A"])
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
word_list = [nato_dict[letter] for letter in word.upper()]
print(word_list)

# import numpy as np
#
# arr_2d = np.arange(50).reshape(5,10)
# print(arr_2d[2,1:4])
