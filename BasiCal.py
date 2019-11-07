import tkinter, math, sys

## FUNCTIONS ##

# sys functions

def exit():
    sys.exit(0)

def clear():
    global equation
    global tk_equation
    equation = []
    tk_equation.set("")

def delete():
    global equation
    global tk_equation
    if type(equation) != list:
        equation = [equation]
    else:
        equation = equation[0:len(equation)-1]
    tk_equation.set(str(join_equation(equation)))

def change_theme():
    global active_theme
    if active_theme < len(themes)-1:
        active_theme += 1
    else:
        active_theme = 0
    for button in num_buttons:
        button.configure(fg=themes[active_theme]["num"]["fg"])
        button.configure(bg=themes[active_theme]["num"]["bg"])
    for button in op_buttons:
        button.configure(fg=themes[active_theme]["op"]["fg"])
        button.configure(bg=themes[active_theme]["op"]["bg"])
    for button in sys_buttons:
        button.configure(fg=themes[active_theme]["sys"]["fg"])
        button.configure(bg=themes[active_theme]["sys"]["bg"])
    title.configure(font = (themes[active_theme]["title_font"]["family"],
                            themes[active_theme]["title_font"]["size"],
                            themes[active_theme]["title_font"]["style"]))
    output.configure(font = (themes[active_theme]["output_font"]["family"],
                             themes[active_theme]["output_font"]["size"],
                             themes[active_theme]["output_font"]["style"]))
                
# math functions

def append_to_equation(element):
    equation.append(element)

def join_equation():
    global equation
    global tk_equation
    if len(equation) != 0:
        equation_joined = "".join(equation)
        return equation_joined
    else:
        return ""

def result():
    global equation
    equation_joined = join_equation()
    result = round(eval(equation_joined), 4)
    equation = [str(result)]
    return result


## BASIC SETUP ##

# layout

    # themes

sky = {"num" : {"bg" : "lightblue", "fg" : "black"},
       "op" : {"bg" : "lightblue", "fg" : "black"},
       "sys" : {"bg" : "white", "fg" : "black"},
       "title_font" : {"family" : "Sitka Heading", "size" : 18, "style" : "bold"},
       "output_font" : {"family" : "SimSun", "size" : 13, "style" : ""}}

dark = {"num" : {"bg" : "black", "fg" : "white"},
        "op" : {"bg" : "black", "fg" : "white"},
        "sys" : {"bg" : "#B22222", "fg" : "white"},
        "title_font" : {"family" : "Castellar", "size" : 15, "style" : "bold"},
        "output_font" : {"family" : "Georgia", "size" : 13, "style" : ""}}

classic = {"num" : {"bg" : "white", "fg" : "black"},
           "op" : {"bg" : "white", "fg" : "black"},
           "sys" : {"bg" : "#DCDCDC", "fg" : "black"},
           "title_font" : {"family" : "Times New Roman", "size" : 17, "style" : "bold"},
           "output_font" : {"family" : "Times New Roman", "size" : 13, "style" : ""}}

themes = [sky, classic, dark]

active_theme = 0

    # button size

button_width = 6
button_height = 4


# tkinter setup

window = tkinter.Tk()

window.title("BasiCal")

# equation variables
    
equation = []
    
tk_equation = tkinter.StringVar()
tk_equation.set(join_equation())


## GUI ##

# frames

frtitle = tkinter.Frame(window)
frtitle.pack()

froutput = tkinter.Frame(window)
froutput.pack()

frbuttons = tkinter.Frame(window)
frbuttons.pack()

# labels and buttons

    # title

title = tkinter.Label(frtitle, text="BasiCal 1.0")
title.configure(font = (themes[active_theme]["title_font"]["family"],
                        themes[active_theme]["title_font"]["size"],
                        themes[active_theme]["title_font"]["style"])) 
title.pack()

    # numbers

