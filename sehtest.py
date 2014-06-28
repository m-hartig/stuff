from Tkinter import *
from random import choice


class Sehtest(object):

    """Klasse modelliert einen Sehtest bestehend aus 3 Reihen, welche eine unterschiedliche Schriftgroese aufweisen"""

    def __init__(self):
        self.fenster = Tk()
        self.button = Button(self.fenster, text="neu!", command=self.neu)
        self.label = [
            Label(self.fenster, font=("Arial", 40), width=6),
            Label(self.fenster, font=("Arial", 20), width=6),
            Label(self.fenster, font=("Arial", 10), width=6)
        ]
        self.neu()
        for l in self.label:
            l.pack()
        self.button.pack(pady=10)
        self.fenster.mainloop()

    def neu(self):
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for l in self.label:
            zeichen = choice(a) + " " + choice(a) + " " + choice(a)
            l.config(text=zeichen)

sehtest = Sehtest()
