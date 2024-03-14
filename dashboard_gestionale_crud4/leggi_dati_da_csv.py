import pandas as pd

# Carica il file CSV
df = pd.read_csv("giacenza.csv", sep=";")

# Leggi solo le colonne DITTA, CODICE e GIACENZA
giacenza_subset = df[["DITTA", "CODICE", "GIACENZA"]]

# Stampalo
print(giacenza_subset)