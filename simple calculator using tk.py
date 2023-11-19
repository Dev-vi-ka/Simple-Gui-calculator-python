from tkinter import *



root = Tk()
root.title("Simple Calculator")
root.geometry("250x400")

scr = Entry(root, width=40)
scr.grid(row=0, column=0, columnspan=4)

def btn_num(val):
    current=scr.get()
    scr.delete(0,END)
    scr.insert(0, str(current) + str(val))
    
def clr_scr():
    scr.delete(0,END)
    
def btn_add():
    num=scr.get()
    scr.delete(0,END)
    global f_num
    f_num= int(num)
    global operation
    operation = "addition"
    
def btn_sub():
    num=scr.get()
    scr.delete(0,END)
    global f_num
    f_num= int(num)
    global operation
    operation = "subtraction"
    
def btn_mult():
    num=scr.get()
    scr.delete(0,END)
    global f_num
    f_num= int(num)
    global operation
    operation = "multiplication"
    
def btn_div():
    num=scr.get()
    scr.delete(0,END)
    global f_num
    f_num= int(num)
    global operation
    operation = "divition"

def equals():
    s_num = scr.get()
    s_num = int(s_num)
    scr.delete(0, END)

    result = None  # Initialize the variable outside the try block

    try:
        if operation == "addition":
            result = f_num + s_num
        elif operation == "subtraction":
            result = f_num - s_num
        elif operation == "multiplication":
            result = f_num * s_num
        elif operation == "division":
            result = f_num / s_num
        else:
            result = "Error"
    except ZeroDivisionError:
        result = "Error: Division by zero"

    scr.insert(0, result)

    
    

btn_1 = Button(root, text="1", padx=20, pady=20, command=lambda: btn_num(1))
btn_2 = Button(root, text="2", padx=20, pady=20, command=lambda: btn_num(2))
btn_3 = Button(root, text="3", padx=20, pady=20, command=lambda: btn_num(3))
btn_4 = Button(root, text="4", padx=20, pady=20, command=lambda: btn_num(4))
btn_5 = Button(root, text="5", padx=20, pady=20, command=lambda: btn_num(5))
btn_6 = Button(root, text="6", padx=20, pady=20, command=lambda: btn_num(6))
btn_7 = Button(root, text="7", padx=20, pady=20, command=lambda: btn_num(7))
btn_8 = Button(root, text="8", padx=20, pady=20, command=lambda: btn_num(8))
btn_9 = Button(root, text="9", padx=20, pady=20, command=lambda: btn_num(9))
btn_0 = Button(root, text="0", padx=20, pady=20, command=lambda: btn_num(0))

btn_clr = Button(root, text="DEL", padx=20, pady=20, command=clr_scr)
btn_equal = Button(root, text="=", padx=20, pady=20, command=equals)
btn_add = Button(root, text="+", padx=20, pady=20, command= btn_add)
btn_sub = Button(root, text="-", padx=20, pady=20, command= btn_sub)
btn_mult = Button(root, text="X", padx=20, pady=20, command= btn_mult)
btn_div = Button(root, text="/", padx=20, pady=20, command=btn_div)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_add.grid(row=1, column=3)


btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_mult.grid(row=3, column=3)

btn_clr.grid(row=4, column=0)
btn_0.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_div.grid(row=4, column=3)

root.mainloop()
