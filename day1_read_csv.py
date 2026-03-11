file = open("week2/data/security_log.csv", "r")

for riga in file:
    riga = riga.strip()   #riga.strip() è la funzione che rimuove gli spazi iniziali e finali della stringa.
    colonne = riga.split(",") #ho una lista con i campi della riga
    
    print(colonne)            
 
file.close()