sales = [120, 90, 0, 310, 230, 180, 75, 210, 0, 95]
regions = ["N", "S", "N", "C", "S", "S", "C", "N", "C", "N"]

# Esercizio 1 - Stampare evento + contesto

for i in range(len(sales)):
    print("Vendita:", sales[i], "Regioni:", regions[i])

# Esercizio 2 - Anomalia con contesto
# trova le vendita a 0 e stampa anche la regione

for i in range(len(sales)):
    if sales[i] == 0:
        print("Anomalia | Posizione:", i, "| Regioni:", regions[i])

# Esercizio 3 - Contatore per categoria
# conta quante vendite a 0 ci sono per regione

zeri_per_regione = {"N": 0, "S": 0, "C": 0}

for i in range(len(sales)):
    if sales[i] == 0:
        regione = regions[i]
        zeri_per_regione[regione] += 1
print(zeri_per_regione)

