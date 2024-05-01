# step 1 importing the required libraries

import openpyxl

from tkinter import *

from tkinter import messagebox

# step2 initialize the tool kit window

root = Tk()
root.title("student registration form")
root.geometry("800x800")

# Step 3: Create Labels and Entry Fields
First_name_label = Label(root, text="First name")
First_name_label.pack()

First_name_entry = Entry(root)
First_name_entry.pack()

Last_name_label = Label(root, text="last name")
Last_name_label.pack()

Last_name_entry = Entry(root)
Last_name_entry.pack()

admission_label = Label(root, text="your age")
admission_label.pack()

admission_entry = Entry(root)
admission_entry.pack()

email_label = Label(root,text="email adress")
email_label.pack()

email_entry = Entry(root)
email_entry.pack()

mobile_label = Label(root, text="phone number")
mobile_label.pack()

mobile_entry = Entry(root)
mobile_entry.pack()
                     
''' For positioning the labels and the entry field, you can use
 different
 methods such as pack, grid, and place. '''

# Step 4: Create a Function to get data from Entry Fields

def register():
    # get user input from the form
    First_name = First_name_entry.get()
    Last_name = Last_name_entry.get()
    admission = admission_entry.get()
    email_adress = email_entry.get()
    Phone = mobile_entry.get()
    # Create a new row with the user input

    new_row = [First_name, Last_name, admission, email_adress, Phone]

    # Append the new row to the Excel sheet

    workbook = openpyxl.load_workbook("registration_data.xlsl")
    sheet = workbook.active
    sheet.append(new_row)
    workbook.save("registration_data.xlsl")
    messagebox.showinfo("Success", "registratin successful")

    # Step 5: Create Submit Button and run the main loop

register_button = Button(root, text="Register", command="register")
register_button.pack()

root.mainloop()