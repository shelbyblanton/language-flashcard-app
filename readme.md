# Language Flash Card Application

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 31 of 100:* Flashcard App Capstone Project

## Project Specs

Using TkInter and the Pandas data library, develop a language learning flashcard application that displays a word in a foreign language for 3 seconds, then flips the card to the english translation.

The instructor used French as the language, but I used Portuguese as my husband is Brazilian. 

This application is written with Python 3.11.

![alt text](https://github-readme.s3.us-west-1.amazonaws.com/FlashCardApp.png)

### Main Features
The application displays a word in Portuguese for 3 seconds before it reveals the english translation. 

If a user guesses the word correctly, they click on the green checkmark to remove the word from card deck rotation. If they guessed incorrectly, they click on the red 'X' and the word remains in the card deck rotation.  

## Usage & Requirements

This project uses three libraries:
- TkInter
- Random
- Pandas

### Workflow
Words and translations are stored in a .csv file and read into Python using the Pandas library. A second .csv file is used to store words that the user clicked as missed: 

```
try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/portuguese_words.csv")
    to_learn = word_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")```
```

TkInter is used to create the application canvas, store button actions, and run the card flip timer:

```angular2html
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
```

# Getting Started

All of the commands below should be typed into the Python terminal of your IDE (I use PyCharm for my Python Development).

First, clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:shelbyblanton/strongminds_pizzapya.git
    
Then open the project in PyCharm.
    
In the `main.py` file, click on the word `pandas` in the import statement at the top of the page. Then click on the red exclamation point and click `Install Package Pandas` to load the library:

![alt text](https://github-readme.s3.us-west-1.amazonaws.com/Install-Pandas.png)

**Setup is complete!** 

Click Run in PyCharm to see the app in action.


# Author & Credits

Programmed by **[M. Shelby Blanton](https://www.linkedin.com/in/shelbyblanton/)** under the instructional guidance of **[Dr. Angela Yu](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)** via **[Udemy.com](udemy.com)**.