one = tkinter.Button(frbuttons, text="1", command=lambda: [append_to_equation("1"), tk_equation.set(join_equation())])
one.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
one.grid(row=3, column=0)
window.bind("1", lambda x: [equation.append("1"), tk_equation.set(join_equation())])

two = tkinter.Button(frbuttons, text="2", command=lambda: [append_to_equation("2"), tk_equation.set(join_equation())])
two.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
two.grid(row=3, column=1)
window.bind("2", lambda x: [equation.append("2"), tk_equation.set(join_equation())])

three = tkinter.Button(frbuttons, text="3", command=lambda: [append_to_equation("3"), tk_equation.set(join_equation())])
three.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
three.grid(row=3, column=2)
window.bind("3", lambda x: [equation.append("3"), tk_equation.set(join_equation())])

four = tkinter.Button(frbuttons, text="4", command=lambda: [append_to_equation("4"), tk_equation.set(join_equation())])
four.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
four.grid(row=2, column=0)
window.bind("4", lambda x: [equation.append("4"), tk_equation.set(join_equation())])

five = tkinter.Button(frbuttons, text="5", command=lambda: [append_to_equation("5"), tk_equation.set(join_equation())])
five.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
five.grid(row=2, column=1)
window.bind("5", lambda x: [equation.append("5"), tk_equation.set(join_equation())])

six = tkinter.Button(frbuttons, text="6", command=lambda: [append_to_equation("6"), tk_equation.set(join_equation())])
six.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
six.grid(row=2, column=2)
window.bind("6", lambda x: [equation.append("6"), tk_equation.set(join_equation())])

seven = tkinter.Button(frbuttons, text="7", command=lambda: [append_to_equation("7"), tk_equation.set(join_equation())])
seven.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
seven.grid(row=1, column=0)
window.bind("7", lambda x: [equation.append("7"), tk_equation.set(join_equation())])

eight = tkinter.Button(frbuttons, text="8", command=lambda: [append_to_equation("8"), tk_equation.set(join_equation())])
eight.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
eight.grid(row=1, column=1)
window.bind("8", lambda x: [equation.append("8"), tk_equation.set(join_equation())])

nine = tkinter.Button(frbuttons, text="9", command=lambda: [append_to_equation("9"), tk_equation.set(join_equation())])
nine.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
nine.grid(row=1, column=2)
window.bind("9", lambda x: [equation.append("9"), tk_equation.set(join_equation())])

zero = tkinter.Button(frbuttons, text="0", command=lambda: [append_to_equation("0"), tk_equation.set(join_equation())])
zero.configure(width = button_width, height = button_height, fg = themes[active_theme]["num"]["fg"], bg = themes[active_theme]["num"]["bg"])
zero.grid(row=4, column=1)
window.bind("0", lambda x: [equation.append("0"), tk_equation.set(join_equation())])

    # operator and format buttons

plus = tkinter.Button(frbuttons, text="+", command=lambda: [append_to_equation("+"), tk_equation.set(join_equation())])
plus.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
plus.grid(row=3, column=3)
window.bind("+", lambda x: [equation.append("+"), tk_equation.set(join_equation())])

minus = tkinter.Button(frbuttons, text="-", command=lambda: [append_to_equation("-"), tk_equation.set(join_equation())])
minus.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
minus.grid(row=4, column=3)
window.bind("-", lambda x: [equation.append("-"), tk_equation.set(join_equation())])

times = tkinter.Button(frbuttons, text="*", command=lambda: [append_to_equation("*"), tk_equation.set(join_equation())])
times.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
times.grid(row=2, column=4)
window.bind("*", lambda x: [equation.append("*"), tk_equation.set(join_equation())])

divided_by = tkinter.Button(frbuttons, text="/", command=lambda: [append_to_equation("/"), tk_equation.set(join_equation())])
divided_by.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
divided_by.grid(row=2, column=3)
window.bind("/", lambda x: [equation.append("/"), tk_equation.set(join_equation())])

