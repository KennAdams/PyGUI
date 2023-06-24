import tkinter as tk

window=tk.Tk(screenName="Calc")
window.resizable(500, 400)
window.columnconfigure(0, weight=5)
window.columnconfigure(1, weight=5)
window.columnconfigure(2, weight=5)
window.columnconfigure(3, weight=5)


result=tk.StringVar()
def press(str):
    sth=result.get()
    result.set(sth+str)
    print(sth,"::",sth,"::",eval(sth+str))
def equal():
    try:
        result.set(str(eval(result.get())))
    except:
        result.set("error")

def AC():
    result.set("")
num1button=tk.Button(window,text="1",background="white",foreground="black",command=lambda: press('1'), height=1, width=3)
num2button=tk.Button(window,text="2",background="white",foreground="black",command=lambda: press('2'), height=1, width=3)
num3button=tk.Button(window,text="3",background="white",foreground="black",command=lambda: press('3'), height=1, width=3)
num4button=tk.Button(window,text="4",background="white",foreground="black",command=lambda: press('4'), height=1, width=3)
num5button=tk.Button(window,text="5",background="white",foreground="black",command=lambda: press('5'), height=1, width=3)
num6button=tk.Button(window,text="6",background="white",foreground="black",command=lambda: press('6'), height=1, width=3)
num7button=tk.Button(window,text="7",background="white",foreground="black",command=lambda: press('7'), height=1, width=3)
num8button=tk.Button(window,text="8",background="white",foreground="black",command=lambda: press('8'), height=1, width=3)
num9button=tk.Button(window,text="9",background="white",foreground="black",command=lambda: press('9'), height=1, width=3)
num0button=tk.Button(window,text="0",background="white",foreground="black",command=lambda: press('0'), height=1, width=10)
add_button=tk.Button(window,text="+",background="grey",foreground="black",command=lambda: press('+'), height=1, width=3)
minus_button=tk.Button(window,text="-",background="grey",foreground="black",command=lambda: press('-'), height=1, width=3)
multiply_button=tk.Button(window,text="x",background="grey",foreground="black",command=lambda: press('*'), height=1, width=3)
divid_button=tk.Button(window,text="/",background="grey",foreground="black",command=lambda: press('/'), height=1, width=3)
equal_button=tk.Button(window,text="=",background="orange",foreground="black",command=equal, height=3, width=3)
clear_button=tk.Button(window,text="AC",background="grey",foreground="black",command=AC, height=1, width=10)
dot_button=tk.Button(window,text=".",foreground="black",command=lambda: press('.'), height=1, width=30)
display_box=tk.Entry(window,textvariable=result,background="white",foreground="black")
#GUI 
num0button.grid(column=0,row=5,columnspan=2)
dot_button.grid(column=2,row=5)
equal_button.grid(column=3,row=4,rowspan=2)
num1button.grid(column=0,row=4)
num2button.grid(column=1,row=4)
num3button.grid(column=2,row=4)
num4button.grid(column=0,row=3)
num5button.grid(column=1,row=3)
num6button.grid(column=2,row=3)
add_button.grid(column=3,row=3)
num7button.grid(column=0,row=2)
num8button.grid(column=1,row=2)
num9button.grid(column=2,row=2)
minus_button.grid(column=3,row=2)
clear_button.grid(column=2,columnspan=2,row=1)
multiply_button.grid(column=0,row=1)
divid_button.grid(column=1,row=1)
display_box.grid(column=0,row=0,columnspan=4,rowspan=1)


window.mainloop()