from tkinter import *
from main_create_pass import *
from main_easy_pass import *
from main_custom_pass import *

window = Tk()

def password_display(): #called when generate button is clicked

    allowedchar = allowed_characters()

    if pass_type.get() == 1:
        pass_length = length_slider.get()
        password_box.delete(0, END)
        password_box.insert(0, create_strong_pass(pass_length, allowedchar))

    elif pass_type.get() == 2:
        pass_length = length_slider.get()
        password_box.delete(0, END)
        password_box.insert(0, create_easy_pass(pass_length, allowedchar))

    elif pass_type.get() == 3:
        LenOfChar = lengthofchar_custom()

        password_box.delete(0, END)
        password_box.insert(0, create_custom_pass(allowedchar, LenOfChar))
        set_slider(0)

def set_slider(self): # displays the length of custom_pass on scale

    if pass_type.get() == 3:
        allowedchar = allowed_characters()
        LenOfChar = lengthofchar_custom()
        total_length = length_custom_pass(LenOfChar, allowedchar)
        length_slider.set(total_length)

def clipper(): # for copying password

    window.clipboard_clear()
    window.clipboard_append(password_box.get())

def allowed_characters():

    #list of 0/1 for types of characters
    # eg.[1, 1, 0, 0] corresponds [lower:true, upper:true, digits:false, symbols:false]
    allowedchar = []
    allowedchar.append(lower_state.get())
    allowedchar.append(upper_state.get())
    allowedchar.append(digit_state.get())
    allowedchar.append(symbol_state.get())
    return allowedchar

def lengthofchar_custom(): # creating list containing length of each type of character

    LenOfChar = []
    LenOfChar.append(lowercase_slider.get())
    LenOfChar.append(uppercase_slider.get())
    LenOfChar.append(digits_slider.get())
    LenOfChar.append(Symbols_slider.get())
    return LenOfChar

def Initial_state(): # initial settings when the window is launched

    lower_state.set(1) # initially all options for type of characters is ticked
    upper_state.set(1)
    digit_state.set(1)
    symbol_state.set(1)

    lowercase_slider.configure(state="disable")
    uppercase_slider.configure(state="disable")
    digits_slider.configure(state="disable")
    Symbols_slider.configure(state="disable")

def enable_custom_slider():

	lowercase_slider.configure(state="normal")
	lowercase_slider.update()
	uppercase_slider.configure(state="normal")
	uppercase_slider.update()
	digits_slider.configure(state="normal")
	digits_slider.update()
	Symbols_slider.configure(state="normal")
	Symbols_slider.update()

def disable_custom_slider():

	lowercase_slider.configure(state="disable")
	lowercase_slider.update()
	uppercase_slider.configure(state="disable")
	uppercase_slider.update()
	digits_slider.configure(state="disable")
	digits_slider.update()
	Symbols_slider.configure(state="disable")
	Symbols_slider.update()

window.title("Unique Password Generator")
# +250 +20 adjust the placement of window on computer screen when program runs
window.geometry('620x620+260+0')
# window not resizable
window.resizable(0, 0)
# padx and pady decides the gap between widget and window(border)
window.config(padx=35, pady=20, bg="#2592EF")

Main_title = Label(window, text="Unique Password Generator: Generate Secure Passwords",
                    bg="gold", fg='#8B4513', bd=12, font=("Arial", 15)) # bd for border size
Main_title.pack(side=TOP, anchor=NW,)

"""
Frame1
- displaying password
- generate button
- copy button
"""
display_frame = Frame(window)
display_frame.pack(anchor=NW, pady=18)
display_frame.config(padx=5, pady=5)

password_box = Entry(display_frame, width=30, bd=10, font=("Helvetica", 15))
password_box.grid(row=0, column=0, padx=10)

generate_button = Button(display_frame, text="Generate", command=password_display,
                         width=8,font = ("Helvetica", 12))
generate_button.grid(row = 0, column = 1,)

copy_button = Button(display_frame, text="copy", command=clipper, width=8, font=("Helvetica", 12))
copy_button.grid(row=0, column=2, padx=10)

"""
Frame2
- password length label
- length slider
"""
Pass_length_frame = Frame(window)
Pass_length_frame.place(rely=0.2, x=5, y=20)

Password_length = Label(Pass_length_frame, text="Password length",
                        fg="#150303", bd=5, font=("Helvetica", 15))
Password_length.grid(row=0, column=0, padx=10)

