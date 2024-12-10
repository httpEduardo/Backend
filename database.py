import sqlite3
import pandas as pd

def initialize_database():
    conn = sqlite3.connect(":memory:")  # Banco de dados em memória
    cursor = conn.cursor()

    # Criar tabela
    cursor.execute("""
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            title TEXT,
            studios TEXT,
            producers TEXT,
            winner BOOLEAN
        )
    """)

    # Ler CSV e tratar valores nulos
    data = pd.read_csv("Movielist.csv", sep=";").fillna("")  # Substituir NaN por string vazia
    for _, row in data.iterrows():
        winner = 1 if str(row['winner']).strip().lower() == "yes" else 0
        cursor.execute("""
            INSERT INTO movies (year, title, studios, producers, winner)
            VALUES (?, ?, ?, ?, ?)
        """, (row['year'], row['title'], row['studios'], row['producers'], winner))

    conn.commit()
    return conn
