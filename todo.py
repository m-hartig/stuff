from datetime import datetime
from json import load, dump


def datum_auswerten(datum):
    """Zeit bis zur Aufgabe wird ermittelt"""
    datum = map(int, datum.split("."))
    datum = datetime(datum[2], datum[1], datum[0])
    return [datum, (datum - datetime.now()).days]


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    datum, countdown = datum_auswerten(datum)
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))
    return {fach: [str(datum), thema, note, countdown]}


def ausgabe_der_aufgaben(aufgaben):
    """Darstellung der Aufgaben"""
    for key, value in sorted(aufgaben.iteritems(), key=lambda kvt: kvt[1][-1]):
        print key, ":", value


def main():
    """Hauptfunktion"""
    aufgaben = load(open("aufgaben.txt"))

    while True:
        ausgabe_der_aufgaben(aufgaben)

        auswahl = raw_input("> ").lower()

        if "neu" in auswahl:
            aufgaben.update(neue_aufgabe())
            dump(aufgaben, open("aufgaben.txt", "w"))
        else:
            break


if __name__ == '__main__':
    main()

# Was noch fehlt
# ======
# Verhalten, wenn Datei leer
# with Statement
# Countdown gilt nur fuer Erstellungstag
# Sortieren nach noch verbleibender Zeit
# Aufgabe mit Erinnerung durch OSX verbinden
# Online Zugang
# GUI
