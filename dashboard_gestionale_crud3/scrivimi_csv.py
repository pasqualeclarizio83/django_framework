import csv
import random

# Apri il file in modalità scrittura
with open('giacenze.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    
    # Scrivi l'intestazione del file CSV
    writer.writerow(['DITTA', 'CODICE', 'GIACENZA'])
    
    # Definisci il numero di righe da generare
    num_rows = 500
    
    # Genera e scrivi le righe del file CSV
    for _ in range(num_rows):
        # Genera valori casuali per DITTA, CODICE e GIACENZA
        ditta = 1
        codice = f"ART-{random.randint(100, 999)}"
        giacenza = random.randint(0, 100)
        
        # Scrivi la riga nel file CSV
        writer.writerow([ditta, codice, giacenza])