from datetime import datetime
from json import load, dump
from sys import argv


def abkuerzung(fach):
    """Zuordnung der Faecher zu den Abkuerzungen"""
    faecher = {"D": "Deutsch", "Ma": "Mathematik",
               "Ru": "Russisch", "Eng": "Englisch"}

    if fach in faecher:
        return faecher[fach]
    else:
        return fach


def datum_auswerten(datum):
    """Zeit bis zur Aufgabe wird ermittelt"""
    if "." in datum:
        # Deutsches Datum
        datum = map(int, datum.split("."))
        datum = datetime(datum[2], datum[1], datum[0])
    else:
        # Amerikanisches Datum
        datum = map(int, datum.split("-"))
        datum = datetime(datum[0], datum[1], datum[2])
    return datum


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))
    return {abkuerzung(fach): [str(datum_auswerten(datum)), thema, note]}


def ausgabe_der_aufgaben(aufgaben):
    """Darstellung der Aufgaben"""
    print
    for key, value in sorted(aufgaben.iteritems()):
        # countdown = Tage von heute bis zum Datum
        countdown = (datum_auswerten(value[0][:10]) - datetime.now()).days + 1
        # 00:00:00 entfernen
        value[0] = value[0][:10]

        print "%s - noch %d Tag(e)" % (key, countdown)
        for eintrag in value:
            print eintrag
    print


def schnell_aufgabe_erstellen(datum, fach, thema, aufgaben):
    """Schnelles Erstellen einer Aufgabe via Terminal"""
    aufgaben.update(
        {abkuerzung(fach): [str(datum_auswerten(datum)), thema, False]})


def main():
    """Hauptfunktion"""
    aufgaben = load(open("aufgaben.txt"))

    if argv[1:]:
        # Wenn Paramter uebergeben wurden
        script, datum, fach, thema = argv
        schnell_aufgabe_erstellen(datum, fach, thema, aufgaben)
        dump(aufgaben, open("aufgaben.txt", "w"))
        exit()

    while True:
        ausgabe_der_aufgaben(aufgaben)

        print "Neue Aufgabe anlegen?"
        auswahl = raw_input("> ").lower()

        if "ja" in auswahl:
            aufgaben.update(neue_aufgabe())
            dump(aufgaben, open("aufgaben.txt", "w"))
            print
        else:
            break


if __name__ == '__main__':
    main()

# Was noch fehlt
# ======
# Verhalten, wenn Datei leer
# with Statement
# Sortieren nach noch verbleibender Zeit
# Aufgabe mit Erinnerung durch OSX verbinden
# Online Zugang
# GUI
