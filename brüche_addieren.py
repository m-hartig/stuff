
def bruch_aufbereiten(bruch):
    """Bruch wird in Zaehler und Nenner geteilt"""
    strich = bruch.index("/")
    zaehler = bruch[:strich]
    nenner = bruch[strich + 1:]
    return [int(zaehler), int(nenner)]


def nenner_angleichen(a, b):
    """Nenner von Bruch a und b werden angeglichen"""
    c = a[:]
    a[0], a[-1] = a[0] * b[-1], a[-1] * b[-1]
    b[0], b[-1] = b[0] * c[-1], b[-1] * c[-1]
    return [a, b]


def kuerzen(bruch):
    """Bruch mit Euklidischen Algorithmus gekuerzt"""
    term = bruch[:]

    while term[-1] != 0:
        term[0], term[-1] = term[-1], term[0] % term[-1]
    ggt = term[0]

    bruch[0] = bruch[0] / ggt
    bruch[-1] = bruch[-1] / ggt
    return bruch


def main():
    """Hauptfunktion"""
    a, b = "2/4", "8/5"
    a, b = bruch_aufbereiten(a), bruch_aufbereiten(b)

    if a[-1] != b[-1]:
        a, b = nenner_angleichen(a, b)

    print "Summe:\t\t", kuerzen([a[0] + b[0], a[-1]])
    print "Diffenrenz:\t", kuerzen([a[0] - b[0], a[-1]])
    print "Produkt:\t", kuerzen([a[0] * b[0], a[-1] * a[-1]])
    print "Quotient:\t", kuerzen([a[0] * b[-1], a[-1] * b[0]])

if __name__ == '__main__':
    main()
