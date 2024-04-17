from tkinter import *
from random import randint

score = 0
is_game_over = False


def is_this_space_empty(label):
    return label.cget("text") == " "


def down_key(event):
    if not is_game_over:
        down_key_pressed(event)
        merge_down(event)
        down_key_pressed(event)
        add_new_number()
        add_new_number()
    else:
        end_game_score()


def up_key(event):
    if not is_game_over:
        up_key_pressed(event)
        merge_up(event)
        up_key_pressed(event)
        add_new_number()
        add_new_number()
    else:
        end_game_score()


def left_key(event):
    if not is_game_over:
        left_key_pressed(event)
        merge_left(event)
        left_key_pressed(event)
        add_new_number()
        add_new_number()
    else:
        end_game_score()


def right_key(event):
    if not is_game_over:
        right_key_pressed(event)
        merge_right(event)
        right_key_pressed(event)
        add_new_number()
        add_new_number()
    else:
        end_game_score()



def merge_down(event):
    global labels
    global score
    print("merging")
    for i in range(4):
        previous_number = 0
        for j in range(3, -1, -1):
            current_number = labels[i][j].cget("text")
            if previous_number == current_number != " ":
                new_number = (int(current_number))*2
                score += int(current_number)
                update_score_label()
                labels[i][j+1].config(text=new_number)
                labels[i][j].config(text=" ")
            previous_number = current_number


def merge_up(event):
    global labels
    global score
    print("merging")
    for i in range(4):
        previous_number = 0
        for j in range(4):
            current_number = labels[i][j].cget("text")
            if previous_number == current_number != " ":
                new_number = (int(current_number))*2
                score += int(current_number)
                update_score_label()
                labels[i][j-1].config(text=new_number)
                labels[i][j].config(text=" ")
            previous_number = current_number


def merge_left(event):
    global labels
    global score
    print("merging")
    for j in range(4):
        previous_number = 0
        for i in range(4):
            current_number = labels[i][j].cget("text")
            if previous_number == current_number != " ":
                new_number = (int(current_number)) * 2
                score += int(current_number)
                update_score_label()
                labels[i-1][j].config(text=new_number)
                labels[i][j].config(text=" ")
            previous_number = current_number


def merge_right(event):
    global labels
    global score
    print("merging")
    for j in range(4):
        previous_number = 0
        for i in range(3, -1, -1):
            current_number = labels[i][j].cget("text")
            if previous_number == current_number != " ":
                new_number = (int(current_number)) * 2
                score += int(current_number)
                update_score_label()
                labels[i+1][j].config(text=new_number)
                labels[i][j].config(text=" ")
            previous_number = current_number


def add_new_number():
    global labels
    free_spaces = []
    for r in range(4):
        for c in range(4):
            label_tmp = labels[r][c]
            if is_this_space_empty(label_tmp):
                free_spaces.append(str(r) + str(c))

    number_of_free_spaces = len(free_spaces)
    if number_of_free_spaces > 0:
        random_index = randint(0, number_of_free_spaces - 1)
        random_free_space = free_spaces[random_index]
        r, c = int(random_free_space[0]), int(random_free_space[1])
        labels[r][c].config(text="2")
    else:
        print("No free spaces available")
        global is_game_over
        is_game_over = True


def down_key_pressed(event):
    global labels
    print("pressed")
    is_finished = False
    while not is_finished:
        is_finished = True
        for i in range(4):
            is_previous_space_empty = False
            for j in range(3, -1, -1):
                label_tmp = labels[i][j]
                if is_previous_space_empty and not is_this_space_empty(label_tmp):
                    labels[i][j+1].config(text=label_tmp.cget("text"))
                    labels[i][j].config(text=" ")
                    is_finished = False
                is_previous_space_empty = is_this_space_empty(label_tmp)


def up_key_pressed(event):
    global labels
    print("pressed")
    is_finished = False
    while not is_finished:
        is_finished = True
        for i in range(4):
            is_previous_space_empty = False
            for j in range(4):
                label_tmp = labels[i][j]
                if is_previous_space_empty and not is_this_space_empty(label_tmp):
                    labels[i][j-1].config(text=label_tmp.cget("text"))
                    labels[i][j].config(text=" ")
                    is_finished = False
                is_previous_space_empty = is_this_space_empty(label_tmp)


def left_key_pressed(event):
    global labels
    print("pressed")
    is_finished = False
    while not is_finished:
        is_finished = True
        for j in range(4):
            is_previous_space_empty = False
            for i in range(4):
                label_tmp = labels[i][j]
                if is_previous_space_empty and not is_this_space_empty(label_tmp):
                    labels[i-1][j].config(text=label_tmp.cget("text"))
                    labels[i][j].config(text=" ")
                    is_finished = False
                is_previous_space_empty = is_this_space_empty(label_tmp)


def right_key_pressed(event):
    global labels
    print("pressed")
    is_finished = False
    while not is_finished:
        is_finished = True
        for j in range(4):
            is_previous_space_empty = False
            for i in range(3, -1, -1):
                label_tmp = labels[i][j]
                if is_previous_space_empty and not is_this_space_empty(label_tmp):
                    labels[i+1][j].config(text=label_tmp.cget("text"))
                    labels[i][j].config(text=" ")
                    is_finished = False
                is_previous_space_empty = is_this_space_empty(label_tmp)


def update_score_label():
    global score
    score_label.config(text="Score: " + str(score))


def end_game_score():
    global score
    score_label.config(text="GAME OVER\nScore: " + str(score))

root = Tk()
root.bind('<Down>', down_key)
root.bind('<Up>', up_key)
root.bind('<Left>', left_key)
root.bind('<Right>', right_key)
labels = [[None] * 4 for _ in range(4)]
b = 0
for r in range(4):
    for c in range(4):
        b = b + 1
        label_tmp = Label(
            root,
            text=" ",
            borderwidth=3,
            bg="dark grey",
            width=6,
            height=3,
            highlightbackground="grey",
            highlightthickness=1
        )
        label_tmp.grid(row=r, column=c)
        labels[c][r] = label_tmp
score_label = Label(root, text="Score: " + str(score))
score_label.grid(row=5, columnspan=4)
add_new_number()
add_new_number()
root.mainloop()
