def main():
    #call van verschillende methodes
    #sequentie = "GAAATTAACACCCCCAG"
    
    bestandsNaam = "muis.txt"
    htmlBestand = "afvink6.html"
    sequentie = leesBestand(bestandsNaam)
    gcPercentage = bepaalGCpercentage (sequentie)
    maakHTML (gcPercentage, sequentie, bestandsNaam, htmlBestand)
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

def maakHTML (gcPercentage, sequentie, bestandsNaam, htmlBestand):
    #maakt een HTML bestand met de sequentie en berekende GC percentage
    file = open(htmlBestand, "w")
    
    message = """<html>
    <head></head>
    <body><p>bestandsnaam:  {bestandsNaam}</p><br
    <p>gcPercentage: {gcPercentage}</p><br
    <p>sequentie: {sequentie}</p></body>
    </html>""".format(bestandsNaam=bestandsNaam, gcPercentage=gcPercentage, sequentie=sequentie)

    file.write(message)
    file.close
    
main()
