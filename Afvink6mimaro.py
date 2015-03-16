def main():
    #call van verschillende methodes
    #sequentie = "GAAATTAACACCCCCAG"
    
    deMuis = open("muis.txt", "r+")
    sequentie = deMuis.read()
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
    print("het gc percentage:") 
    print(float(gcPercentage)*100)

main()
    