length_slider = Scale(Pass_length_frame, orient=HORIZONTAL, from_=1, to=60, sliderlength=20,
                      tickinterval=9, relief=SOLID, width=24, length=250, troughcolor="red",)
length_slider.grid(row=0, column=1, padx=10)
length_slider.set(14)

"""
Frame3
- Radio buttons (strong, easy, custom)
"""
pass_type_frame = Frame(window)
pass_type_frame.place(rely=0.3, x=10, y=50)

pass_type = IntVar(value=1)
Strong_pass = Radiobutton(pass_type_frame, text="Strong  Password",  command=disable_custom_slider
                         ,variable=pass_type, value=1, indicatoron=0, offrelief = FLAT,
                         font=("Helvetica", 15), bg="gold", fg= 'red', borderwidth=6,)
Strong_pass.grid(row=0, column=0)

Easy_pass = Radiobutton(pass_type_frame, text="Easy to remember", command=disable_custom_slider,
                       variable=pass_type, value=2, indicatoron=0, offrelief=FLAT,
                       font=("Helvetica", 15), bg="gold", fg='red', borderwidth=6,)
Easy_pass.grid(row=1, column=0)

Customized_pass = Radiobutton(pass_type_frame, text="Custom Password",command=enable_custom_slider
                            ,variable=pass_type, value=3, indicatoron=0, offrelief=FLAT,
                            font=("Helvetica", 15), bg="gold" ,fg='red', borderwidth = 6,)
Customized_pass.grid(row=2, column=0)

"""
Frame4
- combo box (lowercase, digits etc.)
"""
char_options_frame = Frame(window)
char_options_frame.place(rely = 0.3, relx = 0.5, x= 10, y = 45)

lower_state, upper_state, digit_state, symbol_state = IntVar(), IntVar(), IntVar(), IntVar()

lowercase_state = Checkbutton(char_options_frame, text='lowercase', variable=lower_state,
							onvalue=1, offvalue=0, font=('Helvetica', 15),bg='gold',fg='red')
lowercase_state.grid(row=0, column = 1)

uppercase_state = Checkbutton(char_options_frame, text='uppercase',variable=upper_state,
                            onvalue=1, offvalue=0 , font=('Helvetica', 15), bg='gold', fg='red')
uppercase_state.grid(row=1, column=1)

digitschar_state = Checkbutton(char_options_frame, text='digits', variable=digit_state, onvalue=1,
                            offvalue=0, font=('Helvetica', 15), bg='gold', width=9, fg='red')
digitschar_state.grid(row=2, column = 1)

Specialchar_state = Checkbutton(char_options_frame, text='special char', variable=symbol_state,
                                onvalue=1, offvalue=0, font=('Helvetica', 15),bg='gold', fg='red')
Specialchar_state.grid(row=3, column = 1)

"""
Frame 5
- (lowercase, uppercase, digits, symbols) length slider
"""
CustomLen_frame = Frame(window, bg='#2592EF')
CustomLen_frame.place(rely=0.4, x=10, y=150)

lowercase_slider = Scale(CustomLen_frame, orient=VERTICAL, from_=0, to=60, sliderlength=18,
                     relief=SOLID, width=30, length=180, troughcolor="red", label="lowercase")
lowercase_slider.grid(row=0, column=1,)
lowercase_slider.bind("<ButtonRelease-1>",set_slider)

uppercase_slider = Scale(CustomLen_frame, orient=VERTICAL, from_=0, to=60, sliderlength=18,
                     relief=SOLID, width=30, length=180, troughcolor="red", label="uppercase" )
uppercase_slider.grid(row=0, column=2, padx=30)
uppercase_slider.bind("<ButtonRelease-1>",set_slider)

digits_slider = Scale(CustomLen_frame, orient = VERTICAL, from_=0, to=60, sliderlength=18,
                     relief=SOLID, width=30, length=180, troughcolor="red", label="digits" )
digits_slider.grid(row=0, column=3,)
digits_slider.bind("<ButtonRelease-1>",set_slider)

Symbols_slider = Scale(CustomLen_frame, orient=VERTICAL, from_=0, to=60, sliderlength=18,
                     relief=SOLID, width=30, length=180, troughcolor="red", label="symbols")
Symbols_slider.grid(row=0, column=4, padx=30)
Symbols_slider.bind("<ButtonRelease-1>",set_slider)

Initial_state()

window.mainloop()


