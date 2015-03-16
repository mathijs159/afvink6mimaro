def main():
    #call van verschillende methodes
    #sequentie = "GAAATTAACACCCCCAG"
    
    bestandsNaam = "muis.txt"
    sequentie = leesBestand(bestandsNaam)
    bepaalGCpercentage (sequentie)
    #print(sequentie)
    
def bepaalGCpercentage (sequentie):
    #retourneert het GC percentage
    gCount = sequentie.count("G")
    cCount = sequentie.count("C")
    aCount = sequentie.count("A")
    tCount = sequentie.count("T")
    totalCount = gCount + cCount + aCount + tCount
    gcCount = gCount + cCount
    gcPercentage = float(gcCount) / float(totalCount)

    return (float(gcPercentage)*100)

def leesBestand (bestandsNaam):
    deMuis = open(bestandsNaam, "r+")
    sequentie = deMuis.read()
    return sequentie

def maakHTML (gcPercentage, sequentie, bestandsnaam):
    #maakt een HTML bestand met de sequentie en berekende GC percentage
    file = open("afvink6.html")

    message = """<html>
    <head></head>
    <body><p>Hello! Martijn</p></body>
    </html>"""
    
main()
