import csv

input_csv = "lexpredict-legal-dictionary/sources/blacks_second_edition/blacks_second_edition_terms.csv"
output_txt = "legal_llm/dataset.txt"

with open(input_csv, newline='', encoding='utf-8') as csvfile, open(output_txt, 'w', encoding='utf-8') as txtfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        term = row['term']
        definition = row['definition']
        if term and definition:
            txtfile.write(f"{term}: {definition}\n") 