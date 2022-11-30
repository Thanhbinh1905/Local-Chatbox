from tkinter import *
import chat1
root = Tk()
root.title("Chatbox2")
root.geometry('600x450')
root['bg'] = '#FBB3D5'
# root.attributes('-rootmost',True) #alwaysonscreen
root.resizable(width=False,height=False)
lst=Listbox(root,width=94, height=21, bd=3)
# def retrieve_input():
#     if(textBox.get("1.0","end-1c")!=""):
#         lst.insert(END, "User2: " +textBox.get("1.0","end-1c"))
lst.place(x=5, y=5)
sbar = Scrollbar(root,orient=VERTICAL,width=15)
sbar.place(x=580,y=5,height=344)
lst.config(yscrollcommand = sbar.set)
sbar.config(command=lst.yview)
textBox=Text(root, height=5, width=63, bd=3)
textBox.place(x=5,y=353)
# buttonCommit=Button(root, height=1, width=9, text="Gửi", command=lambda: retrieve_input())
# buttonCommit.place(x=520,y=353)
