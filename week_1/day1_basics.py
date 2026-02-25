# Dataset di oggi
#ESERCIZIO 1 - Scansione del dataset

sales = [120, 90, 0, 310, 230, 180, 75, 210, 0, 95]

#obiettivo:capire cosa fa davvero un ciclo for

for valore in sales:
    print(valore)

# Quante volte gira il ciclo? Tante volte quanto sono i valori presenti nel dataset

# Cosa rappresenta "valore" ? Rappresenta la variabile a cui ogni volta viene assegnato il numero all'interno della lista "sales"

#ESERCIZIO 2 - Accumulatore (ripasso solido)

somma = 0

for valore in sales:
    somma += valore #somma tutti i valori

print("Somma:", somma)

# ESERCIZIO 3 - Controllo condizionale
# Stampa solo valori maggiori di 200

for valore in sales:
    if valore > 200:
        print(valore)  # questo è già data filtering

# ESERCIZI 4 - Contatore (qualità dato)
# Conta quante vendite sono pari a 0

conta_zeri = 0

for valore in sales:
    if valore ==0:
        conta_zeri +=1

print("Numero di zeri:", conta_zeri)
