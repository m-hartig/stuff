from datetime import datetime
from json import load, dump


def datum_auswerten(datum):
    """Zeit bis zur Aufgabe wird ermittelt"""
    if "." in datum:
        datum = map(int, datum.split("."))
        datum = datetime(datum[2], datum[1], datum[0])
    else:
        datum = map(int, datum.split("-"))
        datum = datetime(datum[0], datum[1], datum[2])
    return datum


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))
    return {fach: [str(datum_auswerten(datum)), thema, note]}


def ausgabe_der_aufgaben(aufgaben):
    """Darstellung der Aufgaben"""
    for key, value in sorted(aufgaben.iteritems(), key=lambda kvt: kvt[1][-1]):
        countdown = (datum_auswerten(value[0][:10]) - datetime.now()).days + 1
        value[0] = value[0][:10]
        print "%s - noch %d Tag(e)" % (key, countdown)
        for eintrag in value:
            print eintrag
        print


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
# datum - datetime.now()).days
# with Statement
# Countdown gilt nur fuer Erstellungstag -> IN Ansicht einbauen
# Sortieren nach noch verbleibender Zeit
# Aufgabe mit Erinnerung durch OSX verbinden
# Online Zugang
# GUI
