from flask import Flask, jsonify, g
from database import initialize_database

app = Flask(__name__)  # Inicializa a aplicação Flask

def get_db_connection():
    # Verifica se já existe uma conexão no contexto do Flask
    if "db_connection" not in g:
        g.db_connection = initialize_database()  # Inicializa o banco de dados em memória
    return g.db_connection

@app.teardown_appcontext
def close_db_connection(exception):
    # Fecha a conexão com o banco ao encerrar a requisição
    db_connection = g.pop("db_connection", None)
    if db_connection is not None:
        db_connection.close()

# Endpoint para buscar filmes por ano
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

# Endpoint para listar apenas os filmes vencedores
@app.route("/api/movies/winners", methods=["GET"])
def get_winner_movies():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE winner = 1")  # Busca apenas os filmes vencedores
    rows = cursor.fetchall()
    if not rows:
        return jsonify({"error": "No winner movies found."}), 404
    movies = [
        {"id": row[0], "year": row[1], "title": row[2], "studios": row[3], "producers": row[4], "winner": bool(row[5])}
        for row in rows
    ]
    return jsonify(movies)

# Endpoint para buscar anos com múltiplos vencedores
@app.route("/api/movies/multiple-winners", methods=["GET"])
def get_multiple_winners():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT year, COUNT(*) as win_count 
        FROM movies 
        WHERE winner = 1 
        GROUP BY year 
        HAVING win_count > 1
    """)
    rows = cursor.fetchall()
    if not rows:
        return jsonify({"error": "No years with multiple winners found."}), 404
    result = [{"year": row[0], "win_count": row[1]} for row in rows]
    return jsonify(result)

# Endpoint para buscar os intervalos máximos e mínimos de prêmios
@app.route("/api/movies/intervals", methods=["GET"])
def get_intervals():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT producers, MAX(year) - MIN(year) AS interval, MIN(year) as first_year, MAX(year) as last_year 
        FROM movies 
        WHERE winner = 1 
        GROUP BY producers 
        HAVING COUNT(*) > 1
    """)
    rows = cursor.fetchall()
    if not rows:
        return jsonify({"error": "No intervals found for producers."}), 404
    intervals = [
        {"producer": row[0], "interval": row[1], "first_year": row[2], "last_year": row[3]} 
        for row in rows
    ]
    max_interval = max(intervals, key=lambda x: x["interval"])
    min_interval = min(intervals, key=lambda x: x["interval"])
    return jsonify({"maximum": max_interval, "minimum": min_interval})

# Tratamento de erro para rotas não encontradas
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Rota não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
