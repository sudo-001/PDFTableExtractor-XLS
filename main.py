import tabula
import pandas as pd

def extract_and_save_tables(pdf_path):
    # Lecture des tables du fichier PDF
    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
    # split les 13 derniers éléments de pdf_path tu mets dans une variable name
    name = pdf_path.split('/')[-1]
    name = name.split('.')[0]

    # Vérification et traitement de chaque table extraite
    for i, table in enumerate(tables):
        # Nettoyage des données si besoin : todo (table = clean_table(table))

        # Sauvegarde en xls
        table.to_csv(f"./output/{name}_{i+1}.xls", index=False)
        print(f"Table {i+1} enregistrée en tant que {name}_{i+1}.csv")

extract_and_save_tables('./source/KNSR5001.pdf')