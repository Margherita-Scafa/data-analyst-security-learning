#Dataset di oggi
# Esercizio 1 - check di coerenza lunghezze

sales = [120, 90, 0, 310, 230, 180, 75, 210, 0, 95]
regions = ["N", "S", "N", "C", "S", "S", "C", "N", "C", "N"]

if len(sales) != len(regions):
    print("ERRORE: dataset paralleli incoerenti")
    print("len()sales) = ", len(sales))
    print("len(regions) = ", len(regions))
else:
    print("OK: dataset coerenti, posso analizzare")

# Esercizio 2 - Validare i valori (regole semplici)
# obiettivo: segnalare valori invalidi (negativi o non numerici)

invalidi = 0

for valore in sales:
    if not isinstance(valore, (int, float)): # isinstance è quella funzione che ti restituisce True se l'oggetto specificato è del tipo 
        invalidi +=1                         # specificato, altrimenti dà False   
    elif valore < 0:
        invalidi +=1
print("Valori invalidi:", invalidi)

# Esercizio 3 - Analisi solo se i dati sono OK
# Unisci tutto: controlli prima, analisi poi

if len(sales) == len(regions):
    zeri_per_regione = {"N": 0, "S": 0, "C": 0}

    for i in range(len(sales)):
        if sales[i] ==0:
            regione = regions[i]
            zeri_per_regione[regione] += 1
    print("Zeri per regione:", zeri_per_regione)
else:
    print("Analisi saltata: dataset incoerenti")