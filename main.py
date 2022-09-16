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
flashcard.grid(row=0, column=0)

flashcard.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
flashcard.create_text(600, 263, text="word", font=("Arial", 60, "bold"))

# back portion
card_back_img = PhotoImage(file="images/card_back.png")



window.mainloop()