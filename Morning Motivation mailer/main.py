#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="pratham.jaiswal2004@gmail.com", msg="This is a Test Email.")
import random
import smtplib

# import datetime as dt

my_email = "prathamjaiswal204@gmail.com"
password = "rhhxzirrnqoisxbi"
reciever = "prathamjaiswal204@gmail.com"

word_list = ["Fresh", "Super", "Amazing", "Fantastic", "Enthusiastic", "Optimistic", "Positive", "Bright", "Awakening",
             "Rejuvenating", "Energizing", "Enlivening", "Invigorating"]
# day_of_week = now.weekday()
with open("quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    try:
        with open("count.txt", mode="r+") as count:
            quote_count = int(count.read())
            # print("Day:", quote_count)
    except:
        with open("count.txt", mode="w") as count:
            count.write("0")

    finally:
        with open("count.txt", mode="r+") as count:
            quote_count = int(count.read())
            # print("Day:", quote_count)

        with open("count.txt", mode="w") as count:
            if quote_count < len(all_quotes) - 1:
                count.write(str(quote_count + 1))
                quote = f"Day: {quote_count}\n\n{all_quotes[quote_count]}"
            else:
                count.write(str(0))
                quote = (f"\n{all_quotes[quote_count]}\n\nWell done! It's Day {quote_count}. Restarting from "
                         f"tomorrow ;)")
        print(quote)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=password)
        #     connection.sendmail(from_addr=my_email, to_addrs=reciever,
        #                         msg=f"Subject: Your {random.choice(word_list)} Morning Starter!\n\n{quote}")
        #     connection.close()
