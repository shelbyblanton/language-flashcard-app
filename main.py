from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(language, text="Portuguese", fill="black")
    canvas.itemconfig(card, image=card_back_q)
    canvas.itemconfig(word, text=f"{current_card['Portuguese']}", fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card, image=card_back_a)


def known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/portuguese_words.csv")
    to_learn = word_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_q = PhotoImage(file="images/card_front.png")
card_back_a = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_back_q)
language = canvas.create_text(400, 150, text="Portuguese", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0, command=known)
known_button.grid(column=1, row=1)

next_card()


window.mainloop()