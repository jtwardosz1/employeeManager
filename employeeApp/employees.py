from tkinter import *

# Create window object

app = Tk()

# Employee window details
emp_text = StringVar()
emp_label = Label(app, text='First Name', font=('bold', 14), pady=20)
emp_label.grid(row=0, column=0)

app.title('Employee Manager')
app.geometry('700x350')

# Start program
app.mainloop()


