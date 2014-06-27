from datetime import datetime
from json import load, dump
from sys import argv

ABKUERZUNG_ZU_FACH = {"D": "Deutsch", "Ma": "Mathematik",
                      "Ru": "Russisch", "Eng": "Englisch"}

try:
    AUFGABEN = load(open("aufgaben.txt"))
except:
    dump(dict(), open("aufgaben.txt", "w"))
    AUFGABEN = load(open("aufgaben.txt"))


def schnell_aufgabe_erstellen(datum, fach, thema):
    """Schnelles Erstellen einer Aufgabe via Terminal"""
    AUFGABEN[abkuerzung(fach)] = [str(datum_auswerten(datum)), thema, False]


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))

    return {abkuerzung_expandieren(fach): [str(datum_auswerten(datum)), thema, note]}


def aufgabe_entfernen(fach):
    """Entfernen einer bestehenden Aufgabe"""
    del AUFGABEN[abkuerzung_expandieren(fach)]


def abkuerzung_expandieren(fach):
    """Zuordnung der Abkuerzungen zu den Faechern"""
    return ABKUERZUNG_ZU_FACH.get(fach, fach)


def datum_auswerten(datum):
    """Datum wird zur Weiterverabeitung bearbeitet"""
    try:
        # Deutsches Datum
        tag, monat, jahr = map(int, datum.split("."))
    except:
        # Internationales Datum
        jahr, monat, tag = map(int, datum.split("-"))

    return datetime(jahr, monat, tag)


def countdown_berechnen(datum):
    """Berechnen der noch verbleibenden Zeit"""
    # Addieren mit 1, da heutiger Tag mitgerechnet werden soll
    return (datum_auswerten(datum) - datetime.now()).days + 1


def ausgabe_der_aufgaben():
    """Ausgabe aller Aufgaben"""
    for key, value in sorted(AUFGABEN.iteritems()):
        print "%s - noch %d Tag(e)" % (key, countdown_berechnen(value[0][:10]))
        for eintrag in value:
            print eintrag
        print


def main():
    """Hauptfunktion"""

    if argv[1:]:
        script, datum, fach, thema = argv
        schnell_aufgabe_erstellen(datum, fach, thema)
        dump(AUFGABEN, open("aufgaben.txt", "w"))
    else:
        while True:
            ausgabe_der_aufgaben()

            print "Neue Aufgabe anlegen oder Aufgabe entfernen?"
            auswahl = raw_input("> ").lower()

            if "neu" in auswahl or "neue" in auswahl:
                AUFGABEN.update(neue_aufgabe())
                dump(AUFGABEN, open("aufgaben.txt", "w"))

            elif "entf" in auswahl or "del" in auswahl:
                fach = raw_input("Welches Fach: ")
                aufgabe_entfernen(fach)
                dump(AUFGABEN, open("aufgaben.txt", "w"))

            else:
                break

    AUFGABEN.close()


if __name__ == '__main__':
    main()

# Was noch fehlt
# ======
# Sortieren nach noch verbleibender Zeit + Note