equals = tkinter.Button(frbuttons, text="=", command=lambda: tk_equation.set("{}={}".format(join_equation(), result())))
equals.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
equals.grid(row=4, column=2)
window.bind("=", lambda x: tk_equation.set("{}={}".format(join_equation(equation), result())))
window.bind("<Return>", lambda x: tk_equation.set("{}={}".format(join_equation(), result())))

power = tkinter.Button(frbuttons, text="**", command=lambda: [append_to_equation("**"), tk_equation.set(join_equation())])
power.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
power.grid(row=4, column=4)
window.bind("#", lambda x: [equation.append("**"), tk_equation.set(join_equation())])

point = tkinter.Button(frbuttons, text=".", command=lambda: [append_to_equation("."), tk_equation.set(join_equation())])
point.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
point.grid(row=4, column=0)
window.bind(".", lambda x: [equation.append("."), tk_equation.set(join_equation())])

par_start = tkinter.Button(frbuttons, text="(", command=lambda: [append_to_equation("("), tk_equation.set(join_equation())])
par_start.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
par_start.grid(row=1, column=3)
window.bind("(", lambda x: [equation.append("("), tk_equation.set(join_equation())])

par_end = tkinter.Button(frbuttons, text=")", command=lambda: [append_to_equation(")"), tk_equation.set(join_equation())])
par_end.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
par_end.grid(row=1, column=4)
window.bind(")", lambda x: [equation.append(")"), tk_equation.set(join_equation())])

sq_root = tkinter.Button(frbuttons, text="√", command=lambda: [append_to_equation("**0.5"), tk_equation.set(join_equation())])
sq_root.configure(width = button_width, height = button_height, fg = themes[active_theme]["op"]["fg"], bg = themes[active_theme]["op"]["bg"])
sq_root.grid(row=3, column=4)
window.bind("r", lambda x: [append_to_equation("**0.5"), tk_equation.set(join_equation())])

    # system buttons

clear = tkinter.Button(frbuttons, text="C", command=clear)
clear.configure(width = button_width, height = int(button_height/2), fg = themes[active_theme]["sys"]["fg"], bg = themes[active_theme]["sys"]["bg"])
clear.grid(row=0, column=1)

delete = tkinter.Button(frbuttons, text="DEL", command=delete)
delete.configure(width = button_width, height = int(button_height/2), fg = themes[active_theme]["sys"]["fg"], bg = themes[active_theme]["sys"]["bg"])
delete.grid(row=0, column=2)

off = tkinter.Button(frbuttons, text="OFF", command=exit)
off.configure(width = button_width, height = int(button_height/2), fg = themes[active_theme]["sys"]["fg"], bg = themes[active_theme]["sys"]["bg"])
off.grid(row=0, column=0)

theme = tkinter.Button(frbuttons, text="Theme", command=change_theme)
theme.configure(width = button_width, height = int(button_height/2), fg = themes[active_theme]["sys"]["fg"], bg = themes[active_theme]["sys"]["bg"])
theme.grid(row=0, column=3)

    # output label

output = tkinter.Label(froutput, textvariable = tk_equation)
output.configure(font = (themes[active_theme]["output_font"]["family"],
                         themes[active_theme]["output_font"]["size"],
                         themes[active_theme]["output_font"]["style"]))
output.pack()


## BUTTON LISTS ##

buttons = [one, two, three, four, five, six, seven, eight, nine, zero, plus, minus, times, divided_by, equals, power, point, par_start, par_end, sq_root,
           clear, delete, off, theme]
num_buttons = [one, two, three, four, five, six, seven, eight, nine, zero]
sys_buttons = [clear, delete, off, theme]
op_buttons = [plus, minus, times, divided_by, equals, power, point, par_start, par_end, sq_root]


## MAIN LOOP ##

window.mainloop()

