from tkinter import *
from tkinter import filedialog

root = Tk()

def open_file():
    file_name = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Text file", "*.txt"),))
    with open(file_name, 'r') as file:
        data = file.read()
    print(data)

Button(root, text = 'Click me !', command = open_file).pack()

root.mainloop()


