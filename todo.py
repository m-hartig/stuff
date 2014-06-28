from datetime import datetime, timedelta
import pickle
from sys import argv


def schnell_aufgabe_erstellen(fach, thema):
    """Schnelles Erstellen einer Aufgabe via Terminal"""
    aufgaben[abkz_expand(fach)] = [
        # Termin morgen, da eigentlicher Termin unbekannt
        str(datetime.today() + timedelta(days=1)),
        thema,
        # Keine Benotung, da schnelle Aufgabe meist ohne Note
        False
    ]
    print "Aufgabe wurde erstellt."


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))

    aufgaben[abkz_expand(fach)] = [str(datum_auswerten(datum)), thema, note]


def aufgabe_entfernen():
    """Entfernen einer bestehenden Aufgabe"""
    fach = raw_input("Welches Fach: ")
    if raw_input("Sind Sie sich sicher? ") == "ja":
        del aufgaben[abkz_expand(fach)]
    else:
        return


def abkz_expand(fach):
    """Zuordnung der Abkuerzungen zu den Faechern"""
    abkuerzung_zu_fach = {"D": "Deutsch", "Ma": "Mathematik",
                          "Ru": "Russisch", "Eng": "Englisch"}
    return abkuerzung_zu_fach.get(fach, fach)


def datum_auswerten(datum):
    """Datum wird zur Weiterverabeitung bearbeitet"""
    try:
        tag, monat, jahr = map(int, datum.split("."))
    except:
        jahr, monat, tag = map(int, datum.split("-"))

    return datetime(jahr, monat, tag)


def countdown_berechnen(datum):
    """Berechnen der noch verbleibenden Zeit"""
    # Addieren mit 1, da heutiger Tag mitgerechnet werden soll
    return (datum_auswerten(datum) - datetime.now()).days + 1


def ausgabe_der_aufgaben():
    """Ausgabe aller Aufgaben"""
    for key, value in sorted(aufgaben.iteritems()):
        print "%s - noch %d Tag(e)" % (key, countdown_berechnen(value[0][:10]))
        for eintrag in value:
            print eintrag
        print


def programm_beenden():
    """"Ausgabe bei Beenden der While-Schleife"""
    return "Programm wurde beendet"


def programm_steuern(menue):
    """Steuerung des Programmes ueber ein Menue"""
    while True:
        print "=== Aufgabenverwaltung ==="
        for index, item in enumerate(menue, 1):
            print "{}  {}".format(index, item[0])

        auswahl = int(raw_input("> ")) - 1

        if auswahl == 3:
            print programm_beenden()
            break
        elif 0 <= auswahl < len(menue):
            menue[auswahl][1]()
        else:
            print "Nur Zahlen im Bereich 1 - {} eingeben".format(len(menue))


def datei_laden():
    """Dictionary aus Datei wird geladen"""
    datei = open("aufgaben.txt")
    aufgaben = pickle.load(datei)
    return aufgaben


def in_datei_schreiben(daten):
    """Dictionary wird in Datei gespeichert"""
    datei = open("aufgaben.txt", "w")
    pickle.dump(daten, datei)
    datei.close()

menue = [
    ["Alle Aufgaben anzeigen", ausgabe_der_aufgaben],
    ["Neue Aufgabe anlegen", neue_aufgabe],
    ["Aufgabe entfernen", aufgabe_entfernen],
    ["Programm beenden", programm_beenden]
]

try:
    aufgaben = datei_laden()
except IOError:
    in_datei_schreiben(dict())
    aufgaben = datei_laden()

if argv[1:]:
    script, fach, thema = argv
    schnell_aufgabe_erstellen(fach, thema)
else:
    programm_steuern(menue)

in_datei_schreiben(aufgaben)

# Was noch fehlt/zu tun ist
# ======
# Datumseingabe, MenueEingabe ueberpruefen lassen
# Excpet in datum_auswerten praezisieren
# Schnellaufgabe funktioniert nicht
# Sortieren nach noch verbleibender Zeit + Note
