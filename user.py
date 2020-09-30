from tkinter import Tk, Button, Entry, Grid, mainloop
root = Tk()

text_box = Entry(width=85)

pos = 0
add_list = []
sub_list = []



def fill_entry(number):
    global pos
    text_box.insert(pos, number)
    pos += 1
    return

#ADDITION OPERATION 
def plus():
    global add_list
    global pos
    value = int(text_box.get())
    add_list.append(value)
    text_box.delete(0, 'end')
    pos = 0
    print(f'number list= {add_list} and pos = {pos}')

#EQUALS OPERATION
def equals():
    global add_list
    global pos
    last_val = text_box.get()
    text_box.delete(0, 'end')
    print(f'value of last_val: {len(last_val)}')
    if len(last_val) != 0:
        add_list.append(int(last_val))
        print(f'this executes if {last_val} is not zero')
        print(f'value of add_list when {last_val} is not 0: {add_list}')
    total = sum(add_list)
    add_list = []
    pos = 0
    text_box.insert(pos, total)

#CLEAR THE INPUT AND RESULT FIELD OPERATION
def clear():
    text_box.delete(0, 'end')


button_one = Button(root, text='1', padx=50, pady=20,
                    command=lambda: fill_entry(1))
button_two = Button(root, text='2', padx=50, pady=20,
                    command=lambda: fill_entry(2))
button_three = Button(root, text='3', padx=50, pady=20,
                      command=lambda: fill_entry(3))
button_four = Button(root, text='4', padx=50, pady=20,
                     command=lambda: fill_entry(4))
button_five = Button(root, text='5', padx=50, pady=20,
                     command=lambda: fill_entry(5))
button_six = Button(root, text='6', padx=50, pady=20,
                    command=lambda: fill_entry(6))
button_seven = Button(root, text='7', padx=50, pady=20,
                      command=lambda: fill_entry(7))
button_eight = Button(root, text='8', padx=50, pady=20,
                      command=lambda: fill_entry(8))
button_nine = Button(root, text='9', padx=50, pady=20,
                     command=lambda: fill_entry(9))
button_add = Button(root, text='+', padx=70, pady=20,
                    command=lambda: plus())
button_clear = Button(root, text='C', padx=70,
                      pady=20, command=clear)
button_equals = Button(root, text='=', padx=70,
                       pady=20, command=equals)
button_sub = Button(root, text='-', padx=70, pady=20,
                    command=lambda: plus())
button_mul = Button(root, text='*', padx=70,
                    pady=20, command=clear)
button_div = Button(root, text='/', padx=70,
                    pady=20, command=equals)


button_one.grid(row=0, column=0)
button_two.grid(row=0, column=1)
button_three.grid(row=0, column=2)
button_four.grid(row=1, column=0)
button_five.grid(row=1, column=1)
button_six.grid(row=1, column=2)
button_seven.grid(row=2, column=0)
button_eight.grid(row=2, column=1)
button_nine.grid(row=2, column=2)
text_box.grid(row=3, column=0, columnspan=4)
button_add.grid(row=0, column=3)
button_clear.grid(row=1, column=3)
button_equals.grid(row=2, column=3)
button_sub.grid(row=0, column=5)

root.mainloop()
