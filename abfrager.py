from Tkinter import *
from random import randint


class Abfrager(object):

    """Klasse dient zum Ueben der Malfolgen im Bereich 10 * 10"""

    def __init__(self):
        self.fenster = Tk()

        self.aufgabe = Label(self.fenster, font=("Papyrus", 30), width=10)
        self.neue_aufgabe()

        self.antwort = Entry(self.fenster)
        self.antwort.bind("<Return>", self.antwort_auswerten)

        self.auswertung = Label(
            self.fenster, text="Antwort eingeben ...",
            font=("Comic Sans MS", 15), fg="grey"
        )

        self.aufgabe.pack(pady=5)
        self.antwort.pack()
        self.auswertung.pack(pady=5)

        self.fenster.mainloop()

    def neue_aufgabe(self):
        a, b = randint(2, 10), randint(2, 10)
        self.aufgabe.config(text="%i * %i" % (a, b))
        self.loesung = str(a * b)

    def antwort_auswerten(self, event):
        if self.antwort.get() == self.loesung:
            self.auswertung.config(text="RICHTIG", fg="green")
            self.neue_aufgabe()
        else:
            self.auswertung.config(text="FALSCH", fg="red")

        self.antwort.delete(0, END)

Abfrager()
