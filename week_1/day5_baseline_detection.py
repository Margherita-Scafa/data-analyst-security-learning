# Esercizio 1 - Calcolare la baseline

sales = [120, 90, 0, 310, 230, 180, 75, 210, 0, 95]

somma = 0

for valore in sales:
    somma += valore

baseline = somma/ len(sales)

print( "Baseline vendite:", baseline)

# Esercizio 2 - Identificare il valore sopra la soglia

soglia = 250

for i in range(len(sales)):
     if sales[i] > soglia:
          print("Evento anomalo | posizione", i, "| valore:", sales[i])


# Esercizio 3 - Costruire un piccolo report

anomalie = []

for i in range(len(sales)):
     if sales[i] > soglia:
          anomalie.append((i, sales[i]))

print("Numero anomalie", len(anomalie))
print("Dettaglio", anomalie)



