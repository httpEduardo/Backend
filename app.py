import sqlite3
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
DATABASE = "database.db"  

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            title TEXT,
            studios TEXT,
            producers TEXT,
            winner TEXT
        )
    ''')

    
    try:
        movies_df = pd.read_csv('Movielist.csv', sep=';')
        for _, row in movies_df.iterrows():
            cursor.execute('''
                INSERT INTO movies (year, title, studios, producers, winner)
                VALUES (?, ?, ?, ?, ?)
            ''', (row['year'], row['title'], row['studios'], row['producers'], row['winner']))
    except Exception as e:
        print(f"Erro ao carregar dados do CSV: {e}")

    conn.commit()
    conn.close()

def calculate_intervals():
    conn = sqlite3.connect(DATABASE)
    query = """
    SELECT producers, year
    FROM movies
    WHERE winner = 'yes'
    """
    data = pd.read_sql_query(query, conn)
    conn.close()

    producers_intervals = {}
    for _, row in data.iterrows():
        producers = [p.strip() for p in row['producers'].split(',')]
        year = row['year']
        for producer in producers:
            if producer not in producers_intervals:
                producers_intervals[producer] = []
            producers_intervals[producer].append(year)

    min_intervals, max_intervals = [], []
    for producer, years in producers_intervals.items():
        if len(years) > 1:
            years.sort()
            intervals = [years[i+1] - years[i] for i in range(len(years) - 1)]
            min_interval = min(intervals)
            max_interval = max(intervals)
            min_intervals.append({
                "producer": producer,
                "interval": min_interval,
                "previousWin": years[intervals.index(min_interval)],
                "followingWin": years[intervals.index(min_interval) + 1]
            })
            max_intervals.append({
                "producer": producer,
                "interval": max_interval,
                "previousWin": years[intervals.index(max_interval)],
                "followingWin": years[intervals.index(max_interval) + 1]
            })
    return {"min": min_intervals, "max": max_intervals}

@app.route('/producers/intervals', methods=['GET'])
def get_intervals():
    try:
        result = calculate_intervals()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()  
    app.run(debug=True)
