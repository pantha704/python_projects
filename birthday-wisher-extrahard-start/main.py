##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random, smtplib, pandas as pd, datetime as dt

MY_EMAIL = "prathamjaiswal204@gmail.com"
PASSWORD = "rhhxzirrnqoisxbi"

birthday_list = pd.read_csv("./birthdays.csv")
today = dt.datetime.now()
today_tuple = (today.month, today.day)
# dob = dt.datetime(year=1979, month=10, day=22)
# print(dob)
birthdays = pd.read_csv("birthdays.csv")
# print(birthdays)
birthday_dict = {(rows["month"], rows["day"]): rows for (index, rows) in birthdays.iterrows()}
# print(birthday_dict)

letter_list = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

if today_tuple in birthday_dict:
    with open(random.choice(letter_list)) as file:
        birthday_person = birthday_dict[today_tuple]
        # print(birthday_person)today.month
        letter = file.read().replace("[NAME]", birthday_person["name"]).replace("Angela", "Pratham")
        # print(letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f"Subject: Happy "
                                                                                           f"Birthday!"
                                                                                           f"\n\n{letter}")
            connection.close()
