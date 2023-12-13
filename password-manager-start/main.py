from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    global password_entry
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) <= 0:
        messagebox.showerror(title="Error", message="Enter the name of the website.")

    elif len(email) <= 0:
        messagebox.showerror(title="Error", message="Enter your email.")

    elif len(password) <= 0:
        messagebox.showerror(title="Error", message="Enter your Password.")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Trying to read old data
                data = json.load(data_file)

        except FileNotFoundError:
            # Creating a file named: "data.json"
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating new data inside the old one
            data.update(new_data)

            # Rewriting the updated data inside the json file...
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCHING WEBSITES ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)


    except FileNotFoundError:
        # data.json file missing
        messagebox.showerror(title=website, message="No data file found. Add some data first !")

    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"Email: {data[f'{website}']['email']}\nPassword: {data[f'{website}']['password']}")

        else:
            messagebox.showerror(title=website, message=f"No details for {website} exists.")

        # OR U CAN ALWAYS CHOOSE THE HARD WAY:
        #
        # for key in data:
        #     try:
        #         messagebox.showinfo(title=website,
        #                             message=f"Email: {data[f'{website}']['email']}\nPassword: {data[f'{website}']['password']}")
        #         break
        #
        #     except KeyError:
        #         # no website found
        #         messagebox.showerror(title=website, message=f"No details for {website} exists.")
        #         break
        #
        #     else:
        #         pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ", font=("Arial", 12, "normal"))
email_label = Label(text="Email/Username: ", font=("Arial", 12, "normal"))
password_label = Label(text="Password: ", font=("Arial", 12, "normal"))
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=21)
web_entry.focus()

email_entry = Entry(width=39)

password_entry = Entry(width=21)

web_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
gen_pass = Button(text="Generate Password", width=14, command=generate_pass)
add_button = Button(text="Add", width=33, command=add_info)
search_button.grid(row=1, column=2)
gen_pass.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
