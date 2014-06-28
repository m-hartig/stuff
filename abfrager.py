from Tkinter import *
from random import randint


class Abfrager(object):

    """Die Klasse Abfrager dient dem Ueben der Malfolgen im Bereich 10 * 10."""

    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Malfolgen")

        self.aufgabe = Label(self.fenster, font=("Papyrus", 30), width=10)
        self.neue_aufgabe_erstellen()

        self.antwort = Entry(self.fenster)
        self.antwort.bind("<Return>", self.antwort_auswerten)

        self.auswertung = Label(
            self.fenster, text="Antwort eingeben ...",
            font=("Papyrus", 15), fg="grey"
        )

        self.aufgabe.pack()
        self.antwort.pack()
        self.auswertung.pack()
        self.fenster.mainloop()

    def neue_aufgabe_erstellen(self):
        a, b = randint(2, 10), randint(2, 10)
        self.aufgabe.config(text="%i * %i" % (a, b))
        self.loesung = str(a * b)

    def antwort_auswerten(self, event):
        if self.antwort.get() == self.loesung:
            self.auswertung.config(text="RICHTIG", fg="#33CC33")
            self.neue_aufgabe_erstellen()
        else:
            self.auswertung.config(text="FALSCH", fg="red")
        self.antwort.delete(0, END)


Abfrager()
