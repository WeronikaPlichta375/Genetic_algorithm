import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


import numpy as np

list_score = [33054.0, 27408.0, 23591.0, 32307.0, 29677.0, 28329.0, 31656.0, 31477.0, 32236.0, 29108.0, 1, 36853.0, 36914.0, 32025.0, 1, 34774.0, 34034.0, 36645.0, 31886.0, 35004.0, 32275.0, 35883.0, 36532.0, 35473.0, 38743.0, 37811.0, 37321.0, 38812.0, 37311.0, 39682.0, 36182.0, 38182.0, 35533.0, 35533.0, 40410.0, 39960.0, 37923.0, 33443.0, 40410.0, 38182.0, 38182.0, 35533.0, 35533.0, 41059.0, 39311.0, 38182.0, 37761.0, 37761.0, 41059.0, 39281.0, 39281.0, 35533.0, 38182.0, 35533.0, 38182.0, 40410.0, 36632.0, 41059.0, 38182.0, 36632.0, 36632.0, 39960.0, 36632.0, 36632.0, 35533.0, 39281.0, 36632.0, 36632.0, 39281.0, 39281.0, 39281.0, 39281.0, 39281.0, 39281.0, 39281.0, 36632.0, 39281.0, 41059.0, 39281.0, 39930.0, 39281.0, 39930.0, 41059.0, 39281.0, 39930.0, 41059.0, 39930.0, 39930.0, 41059.0, 41059.0, 39930.0, 41059.0, 39281.0, 39281.0, 41059.0, 39281.0, 41059.0, 41059.0, 40410.0, 41059.0, 41059.0]
root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=150)
t = np.arange(0, 101, 1)
fig.add_subplot(111).plot(t, list_score)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()

def show_graph(list_score):

    root = tkinter.Tk()
    root.wm_title("Embedding in Tk")

    fig = Figure(figsize=(5, 4), dpi=150)
    t = np.arange(0, 101, 1)
    fig.add_subplot(111).plot(t, list_score)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", on_key_press)
    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)

    tkinter.mainloop()