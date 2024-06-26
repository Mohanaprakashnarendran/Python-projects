from tkinter import*
from tkinter import messagebox



to=Tk()
to.title("TODO LIST")
to.geometry('1200x1200')
to.configure(bg="#326273")
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.") 
 
def deleteTask():
    lb.delete(ANCHOR)
    

frame = Frame(to)
frame.pack(pady=10)

lb = Listbox(frame,width=25,height=10,font=('Times', 18),bd=0,fg='#464646',
             selectbackground='#a6a6a6',activestyle="none")
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'complete assigment',
    'drink water',
    'go gym',
    'create software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas',
    'finish Asigments',
    ]
for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(to,font=('times', 20))


my_entry.pack(pady=20) 

button_frame = Frame(to)
button_frame.pack(pady=20) 

addTask_btn = Button(button_frame,text='Add Task',font=('times 14'), bg='#c5f776',padx=20,pady=10,command=newTask)
addTask_btn.pack( side=LEFT)

delTask_btn = Button(button_frame,text='Delete Task',font=('times 14'),bg='#ff8b61',padx=20,pady=10,command=deleteTask)
delTask_btn.pack( side=RIGHT)



to.mainloop()




