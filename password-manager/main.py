from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    email = email_entry.get()
    passw = pass_entry.get()

    if web == "" or email == "" or passw == "":
        messagebox.showinfo(title="Oops", message="Please dont' leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: "
                                                  f"\nEmail: {email} \nPassword: {passw} \n"
                                                  f"Is it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{web} | {email} | {passw}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

text_web = Label(text="Website:")
text_web.grid(row=1, column=0)

text_email = Label(text="Email/Username:")
text_email.grid(row=2, column=0)

text_pass = Label(text="Password:")
text_pass.grid(row=3, column=0)

web_entry = Entry()
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

email_entry = Entry()
email_entry.insert(0, "default@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

pass_entry = Entry()
pass_entry.grid(row=3, column=1, sticky="ew")

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2, sticky="ew")

add = Button(text="Add", command=save)
add.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
