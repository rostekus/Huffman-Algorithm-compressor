from tkinter import *
from tkinter import filedialog

root = Tk()

def freqency(text):
    freqe = {}
    for ch in text:
    	if ch in freqe:
    		freqe[ch] += 1
    	else:
    		freqe[ch] =1
    print(freqe)


def open_file():
    file_name = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Text file", "*.txt"),))
    with open(file_name, 'r') as file:
        data = file.read()
    freqency("gfbhdjnkms")


Button(root, text = 'Click me !', command = open_file).pack()




root.mainloop()


