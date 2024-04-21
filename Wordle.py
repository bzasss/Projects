from tkinter import *
import requests
import re
import random


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def random_word():
    clear_window()
    label = Label(root, text="Enter how many letters you want the word to have")
    label.pack()
    number_entry = Entry(root, validate="key", validatecommand=(root.register(validate_number), '%P'))
    number_entry.pack()
    number_entry.focus_set()
    submit_button = Button(root, text="Submit", command=lambda: new_word(number_entry.get()))
    submit_button.pack()


def validate_number(value):
    if value.isdigit() or value == "":
        return True
    else:
        return False


def game_won():
    label_game_won = Label(root, text=str(guesses) + " guesses")
    start_again_button = Button(root, text="Start Again", command=lambda: new_game())
    label_game_won.grid(row=guesses, column=0, columnspan=number_of_letters)
    start_again_button.grid(row=guesses+1, column=0, columnspan=number_of_letters)


def string_to_table(input_string):
    table = [[char] for char in input_string]
    return table


def submit_entry(event):
    global guesses
    number_of_greens = 0
    secret_word_table = string_to_table(secret_word)
    guesses += 1
    slice_from = (guesses-1)*number_of_letters
    number_entry = -1
    colors = []
    for entry_widget in entry_widgets[slice_from:]:
        current_character = entry_widget.get()
        colors.append("grey")
        int(number_entry)
        number_entry += 1
        if current_character == secret_word_table[number_entry][0]:
            colors.pop()
            colors.append("green")
            number_of_greens += 1
            secret_word_table[number_entry] = " "
        else:
            tmp_no = 0
            for guess in secret_word_table:
                if guess[0] == current_character:
                    colors.pop()
                    colors.append("yellow")
                    secret_word_table[tmp_no] = " "
                    break
                tmp_no += 1
    colors.reverse()
    for entry_widget in entry_widgets[slice_from:]:
        entry_widget.config(readonlybackground=colors.pop(), fg="black", state="readonly")
    if number_of_greens == number_of_letters:
        game_won()
    else:
        new_line()


def new_line():
    for i in range(number_of_letters):
        entry = Entry(root, width=2, validate="key", validatecommand=(root.register(is_character), '%P'))
        entry.bind('<Return>', submit_entry)
        entry.grid(row=guesses, column=i, sticky=W)
        entry_widgets.append(entry)
    root.grid_slaves(row=guesses, column=0)[0].focus_set()


def start_the_actual_game():
    global guesses
    global entry_widgets
    guesses = 0
    clear_window()
    entry_widgets = []
    new_line()


def is_character(letter):
    return len(letter) == 1 or letter == ""


def new_word(number):
    if number == "":
        random_word()
        print("The value cannot be empty")
        return
    clear_window()
    global number_of_letters
    global secret_word

    number_of_letters = int(number)

    try:
        response = requests.get(f"https://meaningpedia.com/{number_of_letters}-letter-words?show=all")
        if response.status_code != 200:
            print("We do not have a database for words with the given length.")
            return
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)
        return
    word_list_collection = response.text
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    word_list = pattern.findall(word_list_collection)
    if not word_list:
        print("No words found in the database for the given length.")
        random_word()
        return

    secret_word = random.choice(word_list)
    start_the_actual_game()


def chosen_word(param):
    clear_window()
    global number_of_letters
    global secret_word
    secret_word = param
    number_of_letters = len(param)
    start_the_actual_game()


def choose_word():
    clear_window()
    label = Label(root, text="choose a word")
    label.pack()
    text_entry = Entry(root, validate="key")
    text_entry.pack()
    submit_button = Button(root, text="Submit", command=lambda: chosen_word(text_entry.get()))
    submit_button.pack()


def new_game():
    clear_window()
    button_random_word = Button(root, text="Random Word", command=random_word)
    button_choose_word = Button(root, text="Choose Word", command=choose_word)
    button_random_word.pack()
    button_choose_word.pack()


def start_game():
    global root
    root = Tk()
    root.title("Wordle")
    new_game()
    root.mainloop()


start_game()
