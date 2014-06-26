from datetime import datetime
from json import load, dump
from sys import argv

ABKUERZUNG_ZU_FACH = {"D": "Deutsch", "Ma": "Mathematik",
                      "Ru": "Russisch", "Eng": "Englisch"}


def schnell_aufgabe_erstellen(datum, fach, thema, aufgaben):
    """Schnelles Erstellen einer Aufgabe via Terminal"""
    aufgaben.update(
        {abkuerzung(fach): [str(datum_auswerten(datum)), thema, False]})


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))
    return {abkuerzung(fach): [str(datum_auswerten(datum)), thema, note]}


def abkuerzung_expandieren(fach):
    """Zuordnung der Abkuerzungen zu den Faechern"""
    return ABKUERZUNG_ZU_FACH.get(fach, fach)


def datum_auswerten(datum):
    """Datum wird zur Weiterverabeitung bearbeitet"""
    if "." in datum:
        # Deutsches Datum
        datum = map(int, datum.split("."))
        datum = datetime(datum[2], datum[1], datum[0])
    else:
        # Internationales Datum
        datum = map(int, datum.split("-"))
        datum = datetime(datum[0], datum[1], datum[2])
    return datum


def aufgabe_entfernen(aufgaben, fach):
    """Entfernen einer bestehenden Aufgabe"""
    del aufgaben[fach]


def ausgabe_der_aufgaben(aufgaben):
    """Ausgabe aller Aufgaben"""
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
    print


def main():
    aufgaben = load(open("aufgaben.txt"))

    if argv[1:]:
        # Wenn Paramter uebergeben wurden
        script, datum, fach, thema = argv
        schnell_aufgabe_erstellen(datum, fach, thema, aufgaben)
        dump(aufgaben, open("aufgaben.txt", "w"))
        exit()

    while True:
        ausgabe_der_aufgaben(aufgaben)

        print "Neue Aufgabe anlegen oder Aufgabe entfernen?"
        auswahl = raw_input("> ").lower()

        if "neu" in auswahl:
            aufgaben.update(neue_aufgabe())
            dump(aufgaben, open("aufgaben.txt", "w"))
            print
        elif "entf" in auswahl:
            fach = raw_input("Welches Fach: ")
            dump(aufgabe_entfernen(aufgaben, fach), open("aufgaben.txt", "w"))
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
