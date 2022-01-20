from tkinter import N, S, W, E, Button, Tk, Entry, StringVar, RIGHT, DISABLED, PhotoImage


expression = ""
display_expression = ""


def press(operation, symbol=None):
    global expression
    global display_expression
    if symbol is None:
        symbol = operation
    try:
        expression += str(int(operation))
        display_expression += str(symbol)
        equation.set(display_expression)
    except Exception:
        if len(expression) != 0:
            if expression[-1] in ('-', '+', '*', '/'):
                expression = expression[0:-1] + str(operation)
                display_expression = display_expression[0:-1] + str(symbol)
                equation.set(display_expression)
            else:
                expression += str(operation)
                display_expression += str(symbol)
                equation.set(display_expression)
        else:
            if str(operation) in ('-', '+'):
                expression += str(operation)
                display_expression += str(symbol)
                equation.set(display_expression)


def equal(event=None):
    try:
        global expression
        global display_expression
        result = str(eval(expression))
        equation.set(result)
        expression = display_expression = str(result)
    except Exception:
        equation.set(" error ")
        expression = display_expression = ""


def clear():
    global expression
    global display_expression
    expression = display_expression = ""
    equation.set("")


window = Tk()
window.configure(background="light grey")
window.title("Simple calculator")
window.iconphoto(False, PhotoImage(file='./resources/icon.png'))
equation = StringVar()
expression_field = Entry(
        window,
        bg='red',
        bd=5,
        justify=RIGHT,
        font=("Times New Roman", 20),
        disabledforeground='black',
        state=DISABLED,
        disabledbackground='white',
        textvariable=equation
        ).grid(columnspan=4, sticky=N+S+W+E)


c_button = Button(
        window,
        text='C',
        command=lambda: clear(),
        height=2
        ).grid(row=2, column=0, sticky=N+S+W+E)

div_button = Button(
        window,
        text='÷',
        command=lambda: press('/', '\u00f7')
        ).grid(row=2, column=1, sticky=N+S+W+E)

mult_button = Button(
        window,
        text='×',
        command=lambda: press('*', '\u2219')
        ).grid(row=2, column=2, sticky=N+S+W+E)

sub_button = Button(
        window,
        text='-',
        command=lambda: press('-', '\u2212')
        ).grid(row=2, column=3, sticky=N+S+W+E)

button_7 = Button(
        window,
        text='7',
        command=lambda: press('7'),
        height=2
        ).grid(row=3, column=0, sticky=N+S+W+E)

button_8 = Button(
        window,
        text='8',
        command=lambda: press('8')
        ).grid(row=3, column=1, sticky=N+S+W+E)

button_9 = Button(
        window,
        text='9',
        command=lambda: press('9')
        ).grid(row=3, column=2, sticky=N+S+W+E)

sum_button = Button(
        window,
        text='+',
        command=lambda: press('+', '\u002b')
        ).grid(row=3, rowspan=2, column=3, sticky=N+S+W+E)

button_4 = Button(
        window,
        text='4',
        command=lambda: press('4'),
        height=2
        ).grid(row=4, column=0, sticky=N+S+W+E)

button_5 = Button(
        window,
        text='5',
        command=lambda: press('5')
        ).grid(row=4, column=1, sticky=N+S+W+E)

button_6 = Button(
        window,
        text='6',
        command=lambda: press('6')
        ).grid(row=4, column=2, sticky=N+S+W+E)

button_1 = Button(
        window,
        text='1',
        command=lambda: press('1'),
        height=2
        ).grid(row=5, column=0, sticky=N+S+W+E)

button_2 = Button(
        window,
        text='2',
        command=lambda: press('2')
        ).grid(row=5, column=1, sticky=N+S+W+E)

button_3 = Button(
        window,
        text='3',
        command=lambda: press('3')
        ).grid(row=5, column=2, sticky=N+S+W+E)

result_button = Button(
        window,
        text='=',
        command=lambda: equal()
        ).grid(row=5, rowspan=2, column=3, sticky=N+S+W+E)

button_0 = Button(
        window,
        text='0',
        command=lambda: press('0'),
        height=2
        ).grid(row=6, column=0, columnspan=2, sticky=N+S+W+E)

dot_button = Button(
        window,
        text='.',
        command=lambda: press('.')
        ).grid(row=6, column=2, sticky=N+S+W+E)


window.bind('<Return>', equal)
window.bind('<KP_Enter>', equal)

window.bind('<KP_Decimal>', lambda event: press('.'))
window.bind('<KP_Add>', lambda event: press('+', '\u002b'))
window.bind('<KP_Subtract>', lambda event: press('-', '\u2212'))
window.bind('<KP_Multiply>', lambda event: press('*', '\u2219'))
window.bind('<KP_Divide>', lambda event: press('/', '\u00f7'))

window.bind('<KP_1>', lambda event: press('1'))
window.bind('<KP_2>', lambda event: press('2'))
window.bind('<KP_3>', lambda event: press('3'))
window.bind('<KP_4>', lambda event: press('4'))
window.bind('<KP_5>', lambda event: press('5'))
window.bind('<KP_6>', lambda event: press('6'))
window.bind('<KP_7>', lambda event: press('7'))
window.bind('<KP_8>', lambda event: press('8'))
window.bind('<KP_9>', lambda event: press('9'))
window.bind('<KP_0>', lambda event: press('0'))

window.mainloop()
