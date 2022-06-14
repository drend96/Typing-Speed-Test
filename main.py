from tkinter import *
import math
from word_list import words
import random

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TIMER = None


################# FUNCTIONS #################
# BIKIN FUNCTION UNTUK VALIDATE ENTRY
# def callback(typed_text):
#     user_entry = ""
#     if typed_text == " ":
#         user_entry = typed_text
#         add_word(typed_text)
#         return False
#
#     elif typed_text == str:
#         user_entry = typed_text
#         print(user_entry)
#         return True
#
#     else:
#         print(user_entry)
#         return False


def add_word(event=None):
    global current_word_index
    typed_text = typing_entry.get()
    current_word_index += 1

    print(typed_text)
    user_typed_text_list.append(typed_text.replace(" ",""))

    print(user_typed_text_list)
    clear_entry_text()

    if current_word_index % 9 == 0:
        canvas.itemconfig(word_box_text, text=words_to_type[current_word_index:current_word_index+10])

    current_word_label.config(text=words_to_type[current_word_index])

def clear_entry_text():
    typing_entry.delete(0,END)

def restart():
    global words_to_type, current_word_index
    window.after_cancel(TIMER)
    words_to_type = random.sample(words, 150)
    current_word_index = 0

    canvas.itemconfig(word_box_text, text=words_to_type[:10])
    timer_count_label.config(text="01:00")
    typing_entry.config(state="normal")

    current_word_label.config(text=words_to_type[0])


def start_time(event=None):
    window.after_cancel(count_down)

    count_down(60)
    window.after(60000, test_end)


def count_down(count):

    count_min = math.floor(count / 60)
    if count_min in range(0, 10):
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    timer_count_label.config(text=f"{count_min}:{count_sec}")

    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)


def test_end():
    cpm = len(''.join(user_typed_text_list))
    wpm = len(user_typed_text_list)
    wpm_correct = 0

    for position in range(0,len(user_typed_text_list)):
        if user_typed_text_list[position] == words_to_type[position]:
            wpm_correct += 1

    canvas.itemconfig(word_box_text, text=f"Your Score:\nCPM:{cpm}\nWPM:{wpm}\nYour accuracy is: {wpm_correct} out of the total {wpm} words typed.")
    typing_entry.config(state="disabled")

################# CODES #################

window = Tk()
window.title('Typing Test')
window.config(padx=50, pady=50, bg=YELLOW)

############ BAGIAN UNTUK TARUH VARIABLE #############
user_typed_text_list = []
words_to_type = random.sample(words,150)

current_word_index = 0

print(words_to_type)

canvas = Canvas(width=400, height=200, bg='white', highlightthickness=0)
word_box_text = canvas.create_text(200, 20, width=380, anchor='n',
                                   text=words_to_type[:10],
                                   fill="black", font=(FONT_NAME, 20, "bold"))

canvas.grid(column=0, row=5, pady=40, columnspan=2)

title_label = Label(text="Typing Speed Test", anchor='center', fg='black', bg=YELLOW, font=(FONT_NAME, 20, "bold"))
title_label.grid(column=0, row=0, columnspan=2)

timer_label = Label(text="Timer", anchor='center', fg='black', bg=YELLOW, font=(FONT_NAME, 20, "bold"), pady=30)
timer_label.grid(column=0, row=1)

timer_count_label = Label(text="01:00", anchor='center', fg='black', bg=YELLOW, font=(FONT_NAME, 20, "bold"), pady=30)
timer_count_label.grid(column=1, row=1)

start_button = Button(text='START', width=25, command=start_time, pady=20, padx=20)
start_button.grid(row=2, column=0, columnspan=1)

start_button = Button(text='RESTART', width=25, command=restart, pady=20, padx=20)
start_button.grid(row=2, column=1, columnspan=1)

empty_label = Label(text="\n", bg=YELLOW)
empty_label.grid(row=3, column=0)

current_word_label = Label(text=words_to_type[0], anchor='center', fg=YELLOW, bg=GREEN, font=(FONT_NAME, 20, "bold"), pady=30)
current_word_label.grid(row=4, column=0, columnspan=2)

type_value = StringVar()
typing_entry = Entry(width=30, textvariable=type_value, font=50)
typing_entry.grid(column=0, row=6, columnspan=2, rowspan=2)

# pake bind space key di bawah ini buat tambahkan kata yang benar ke dalam list.

window.bind("<space>", add_word)

window.mainloop()
