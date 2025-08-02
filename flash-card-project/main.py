from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None

# --------------------------- DATA LOAD ------------------------------ #
try:
    file = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file = read_csv("data/french_words.csv")

to_learn = file.to_dict(orient="records")
word_dict = {}

# --------------------- CREATE NEW FLASH CARDS ------------------------ #
def new_random_word():
    global word_dict, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text, fill="black")
    canvas.itemconfig(word_text, fill="black")

    word_dict = choice(to_learn)

    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=word_dict["French"])

    flip_timer = window.after(3000, flip_card)

# ------------------------- FLIP THE CARDS ---------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)

    canvas.itemconfig(title_text, fill="white")
    canvas.itemconfig(word_text, fill="white")

    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=word_dict["English"])

# ------------------------- SAVE PROGRESS ---------------------------- #
def is_known():
    to_learn.remove(word_dict)

    new_data = DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    new_random_word()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, sticky="ew")

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=new_random_word)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0,command=is_known)
right.grid(row=1, column=1)

new_random_word()
window.mainloop()


