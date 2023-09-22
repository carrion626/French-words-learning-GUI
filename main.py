from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# CVS Working_______________________

try:
    data = pandas.read_csv('./data/to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    dd = original_data.to_dict(orient='records')
else:
    dd = pandas.DataFrame(data=data).to_dict(orient='records')


def words():
    canvas.itemconfig(image_change, image=image_front)
    global rand_card
    rand_card = random.choice(dd)
    fr_value = rand_card['French']
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=fr_value, fill='black')

    def english_word():
        en_value = rand_card['English']
        canvas.itemconfig(card_title, text='English', fill='white')
        canvas.itemconfig(card_word, text=en_value, fill='white')
        canvas.itemconfig(image_change, image=image_back)

    window.after(3000, english_word)


def is_known():
    dd.remove(rand_card)
    print(len(dd))
    dataaa = pandas.DataFrame(dd)
    dataaa.to_csv('./data/to_learn.csv', index=False)
    words()


# UI_________________________________
window = Tk()
window.config(width=1000, height=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
image_front = PhotoImage(file='./images/card_front.png')
image_change = canvas.create_image(400, 263, image=image_front)
image_back = PhotoImage(file='./images/card_back.png')

card_title = canvas.create_text(400, 150, text='', font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

canvas.grid(column=1, row=1, columnspan=2)

# Buttons______________________________
no = PhotoImage(file='./images/wrong.png')
button_no = Button(image=no, highlightthickness=0, command=words)
button_no.grid(column=1, row=2)

yes = PhotoImage(file='./images/right.png')
button_yes = Button(image=yes, highlightthickness=0, command=is_known)
button_yes.grid(column=2, row=2)

words()

window.mainloop()
