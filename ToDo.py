import tkinter as tk
window = tk.Tk()
window.title("To Do")
window.geometry("300x500")
titleFrame=tk.Frame(window).pack(side="top")
label=tk.Label(titleFrame,text="TASKS FOR TODAY",font=("Arial",20)).pack(side="top",expand=True,fill='x')

#Tasks GUI
tasksFrame=tk.Frame(window).pack()
taskList=[]
def addtask():
    text = entryTask.get()
    button=tk.Button(tasksFrame,text=text)
    taskList.append(button)
    for i in taskList:
        i.pack()


#Adding GUI
addFrame=tk.Frame(window).pack(side="bottom",fill='x',expand=True)
entryTask=tk.Entry(addFrame)
addbutton=tk.Button(addFrame,text="add",command=addtask)
entryTask.pack(side="left",fill='x',expand=True)
addbutton.pack(side="left",fill='x',expand=True)


window.mainloop()