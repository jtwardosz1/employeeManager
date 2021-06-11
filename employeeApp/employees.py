import tkinter as tk
from tkinter import *
from tkinter import messagebox
from db import Database

# Instance of database obj
db = Database('employee.db')

# Employee window details
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title('Employee Manager')
        master.geometry('700x350')
        self.create_widgets()
        self.selected_emp = 0
        self.populate_list()
    
    def create_widgets(self):
        #First Name
        self.empFirst_text = tk.StringVar()
        self.empFirst_label = tk.Label(self.master, text='First Name:   ', font=('bold', 14), padx= 20, pady=20)
        self.empFirst_label.grid(row=0, column=0, sticky=W)
        self.empFirst_entry = tk.Entry(self.master, textvariable=self.empFirst_text)
        self.empFirst_entry.grid(row=0, column=1, sticky=W)

        #Last Name
        self.empLast_text = tk.StringVar()
        self.empLast_label = tk.Label(self.master, text='Last Name: ', font=('bold', 14), padx=20, pady=20)
        self.empLast_label.grid(row=0, column=2, sticky=W)
        self.empLast_entry = tk.Entry(self.master, textvariable=self.empLast_text)
        self.empLast_entry.grid(row=0, column=3, sticky=W)

        #phone
        self.empPhone_text = tk.StringVar()
        self.empPhone_label = tk.Label(self.master, text='Phone Number: ', font=('bold', 14), padx= 20, pady=20)
        self.empPhone_label.grid(row=1, column=0, sticky=W)
        self.empPhone_entry = tk.Entry(self.master, textvariable=self.empPhone_text)
        self.empPhone_entry.grid(row=1, column=1, sticky=W)

        #email
        self.empEmail_text = tk.StringVar()
        self.empEmail_label = tk.Label(self.master, text='Email:    ', font=('bold', 14), padx=20, pady=20)
        self.empEmail_label.grid(row=1, column=2, sticky=W)
        self.empEmail_entry = tk.Entry(self.master, textvariable=self.empEmail_text)
        self.empEmail_entry.grid(row=1, column=3, sticky=W)
        
        #emp list
        self.emp_list = tk.Listbox(self.master, height=8, width=50, border=0, font=12)
        self.emp_list.grid(row=3, column=0, columnspan=3, rowspan=6, padx=20, pady=20)
        
        #scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        
        #set scrollbar to listbox
        self.emp_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.emp_list.yview)
        
        #bind select
        self.emp_list.bind('<<ListboxSelect>>', self.select_emp)
        
        #buttons
        self.add_btn = tk.Button(self.master, text="Add Employee", height=1, width=14, border=4, command=self.add_emp)
        self.add_btn.grid(row=2, column=0, padx=(30, 30))
        
        self.remove_btn = tk.Button(self.master, text="Remove Employee", height=1, width=14, border=4, command=self.remove_emp)
        self.remove_btn.grid(row=2, column=1, padx=(30, 30))
        
        self.update_btn = tk.Button(self.master, text="Update Employee", height=1, width=14, border=4, command=self.update_emp)
        self.update_btn.grid(row=2, column=2, padx=(30, 30))
        
        self.clear_btn = tk.Button(self.master, text="Clear Text", height=1, width=14, border=4, command=self.clear_text)
        self.clear_btn.grid(row=2, column=3, padx=(30, 30))
        
    def populate_list(self):
        #Delete items before updating
        self.emp_list.delete(0, tk.END)
        #Loop List
        for row in db.get():
            self.emp_list.insert(tk.END, row)
    
    def add_emp(self):
        if self.empFirst_text.get() == '' or self.empLast_text.get() == '' or self.empPhone_text.get() == '' or self.empEmail_text.get() == '':
            messagebox.showerror('Required Fields', 'Please fill out all fields')
            return
        db.set(self.empFirst_text.get(), self.empLast_text.get(), self.empPhone_text.get(), self.empEmail_text.get())
        #clear list
        self.emp_list.delete(0, END)
        #set to list
        self.emp_list.insert(0, tk.END, (self.empFirst_text.get(), self.empLast_text.get(), self.empPhone_text.get(), self.empEmail_text.get()))
        self.clear_text()
        self.populate_list()
        
    def select_emp(self, event):
        try:
            #index
            index = self.emp_list.curselection()[0]
            #get selected employee
            self.selected_emp = self.emp_list.get(index)
            
            #add text to entries
            self.empFirst_entry.delete(0, tk.END)
            self.empFirst_entry.insert(tk.END, self.selected_emp[1])
            self.empLast_entry.delete(0, tk.END)
            self.empLast_entry.insert(tk.END, self.selected_emp[2])
            self.empPhone_entry.delete(0, tk.END)
            self.empPhone_entry.insert(tk.END, self.selected_emp[3])
            self.empEmail_entry.delete(0, tk.END)
            self.empEmail_entry.insert(tk.END, self.selected_emp[4])
            
        except IndexError:
            pass
        
    def remove_emp(self):
        db.remove(self.selected_emp[0])
        self.clear_text()
        self.populate_list()
    
    def update_emp(self):
        db.update(self.selected_emp[0], self.empFirst_text.get(), self.empLast_text.get(), self.empPhone_text.get(), self.empEmail_text.get())
        self.populate_list()
        
    def clear_text(self):
        self.empFirst_entry.delete(0, END)
        self.empLast_entry.delete(0, END)
        self.empPhone_entry.delete(0, END)
        self.empEmail_entry.delete(0, END)
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()