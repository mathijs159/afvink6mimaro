def main():
    #call van verschillende methodes
    bepaalGCpercentage (sequentie)

def bepaalGCpercentage (sequentie):
    #retourneert het GC percentage
    gCount = sequentie.count("G")
    cCount = sequentie.count("C")
    aCount = sequentie.count("A")
    tCount = sequentie.count("T")
    totalCount = gCount + cCount + aCount + tCount
    gcCount = gCount + cCount
    gcPercentage = float(gcCount) / float(totalCount)
    return(float(gcPercentage)*100)

def maakHTML (bepaalGCpercentage):
    #maakt een HTML bestand met de sequentie en berekende GC percentage
    

main()
