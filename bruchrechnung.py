
def bruch_aufbereiten(bruch):
    """Bruch wird am Bruchstrich in Zaehler und Nenner geteilt"""
    zaehler, nenner = bruch.split("/")
    return [int(zaehler), int(nenner)]


def nenner_angleichen(a, b):
    """Nenner von Bruch a und b werden angeglichen"""
    c = a[:]
    # Zaehler und Nenner von a mit Nenner von b multipliziert
    a[0], a[-1] = a[0] * b[-1], a[-1] * b[-1]
    # Zaehler und Nenner von b mit Nenner von a multipliziert
    b[0], b[-1] = b[0] * c[-1], b[-1] * c[-1]
    return [a, b]


def kuerzen(bruch):
    """Bruch mit Euklidischen Algorithmus gekuerzt"""
    term = bruch[:]

    while term[-1] != 0:
        term[0], term[-1] = term[-1], term[0] % term[-1]
    ggt = term[0]

    bruch[0] /= ggt
    bruch[-1] /= ggt
    return bruch


def main():
    """Hauptfunktion"""
    a = "10/20"
    b = "5/2"

    a, b = bruch_aufbereiten(a), bruch_aufbereiten(b)

    if a[-1] != b[-1]:
        a, b = nenner_angleichen(a, b)

    print "Summe", '/'.join(str(x) for x in kuerzen([a[0] + b[0], a[-1]]))
    print "Differenz", '/'.join(str(x) for x in kuerzen([a[0] - b[0], a[-1]]))
    print "Produkt", '/'.join(str(x) for x in kuerzen([a[0] * b[0], a[-1] * a[-1]]))
    print "Quotients", '/'.join(str(x) for x in kuerzen([a[0] * b[-1], a[-1] * b[0]]))


if __name__ == '__main__':
    main()
