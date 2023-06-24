import tkinter as tk
window = tk.Tk()
window.title("To Do")
window.geometry("300x500")
label=tk.Label(window,text="TASKS FOR TODAY",font=("Arial",20)).grid(column=0,columnspan=5,row=0)

#Tasks GUI
taskList=[]
gridmaxrow=tk.IntVar(value=2)
def addtask():
    text = entryTask.get()
    button=tk.Button(window,text=text)
    taskList.append(button)
    gridmaxrow.set(gridmaxrow.get()+1)
    for i in taskList:
        rw=taskList.index(i)
        i.grid(column=0,row=rw+1)
    entryTask.grid(column=0,columnspan=4,row=gridmaxrow.get()-1)
    addbutton.grid(column=4,row=gridmaxrow.get()-1)


#Adding GUI
entryTask=tk.Entry(window)
addbutton=tk.Button(window,text="add",command=addtask)
entryTask.grid(column=0,columnspan=4,row=gridmaxrow.get()-1)
addbutton.grid(column=4,row=gridmaxrow.get()-1)


window.mainloop()