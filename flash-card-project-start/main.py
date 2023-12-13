import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")

else:
    pass

finally:
    word_list_to_learn = df.to_dict(orient="records")
    word = None


def generate_card():
    global word, timer
    word = random.choice(word_list_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    timer = window.after(5000, func=answer_card)


def answer_card():
    global word
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")
    window.after_cancel(id=timer)


def right_option():
    global word_list_to_learn, word
    word_list_to_learn.remove(word)
    data = pd.DataFrame(word_list_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

    generate_card()


def wrong_option():
    generate_card()


# ---------------------- UI SETUP -------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating canvases
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Declaring image variables
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# Creating images & buttons & texts
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 153, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_img, command=right_option)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, command=wrong_option)
wrong_button.grid(row=1, column=0)

# ----------------------- WORD GENERATOR --------------------#


# Random word

generate_card()

window.mainloop()
