from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 21))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=20)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=4, row=3)
button.config(padx=10, pady=20)


# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)

# New Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=3, row=0)
new_button.config(padx=10, pady=20)







window.mainloop()