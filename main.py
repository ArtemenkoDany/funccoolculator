import tkinter
from tkinter import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

root = Tk()


def plot(a, b, c, n):
    c = float(c)
    if c == 0:
        pass
    else:
        a = float(a)
        b = float(b)
        c = float(c)
        n = float(n)
        x = 101
        y = a + (b / c) * x ** n
        white = Label(
            text="                                                                                                 ")
        res = Label(text="y = " + str(y))
        res.grid(row=7, column=2, padx=5, pady=5)
        white.grid(row=7, column=2, padx=5, pady=5)
        # the figure that will contain the plot
        fig = Figure(figsize=(5, 5),
                     dpi=100)

        # list of squares
        y = [a + (b / c) * x ** n for x in range(101)]

        # adding the subplot
        plot1 = fig.add_subplot(111)

        # plotting the graph
        plot1.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                   master=root)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().grid(row=8, column=2, padx=5, pady=5)


        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().grid(row=8, column=2, padx=5, pady=5)


root.geometry(f"1080x720")
name = StringVar()

name_label = Label(text="Введіть a")
name_entry = Entry(textvariable=name)

nameb = StringVar()
name_labelb = Label(text="Введіть b")
name_entryb = Entry(textvariable=nameb)
namec = StringVar()
name_labelc = Label(text="Введіть c")
name_entryc = Entry(textvariable=namec)
namex = StringVar()

namen = StringVar()
name_labeln = Label(text="Введіть n")
name_entryn = Entry(textvariable=namen)

formula_label = Label(text="y=a+(b÷c)•xⁿ")

name_entry.grid(row=1, column=1, padx=5, pady=5)
name_entryb.grid(row=2, column=1, padx=5, pady=5)
name_entryc.grid(row=3, column=1, padx=5, pady=5)
name_entryn.grid(row=4, column=1, padx=5, pady=5)
name_label.grid(row=1, column=0, sticky="w")
name_labelb.grid(row=2, column=0, sticky="w")
name_labelc.grid(row=3, column=0, sticky="w")
name_labeln.grid(row=4, column=0, sticky="w")
formula_label.grid(row=0, column=0, sticky="w")


def clear_text():
    name_entry.delete(0, 'end')
    name_entryb.delete(0, 'end')
    name_entryc.delete(0, 'end')
    name_entryn.delete(0, 'end')


message_button = Button(text="Відправити", master=root, command=lambda: [plot(name_entry.get(), name_entryb.get(),
                                                                             name_entryc.get(), name_entryn.get()),
                                                                        clear_text()])
message_button.grid(row=6, column=1, padx=5, pady=5, sticky="e")

root.title('function')
root.mainloop()
