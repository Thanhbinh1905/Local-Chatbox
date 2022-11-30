from tkinter import *
import chat1
import chat2
#------------------------------------------------------------------------------------------------------
#Send Message to other boxchat
def retrieve_input1():
    if(chat1.textBox.get("1.0","end-1c")!=""):
        chat1.lst.insert(chat1.END, "User1: " +chat1.textBox.get("1.0","end-1c"))
        chat2.lst.insert(chat2.END, "User1: " +chat1.textBox.get("1.0","end-1c"))
        chat1.textBox.delete('1.0', END)
def retrieve_input2():
    if(chat2.textBox.get("1.0","end-1c")!=""):
        chat1.lst.insert(chat1.END, "User2: " +chat2.textBox.get("1.0","end-1c"))
        chat2.lst.insert(chat2.END, "User2: " +chat2.textBox.get("1.0","end-1c"))
        chat2.textBox.delete('1.0', END)
chat1.buttonCommit = Button(chat1.top, height=1, width=9, text="Gửi", command=lambda: retrieve_input1())
chat1.buttonCommit.place(x=520,y=353)
chat2.buttonCommit = Button(chat2.root, height=1, width=9, text="Gửi", command=lambda: retrieve_input2())
chat2.buttonCommit.place(x=520,y=353)
#------------------------------------------------------------------------------------------------------
# DeleteMessage
def delete_message1():
    chat1.lst.delete(0, END)
def delete_message2():
    chat2.lst.delete(0, END)
chat1.delbut = Button(chat1.top, height=1, width=9, text="Xóa", command=lambda: delete_message1())
chat1.delbut.place(x=520,y=381)
chat2.delbut = Button(chat2.root, height=1, width=9, text="Xóa", command=lambda: delete_message2())
chat2.delbut.place(x=520,y=381)
#------------------------------------------------------------------------------------------------------
chat1.top.mainloop()
chat2.root.mainloop()

