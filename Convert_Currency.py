import tkinter.font
import conversion
from tkinter import *
from tkinter import messagebox

root = Tk()
try:
    root.iconbitmap('images.ico')
except Exception:
    pass

root.title('Currency Converter')
root.geometry("600x400")

des_font = tkinter.font.Font(family="Lucida Sans", size=12)

frame = LabelFrame(root)
frame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.7, anchor=CENTER)

currencies = ["Indian Rupees (INR)",
              "US Dollar (USD)",
              "Euro (EUR)",
              "Pound Sterling (GBP)",
              "Australian Dollar (AUD)",
              "Canadian Dollar (CAD)",
              "Japanese Yen (JPY)",
              "Swiss Franc (CHF)",
              "Chinese Renminbi (CNY)",
              "Hong Kong Dollar (HKD)",
              "New Zealand Dollar (NZD)"
              ]

clicked1 = StringVar()
drop1 = OptionMenu(frame, clicked1, *currencies)
drop1.config(width=25, font=des_font)
drop1_lab = Label(frame, text="From: ", font=des_font)

drop1_lab.pack(side=TOP, pady=5)
drop1.pack(pady=5)

clicked1.set(currencies[1])

clicked2 = StringVar()
drop2 = OptionMenu(frame, clicked2, *currencies)
drop2.config(width=25, font=des_font)
drop2_lab = Label(frame, text="To: ", font=des_font)

drop2_lab.pack(side=TOP)
drop2.pack(pady=5)

clicked2.set(currencies[0])

ent = Entry(frame, width=28, borderwidth=3.25, justify=CENTER, bg="#ffdec2", relief=SUNKEN, font=des_font) #ffdec2
ent.pack(pady=7)

update = StringVar(root, "RESULT")

def process():
    global update
    global lab
    from_country = clicked1.get()
    fc_sliced = from_country[-4:-1]
    to_country = clicked2.get()
    tc_sliced = to_country[-4:-1]
    amt = ent.get()
    try:
        con = conversion.conversion()
        result= con.convert(amt, fc_sliced, tc_sliced)
        result_str = "{0:.3f}".format(result)
        update = StringVar(frame, result_str)
        lab.config(textvariable=update)

    except ValueError:
        messagebox.showerror("Error", "No value or improper value was entered")

lab = Label(frame, textvariable=update, font=("Lucida Sans", 12, "bold"), bd=1, relief=GROOVE)
lab.pack(pady=5, ipadx=64)


button = Button(frame, text="Convert", width=15, font=des_font, command=process, bd=2.25)
button.pack(pady=5)

root.mainloop()





