import csv
import random
import string

def generate_random_code():
    code_prefix = ''.join(random.choices(string.digits, k=3))
    code_suffix = ''.join(random.choices(string.ascii_uppercase, k=3))
    return f"{code_prefix}{code_suffix}ne10"

def generate_description():
    return "Descrizione generica"

def generate_records(num_records):
    records = []
    for _ in range(num_records):
        ditta = "1"
        codice = generate_random_code()
        descrizione = generate_description()
        records.append((ditta, codice, descrizione))
    return records

def write_to_csv(filename, records):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["DITTA", "CODICE", "DESCRIZIONE"])
        writer.writerows(records)

if __name__ == "__main__":
    num_records = 200
    records = generate_records(num_records)
    write_to_csv("articoli.csv", records)
