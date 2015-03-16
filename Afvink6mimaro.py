def main():
    #call van verschillende methodes
<<<<<<< HEAD
    #sequentie = "GAAATTAACACCCCCAG"
    
    deMuis = open("muis.txt", "r+")
    sequentie = deMuis.read()
=======
>>>>>>> 79d4d81721a30322477bdeea7f33331d3cd703f2
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
<<<<<<< HEAD
    print("het gc percentage:") 
    print(float(gcPercentage)*100)
=======
    return(float(gcPercentage)*100)
>>>>>>> 79d4d81721a30322477bdeea7f33331d3cd703f2

main()
