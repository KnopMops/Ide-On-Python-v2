from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import tkinter.scrolledtext
import subprocess
import sys
import platform

root = Tk()
root.title("KnopoCharm")
root.geometry("1300x720+150+80")
root.configure(bg="#323846")
root.resizable(False, False)

file_path = ''


def set_file_path(path):
    global file_path
    file_path = path
    if file_path != '':
        root.title(f'KnopoCharm - Python {platform.python_version()} {file_path}')


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])

    with open(path, 'r') as file:
        code = file.read()
        code_input.delete('1.0', END)
        code_input.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path

    with open(path, 'w') as file:
        code = code_input.get('1.0', END)
        file.write(code)
        set_file_path(path)
        messagebox.showinfo("KnopoCharm", 'Save success ')


def run_server():
    if file_path == '':
        messagebox.showerror('KnopoCharm', 'Please, save your file')
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.config(state='normal')
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)
    code_output.insert('1.0', f'==== {file_path} ====\n')
    code_output.config(state='disabled')


# icon
image_icon = PhotoImage(file="./img/logo.png")
root.iconphoto(False, image_icon)

# code input
code_input = tkinter.scrolledtext.ScrolledText(undo=True, font='consolas 20')
code_input.place(x=180, y=0, width=680, height=720)

# output
code_output = Text(root, font="cosolas 18", bg="#323846", fg="lightgreen")
code_output.place(x=860, y=0, width=440, height=720)
code_output.config(state='disabled')

# buttons

Open = PhotoImage(file="./img/open.png")
Save = PhotoImage(file="./img/save.png")
Run = PhotoImage(file="./img/run.png")

Button(root, image=Open, bg="#323846", bd=0, command=open_file).place(x=30, y=30)
Button(root, image=Save, bg="#323846", bd=0, command=save_as).place(x=30, y=145)
Button(root, image=Run, bg="#323846", bd=0, command=run_server).place(x=30, y=260)

root.mainloop()




