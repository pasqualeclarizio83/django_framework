import csv
import random
import itertools

# Lista delle città italiane con codici a due lettere
città_italiane = [
    'AG', 'AL', 'AN', 'AO', 'AQ', 'AR', 'AP', 'AT', 'AV', 'BA', 'BT', 'BL', 'BN', 'BG', 'BI', 'BO', 'BZ', 'BS',
    'BR', 'CA', 'CL', 'CB', 'CI', 'CE', 'CT', 'CZ', 'CH', 'CO', 'CS', 'CR', 'KR', 'CN', 'EN', 'FM', 'FE', 'FI',
    'FG', 'FC', 'FR', 'GE', 'GO', 'GR', 'IM', 'IS', 'SP', 'AQ', 'LT', 'LE', 'LC', 'LI', 'LO', 'LU', 'MC', 'MN',
    'MS', 'MT', 'ME', 'MI', 'MO', 'MB', 'NA', 'NO', 'NU', 'OG', 'OT', 'OR', 'PD', 'PA', 'PR', 'PV', 'PG', 'PU',
    'PE', 'PC', 'PI', 'PT', 'PN', 'PZ', 'PO', 'RG', 'RA', 'RC', 'RE', 'RI', 'RN', 'RM', 'RO', 'SA', 'VS', 'SS',
    'SV', 'SI', 'SR', 'SO', 'TA', 'TE', 'TR', 'TO', 'TP', 'TN', 'TV', 'TS', 'UD', 'VA', 'VE', 'VB', 'VC', 'VR',
    'VV', 'VI', 'VT'
]

# Apri il file in modalità scrittura
with open('giacenze.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    
    # Scrivi l'intestazione del file CSV
    writer.writerow(['DITTA', 'CODICE', 'DEPOSITO', 'GIACENZA'])
    
    # Definisci il numero di righe da generare
    num_rows = 500
    
    # Genera e scrivi le righe del file CSV
    for _ in range(num_rows):
        # Genera valori casuali per DITTA, CODICE, DEPOSITO e GIACENZA
        ditta = 1
        codice = f"ART-{random.randint(100, 999)}"
        deposito = random.choice(città_italiane)
        giacenza = random.randint(0, 100)
        
        # Scrivi la riga nel file CSV
        writer.writerow([ditta, codice, deposito, giacenza])