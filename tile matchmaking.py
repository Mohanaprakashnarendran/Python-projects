import tkinter
from tkinter import*
from tkinter import messagebox
import random
m=tkinter.Tk()
m.geometry("1200x1200")
m.title("puzzle")
m.config(bg='skyblue')
matches=[1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)

frame=Frame(m)
frame.pack(pady=50)



##define variables
count=0 
answer_list=[]
answer_dict={}
def click(b,number):
    global count,answer_list,answer_dict
    if b["text"]==" " and count<2:
        b["text"]=matches[number]
        answer_list.append(number)
        answer_dict[b]=matches[number]
        count+=1
##determine it is right or not:        
    if len(answer_list)==2:
        if matches[answer_list[0]]==matches[answer_list[1]]:
            my_label.config(text="match")
            for key in answer_dict:
                key["state"]="disabled"
            count=0
            answer_list=[]
            answer_dict={}
        else:
            my_label.config(text="mismatch")
            count=0
            answer_list=[]
            messagebox.showinfo("Opps","Incorrect")
##          reset the button  
            for key in answer_dict:
                key["text"]=" "
            answer_dict={}
##buttons
b0=Button(frame,text=" ",height=10,width=10,command=lambda:click(b0,0))
b1=Button(frame,text=" ",height=10,width=10,command=lambda:click(b1,1))
b2=Button(frame,text=" ",height=10,width=10,command=lambda:click(b2,2))
b3=Button(frame,text=" ",height=10,width=10,command=lambda:click(b3,3))
b4=Button(frame,text=" ",height=10,width=10,command=lambda:click(b4,4))
b5=Button(frame,text=" ",height=10,width=10,command=lambda:click(b5,5))
b6=Button(frame,text=" ",height=10,width=10,command=lambda:click(b6,6))
b7=Button(frame,text=" ",height=10,width=10,command=lambda:click(b7,7))
b8=Button(frame,text=" ",height=10,width=10,command=lambda:click(b8,8))
b9=Button(frame,text=" ",height=10,width=10,command=lambda:click(b9,9))
b10=Button(frame,text=" ",height=10,width=10,command=lambda:click(b10,10))
b11=Button(frame,text=" ",height=10,width=10,command=lambda:click(b11,11))

## grid our button
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

my_label=Label(m,text='')
my_label.pack(pady=20)



m.mainloop()
