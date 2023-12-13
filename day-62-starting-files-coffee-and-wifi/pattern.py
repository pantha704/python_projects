print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.upper()
name2 = name2.upper()

trues = 0
loves = 0

for char in name1:
    if char == "T" or char == "R" or char == "U" or char == "E":
        trues += 1
for char in name2:
    if char == "T" or char == "R" or char == "U" or char == "E":
        trues += 1

for char in name1:
    if char == "L" or char == "O" or char == "V" or char == "E":
        loves += 1
for char in name2:
    if char == "L" or char == "O" or char == "V" or char == "E":
        loves += 1

score = int(str(trues) + str(loves))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score <= 50 or score >= 40:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")