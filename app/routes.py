from flask import jsonify, g
from database import initialize_database

def get_db_connection():
    if "db_connection" not in g:
        g.db_connection = initialize_database()
    return g.db_connection

def close_db_connection(exception):
    db_connection = g.pop("db_connection", None)
    if db_connection is not None:
        db_connection.close()

def register_routes(app):
    @app.route("/api/movies/<int:year>", methods=["GET"])
    def get_movies_by_year(year):
        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM movies WHERE year = ?", (year,))
        rows = cursor.fetchall()
        if not rows:
            return jsonify({"error": "No movies found for the specified year."}), 404
        movies = [
            {"id": row[0], "year": row[1], "title": row[2], "studios": row[3], "producers": row[4], "winner": bool(row[5])}
            for row in rows
        ]
        return jsonify(movies)

    @app.route("/api/movies/winners", methods=["GET"])
    def get_winner_movies():
        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM movies WHERE winner = 1")
        rows = cursor.fetchall()
        if not rows:
            return jsonify({"error": "No winner movies found."}), 404
        movies = [
            {"id": row[0], "year": row[1], "title": row[2], "studios": row[3], "producers": row[4], "winner": bool(row[5])}
            for row in rows
        ]
        return jsonify(movies)

    @app.route("/api/movies/intervals", methods=["GET"])
    def get_intervals():
        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("""
            SELECT year, producers
            FROM movies
            WHERE winner = 1
        """)
        rows = cursor.fetchall()
        
        if not rows:
            return jsonify({"error": "No intervals found for producers."}), 404

        producer_intervals = {}
        for row in rows:
            year = row[0]
            producers = row[1].split(", ")
            for producer in producers:
                if producer not in producer_intervals:
                    producer_intervals[producer] = []
                producer_intervals[producer].append(year)
        
        intervals = []
        for producer, years in producer_intervals.items():
            if len(years) > 1:
                years.sort()
                first_year = years[0]
                last_year = years[-1]
                interval = last_year - first_year
                intervals.append({
                    "producer": producer,
                    "first_year": first_year,
                    "last_year": last_year,
                    "interval": interval
                })
        
        if not intervals:
            return jsonify({"error": "No producers with multiple wins found."}), 404
        
        max_interval = max(intervals, key=lambda x: x["interval"])
        min_interval = min(intervals, key=lambda x: x["interval"])

        return jsonify({"maximum": max_interval, "minimum": min_interval})
