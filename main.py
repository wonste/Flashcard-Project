from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# initialize module and set up the ui window
window = Tk()
window.title("Deck This")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create the card and front portion
flashcard = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
flashcard.create_image(400, 263, image=card_front_img)

flashcard.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard.grid(row=0, column=0, columnspan=2)

flashcard.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
flashcard.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")

# buttons
cross = PhotoImage(file="images/wrong.png")
error_button = Button(image=cross, highlightthickness=0)
error_button.grid(row=1, column=0)

check = PhotoImage(file="images/right.png")
yes_button = Button(image=check, highlightthickness=0)
yes_button.grid(row=1, column=1)

window.mainloop()