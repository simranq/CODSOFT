from tkinter import *
from PIL import Image, ImageTk
import messagebox

#-------------------------------------------CONSTANTS-------------------------------------------#

LABEL_BACKGROUND = "#D994FB"
BG_COLOR = "#D994FB"
BUTTON_COLOR = "#89BD21"

#-------------------------------------------FUNCTIONAL SETUP-------------------------------------------#

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_list.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Warning",message="You must enter a task first!")

def update_task():
    delete_task()
    add_task()


def delete_task():
    try:
        selected_task_index = tasks_list.curselection()[0]
        tasks_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning(title="Empty",message="Kindly select something to delete")

def save_tasks():
    tasks = tasks_list.get(0, tasks_list.size())
    with open ("tasks.txt", "w") as task_file:
        for task in tasks:
            task_file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt","r") as task_file:
            tasks = task_file.readlines()
            for task in tasks:
                tasks_list.insert(END, task.strip())
    except FileNotFoundError:
        messagebox.showerror("Add some tasks to view!")

#-------------------------------------------UI SETUP-------------------------------------------#

root = Tk()

#Background Image
bg_image = Image.open("bg-img.jpeg")
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = Label(root,image=bg_image)
bg_label.place(x=-50, y=-50)

#Title
root.title("To-Do List")
root.config(padx=30, pady=50, bg=BG_COLOR)
root.minsize(height=300,width=400)

#Label
label1 = Label(text="Enter task:",font="Georgia", fg="#604983")
label1.grid(row=0, columnspan=5)

#User-friendly task entry
task_entry = Entry(width=75)
task_entry.grid(row=1,columnspan=5)

#Frame, List and scrollbar consisting of tasks
frame_for_tasks = Frame(root)
frame_for_tasks.grid(row=3,columnspan=4)

tasks_list = Listbox(frame_for_tasks, height=10,width=75)
tasks_list.grid(row=3,columnspan=4)

tasks_scrollbar = Scrollbar(frame_for_tasks, orient=VERTICAL)
tasks_scrollbar.grid(row=3, column=5, sticky='ns')

tasks_list.config(yscrollcommand=tasks_scrollbar.set)
tasks_scrollbar.config(command=tasks_list.yview)

#Buttons

add_button = Button(highlightthickness=0, width=28, text="Add Task", bg=BUTTON_COLOR, command=add_task)
add_button.grid(row=2, column=2)

delete_button = Button(highlightthickness=0, width=28, text="Delete Task", bg=BUTTON_COLOR, command=delete_task)
delete_button.grid(row=2, column=3)

save_task_button = Button(highlightthickness=0, width=28, text="Save Task", bg =BUTTON_COLOR, command=save_tasks)
save_task_button.grid(row=5, column=2)

update_task_button = Button(highlightthickness=0, width=28, text="Update Task", bg=BUTTON_COLOR, command=update_task)
update_task_button.grid(row=5, column=3)
load_tasks()

root.mainloop()