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
    huff = []
    for key in freqe:
        huff.append(Node(key,freqe[key]))
    
    return huff

class Node:

    def __init__(self,propability,letter,left_child = NONE, right_child = NONE,binary = 0):
        self.propability = propability
        self.letter = letter
        self.left_child = left_child
        self.right_child = right_child
        self.binary = binary


def create_huffman_tree(text):
    huff = freqency(text)

    while len(huff) > 1:
        huff = sorted(huff, key = lambda x: x.propability)
        right_node = huff[0]
        left_node = huff[1]
        right_node.binary = 1

        parent_node = Node(right_node.propability +left_node.propability, right_node.letter+left_node.letter, left_node, right_node)
        
        huff.append(parent_node)
        huff.remove(right_node)
        huff.remove(left_node)

    print(huff[0])








def open_file():
    file_name = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Text file", "*.txt"),))
    with open(file_name, 'r') as file:
        data = file.read()
    create_huffman_tree(data)


Button(root, text = 'Click me !', command = open_file).pack()




root.mainloop()


