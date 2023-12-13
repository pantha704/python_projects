#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

letter_file = open("./Input/Letters/starting_letter.txt", mode="r")

name_file = open("./Input/Names/invited_names.txt", "r")

names = name_file.readlines()

letter = letter_file.read()
for name in names:
    name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, name)
    completed_letter = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")
    completed_letter.write(new_letter)