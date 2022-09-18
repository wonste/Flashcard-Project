from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# import data
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)

    # update card with title and new word
    canvas.itemconfig(title_card, text="French")
    canvas.itemconfig(content_card, text=current_card["French"])


# initialize module and set up the ui window
window = Tk()
window.title("Deck This")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create the card and front portion
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

title_card = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
content_card = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
cross = PhotoImage(file="images/wrong.png")
error_button = Button(image=cross, highlightthickness=0)
error_button.grid(row=1, column=0)

check = PhotoImage(file="images/right.png")
yes_button = Button(image=check, highlightthickness=0)
yes_button.grid(row=1, column=1)

next_card()

window.mainloop()
