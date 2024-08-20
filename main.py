from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    character_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = character_list + symbol_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    Password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = Email_entry.get()
    password = Password.get()
    if len(web)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title= 'Error!', message="Please don't leave any box empty.")
    else:
        choice = messagebox.askyesno(title = web, message = f"This is the information that you are going to save\n"
                                                   f"website:  {web}\n email/;  {email}\n  password:{password}\n"
                                                            f" \n is it okey? ")

        if choice:

            with open('data_file.txt', 'a') as data_file:
                data_file.write(f"{web} | {email} | {password}\n")
                website_entry.delete(0, END)
                Password.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #



def function():
    return None

window = Tk()
window.title('Password Manager')
window.config(padx= 50, pady =50)

canvas = Canvas(width = 200 , height = 200,  highlightthickness=0)
logo_image = PhotoImage(file = 'logo.png')
canvas.create_image(100,100,image = logo_image)
canvas.grid(row = 0, column =1)


web = Label(text = "Website:")
web.grid(row = 1, column = 0)
Email = Label(text = "Email/Username:")
Email.grid(row = 2, column = 0)
passwordlabel = Label(text = "Password:")
passwordlabel.grid(row = 3, column = 0)

website_entry = Entry(width = 35)
website_entry.grid(row = 1, column= 1, columnspan = 2)
website_entry.focus()
Email_entry = Entry( width = 35)
Email_entry.grid(row = 2, column= 1, columnspan = 2)

Password = Entry( width = 21)
Password.grid(row = 3, column= 1, columnspan = 2)


Generate = Button(text = 'Generate Password',command = password)
Generate.grid(row = 3, column =2)


Add = Button(text = 'Add',command = save, width = 36)
Add.grid(row = 4, column =1)
window.mainloop()
