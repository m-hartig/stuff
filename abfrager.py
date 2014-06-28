from Tkinter import *
from random import randint


class Abfrager(object):

    """Klasse dient als Abfrager fuer Malfolgen im Bereich 10 * 10"""

    def __init__(self):
        self.fenster = Tk()

        self.aufgabe = Label(
            self.fenster, font=("Comic Sans MS", 20), width=20)
        self.neue_aufgabe()

        self.antwort = Entry(self.fenster)
        self.antworten = Button(
            self.fenster, text="Antworten", command=self.antwort_auswerten)
        self.auswertung = Label(self.fenster, font=("Comic Sans MS", 15))

        self.aufgabe.pack()
        self.antwort.pack()
        self.antworten.pack()
        self.auswertung.pack(pady=10)

        self.fenster.mainloop()

    def neue_aufgabe(self):
        a, b = randint(1, 10), randint(1, 10)
        self.aufgabe.config(text="%i * %i" % (a, b))
        self.loesung = str(a * b)

    def antwort_auswerten(self):
        if self.antwort.get() == self.loesung:
            self.auswertung.config(text="RICHTIG", fg="green")
            self.neue_aufgabe()
        else:
            self.auswertung.config(text="FALSCH", fg="red")

        self.antwort.delete(0, END)

Abfrager()
