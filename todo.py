from datetime import datetime, date
from json import load, dump


def datum_auswerten(datum):
    """Zeit bis zur Aufgabe wird ermittelt"""
    tag, monat, jahr = int(datum[:datum.index(".")]), int(
        datum[datum.index(".") + 1:-5]), int(datum[-4:])
    datum = date(jahr, monat, tag)
    return [datum, int(str(datum - date.today())[0])]


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
    for key in aufgaben.keys():
        print key, aufgaben[key]


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
# Sortieren nach noch verbleibender Zeit
# Aufgabe mit Erinnerung durch OSX verbinden
# Online Zugang
# GUI
