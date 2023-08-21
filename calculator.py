from tkinter import *

root= Tk()
root.title('calculator')

e = Entry(root,width=35,border=5)
e.grid(row=0,column=0,columnspan=3)



#function for the command
def cal(number):
    current= e.get() #gets the current value in the entry field
    e.delete(0,END)#deletes the first value 
    e.insert(0,str(current)+str(number)) #appends the current value and the new value
    
def clear_num():
    e.delete(0,END) # clear the values in the entry field


def add_fun():
    fistnum=e.get()
    global f_num 
    global sign 
    sign = 'addition'
    f_num =int(fistnum)
    e.delete(0,END)

def sub_fun():
    fistnum=e.get()
    global f_num 
    global sign 
    sign='subtraction'
    f_num =int(fistnum)
    e.delete(0,END)

def times_fun():
    fistnum=e.get()
    global f_num 
    global sign 
    sign='multiplication'
    f_num =int(fistnum)
    e.delete(0,END)

def div_fun():
    fistnum=e.get() # get the number on the entry field
    global f_num 
    global sign 
    sign = 'division'
    f_num =int(fistnum) # assigns f_num the value of the numeber
    e.delete(0,END) # deletes the first number inn the field

def equal_fun():
    second=e.get()
    e.delete(0,END)
    if sign == 'addition':
        e.insert(0, f_num + int(second))
    if sign == 'subtraction':
        e.insert(0, f_num - int(second))
    if sign == 'multiplication':
        e.insert(0, f_num * int(second))
    if sign == 'division':
        e.insert(0, f_num + int(second))
    # if sign == 'addition':
    #     e.insert(0, f_num + int(second))

# each section of numbers
#first row
btn1 = Button(root,text=1,command=lambda:cal(1)).grid(row=1,column=0)
btn2 = Button(root,text=2,command=lambda:cal(2)).grid(row=1,column=1)
btn3 = Button(root,text=3,command=lambda:cal(3)).grid(row=1,column=2)
 #second row
btn4 = Button(root,text=4,command=lambda:cal(4)).grid(row=2,column=0)
btn5 = Button(root,text=5,command=lambda:cal(5)).grid(row=2,column=1)
btn6 = Button(root,text=6,command=lambda:cal(6)).grid(row=2,column=2)

btn_add = Button(root,text='+',command=add_fun).grid(row=3,column=0)
btn_sub = Button(root,text='-',command=sub_fun).grid(row=3,column=1)
btn_clear = Button(root,text='clear',command=clear_num).grid(row=3,column=1,columnspan=2)
btn0 = Button(root,text=0,command=lambda:cal(0)).grid(row=4,column=0)
btn_eqa = Button(root,text='=',command=equal_fun).grid(row=4,column=1,columnspan=2)



# the main loop 
root.mainloop()