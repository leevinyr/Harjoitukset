while(True):   
    tuumat = float(input("Anna tuumat (alle 0 lopettaa): "))
    if(tuumat > 0):
        print("Annetut tuumat senttimetreinä:", tuumat * 2.54)
        continue
    elif(tuumat < 0):
        break