# Simple Calculator
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

# Define window
root = tkinter.Tk()
root.title('Calculator')
root.geometry('300x400')
root.resizable(0, 0)

# Define colors and fonts
brown = '#A17C6B'
light_brown = '#CEB5A7'
light_blue = '#E0F2E9'
navy_blue = '#5B7B7A'
button_font = ('Arial', 18)
display_font = ('Arial', 30)



# Define functions
def submit_number(number):
    """Add a number or decimal to the display"""
    # Insert the number or decimal pressed to the end of the display
    display.insert(END, number)

    # If decimal was pressed, disable the decimal button so it cannot be pressed twice
    if "." in display.get():
        decimal_button.config(state=DISABLED)


def operate(operator):
    """Store the first number of the expression and the operation to be used"""
    global first_number
    global operation

    # Get the operator pressed and the current value of the display.  This is the first number in the calculation
    operation = operator
    first_number = display.get()

    # Delete the value (first number) from entry display
    display.delete(0, END)

    # Disable all operator buttons until equal or clear is pressed
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    square_root.config(state=DISABLED)
    cubed_button.config(state=DISABLED)

    # Return decimal button to normal state
    decimal_button.config(state=NORMAL)


def equal():
    """Run the stored operation for two number."""
    # Perform the desired mathematics
    if operation == 'add':
        value = float(first_number) + float(display.get())
    elif operation == 'subtract':
        value = float(first_number) - float(display.get())
    elif operation == 'multiply':
        value = float(first_number) * float(display.get())
    elif operation == 'divide':
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(display.get())


    # Remove the curent value of the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)

    # Return buttons to normal states
    enable_buttons()


def enable_buttons():
    """Enable all buttons on the calculator"""
    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    square_root.config(state=NORMAL)
    square_button.config(state=NORMAL)
    cubed_button.config(state=NORMAL)


def clear():
    """Clear the display"""
    display.delete(0, END)

    # Return buttons to normal state
    enable_buttons()


def square_root():
    """Calculate the square root of a given number."""
    value = float(display.get()) ** 0.5

    # Remove the current value in the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)

def cubed():
    """Calculate the square of a given number."""
    value = float(display.get()) ** 3

    display.delete(0, END)
    display.insert(0, value)


def square():
    """Calculate the square of a given number."""
    value = float(display.get()) ** 2

    # Remove the current value in the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)


def negate():
    """Negate a given number."""
    value = -1 * float(display.get())

    # Remove the current value in the display and update it with the answer
    display.delete(0, END)
    display.insert(0, value)


# GUI Layout
# Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5, 20))
button_frame.pack(padx=2, pady=5)

# Layout for the display frame
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=light_blue, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

# Layout for the button frame
clear_button = tkinter.Button(button_frame, text="CE", font=button_font, bg=brown, fg='#3E2F28', command=clear)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font, bg=brown, fg='#3E2F28', command=root.destroy)
square_root = tkinter.Button(button_frame, text='\u221A', font=button_font, bg=light_brown, fg='#4E392C', command=square_root)
square_button = tkinter.Button(button_frame, text='x\u00B2', font=button_font, bg=light_brown, fg='#4E392C', command=square)
cubed_button = tkinter.Button(button_frame, text='x\u00B3', font=button_font, bg=brown, fg='#3E2F28', command=cubed)
exponent_button = tkinter.Button(button_frame, text='x\u207f', font=button_font, bg=light_brown, fg='#4E392C',
                                 command=lambda: operate('exponent'))
divide_button = tkinter.Button(button_frame, text=' / ', font=button_font, bg=light_brown, fg='#4E392C',
                               command=lambda: operate('divide'))
multiply_button = tkinter.Button(button_frame, text='*', font=button_font, bg=light_brown, fg='#4E392C',
                                 command=lambda: operate('multiply'))
subtract_button = tkinter.Button(button_frame, text='-', font=button_font, bg=light_brown, fg='#4E392C',
                                 command=lambda: operate('subtract'))
add_button = tkinter.Button(button_frame, text='+', font=button_font, bg=light_brown, fg='#4E392C', command=lambda: operate('add'))
equal_button = tkinter.Button(button_frame, text='=', font=button_font, bg=brown, fg='#3E2F28', command=equal)
decimal_button = tkinter.Button(button_frame, text='.', font=button_font, bg='#5B7B7A', fg='white',
                                command=lambda: submit_number("."))
negate_button = tkinter.Button(button_frame, text='+/-', font=button_font, bg='#5B7B7A', fg='white', command=negate)

nine_button = tkinter.Button(button_frame, text='9', font=button_font, bg='#5B7B7A', fg='white',
                             command=lambda: submit_number(9))
eight_button = tkinter.Button(button_frame, text='8', font=button_font, bg='#5B7B7A', fg='white',
                              command=lambda: submit_number(8))
seven_button = tkinter.Button(button_frame, text='7', font=button_font, bg='#5B7B7A', fg='white',
                              command=lambda: submit_number(7))
six_button = tkinter.Button(button_frame, text='6', font=button_font, bg='#5B7B7A', fg='white',
                            command=lambda: submit_number(6))
five_button = tkinter.Button(button_frame, text='5', font=button_font, bg='#5B7B7A', fg='white',
                             command=lambda: submit_number(5))
four_button = tkinter.Button(button_frame, text='4', font=button_font, bg='#5B7B7A', fg='white',
                             command=lambda: submit_number(4))
three_button = tkinter.Button(button_frame, text='3', font=button_font, bg='#5B7B7A', fg='white',
                              command=lambda: submit_number(3))
two_button = tkinter.Button(button_frame, text='2', font=button_font, bg='#5B7B7A', fg='white',
                            command=lambda: submit_number(2))
one_button = tkinter.Button(button_frame, text='1', font=button_font, bg='#5B7B7A', fg='white',
                            command=lambda: submit_number(1))
zero_button = tkinter.Button(button_frame, text='0', font=button_font, bg='#5B7B7A', fg='white',
                             command=lambda: submit_number(0))

# First row
clear_button.grid(row=0, column=1, columnspan=2, pady=1, sticky="WE")
quit_button.grid(row=0, column=3, pady=1, sticky="WE")
cubed_button.grid(row=0, column=0, pady=1, sticky="WE")

# Second row
square_root.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")
# Third row (Add padding to create the size of the columns)
seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)
# Fourth row
four_button.grid(row=3, column=0, pady=1, sticky="WE")
five_button.grid(row=3, column=1, pady=1, sticky="WE")
six_button.grid(row=3, column=2, pady=1, sticky="WE")
subtract_button.grid(row=3, column=3, pady=1, sticky="WE")
# Fifth row
one_button.grid(row=4, column=0, pady=1, sticky="WE")
two_button.grid(row=4, column=1, pady=1, sticky="WE")
three_button.grid(row=4, column=2, pady=1, sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")
# Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky="WE")
zero_button.grid(row=5, column=1, pady=1, sticky="WE")
decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")

# Run the root window's main loop
root.mainloop()