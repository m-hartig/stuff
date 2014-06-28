from datetime import datetime, timedelta
from pickle import load, dump
from sys import argv


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))

    aufgaben[abkz_expand(fach)] = [str(datum_auswerten(datum)), thema, note]


def datum_auswerten(datum):
    """Datum wird zur Weiterverabeitung bearbeitet"""
    try:
        tag, monat, jahr = map(int, datum.split("."))
    except ValueError:
        jahr, monat, tag = map(int, datum.split("-"))

    return datetime(jahr, monat, tag)


def schnell_aufgabe_erstellen(fach, thema):
    """Schnelles Erstellen einer Aufgabe via Terminal: python todo.py Ph LK"""
    aufgaben[abkz_expand(fach)] = [
        # Termin morgen, da eigentlicher Termin unbekannt
        str(datetime.today() + timedelta(days=1)),
        # Beschreibung der Aufgabe in einem Wort
        thema,
        # Keine Benotung, da schnelle Aufgabe meist ohne Note
        False
    ]
    print "Aufgabe wurde erstellt."


def aufgabe_entfernen():
    """Entfernen einer bestehenden Aufgabe"""
    fach = raw_input("Welches Fach: ")

    if fach not in aufgaben:
        print "Keine Aufgabe in diesem Fach"
        return
    elif raw_input("Sind Sie sich sicher? ") == "ja":
        del aufgaben[abkz_expand(fach)]
    else:
        return


def abkz_expand(fach):
    """Zuordnung der Abkuerzungen zu den Faechern"""
    abkuerzung_zu_fach = {"d": "Deutsch", "Ma": "Mathematik",
                          "ru": "Russisch", "Eng": "Englisch",
                          "info": "Informatik", "Ph": "Physik",
                          "bio": "Biologie", "Ch": "Chemie"}
    return abkuerzung_zu_fach.get(fach, fach)


def ausgabe_der_aufgaben():
    """Ausgabe aller Aufgaben"""
    print
    for key, value in sorted(aufgaben.iteritems()):
        print "%s - noch %d Tag(e)" % (key, countdown_berechnen(value[0][:10]))
        for eintrag in value:
            print eintrag
        print


def countdown_berechnen(datum):
    """Berechnen der noch verbleibenden Zeit"""
    # Addieren mit 1, da heutiger Tag mitgerechnet werden soll
    return (datum_auswerten(datum) - datetime.now()).days + 1


def programm_steuern(menue):
    """Steuerung des Programmes ueber ein Menue"""
    while True:
        print "=== Aufgabenverwaltung ==="
        for index, item in enumerate(menue, 1):
            print "{}  {}".format(index, item[0])

        auswahl = int(raw_input("> ")) - 1

        if auswahl == 3:
            if programm_beenden():
                break
        elif 0 <= auswahl < len(menue):
            menue[auswahl][1]()
        else:
            print "Nur Zahlen im Bereich 1 - {} eingeben".format(len(menue))


def programm_beenden():
    """"Ausgabe bei Beenden der While-Schleife"""
    if raw_input("Wollen Sie das Programm wirklich beenden? ") == "ja":
        return True
    return False


def datei_laden():
    """Dictionary aus Datei wird geladen"""
    with open("aufgaben.txt") as datei:
        aufgaben = load(datei)
    return aufgaben


def in_datei_schreiben(daten):
    """Dictionary wird in Datei gespeichert"""
    with open("aufgaben.txt", "w") as datei:
        dump(daten, datei)


try:
    aufgaben = datei_laden()
except IOError:
    # Wenn die Datei leer ist, soll sie mit einem Dictionary gefuellt werden
    in_datei_schreiben(dict())
    aufgaben = datei_laden()


def main():
    """Hauptfunktion"""
    menue = [
        ["Alle Aufgaben anzeigen", ausgabe_der_aufgaben],
        ["Neue Aufgabe anlegen", neue_aufgabe],
        ["Aufgabe entfernen", aufgabe_entfernen],
        ["Programm beenden", programm_beenden]
    ]

    if argv[1:]:
        script, fach, thema = argv
        schnell_aufgabe_erstellen(fach, thema)
    else:
        programm_steuern(menue)

    in_datei_schreiben(aufgaben)

if __name__ == '__main__':
    main()
