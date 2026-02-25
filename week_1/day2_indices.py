# Dato il dataset "sales" fare i seguenti esercizi

sales = [120, 90, 0, 310, 230, 180, 75, 210, 0, 95]

# Esercizio 1 - stampare indice e valore

for i in range(len((sales))):
   # if i == 8:
        print(i, sales[i])    #mi dice indice (posizione) e valore insieme

# Esercizio 2 - individuare posizioni anomale

for i in range(len(sales)):
        if sales[i] == 0:
            print("Anomalia è in posizione:", i)

# Esercizio 3 - Salvare le posizioni

indici_zeri =[]

for i in range(len(sales)):
       if sales[i] == 0:
              indici_zeri.append(i)
       print(indici_zeri)