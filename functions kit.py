import tkinter as tk


# def identity(x):
#     '''Identity function'''
#     return x
#
#
# f = identity
# for attribute in (f.__name__,
#                   f.__doc__,
#                   f.__module__,
#                   f.__class__):
#     print(attribute)

# add_l = lambda x, y: x + y
# print(add_l(1, 120))
#
#
# def under_lambda(x, y):
#     return add_l(x, y)
# print(under_lambda(8, 3))

class App:
    """"""

    def __init__(self, parent):
        """Конструктор"""
        frame = tk.Frame(parent)
        frame.pack()

        btn22 = tk.Button(
            frame,
            text="22",
            command=lambda: self.printNum(22)
        )
        btn22.pack(side=tk.LEFT)

        btn44 = tk.Button(
            frame,
            text="44",
            command=lambda: self.printNum(44)
        )
        btn44.pack(side=tk.LEFT)

        quitBtn = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
        quitBtn.pack(side=tk.LEFT)

    def printNum(self, num):
        print("Вы нажали кнопку: %s" % num)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
