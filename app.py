import sqlite3
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
DB_NAME = "electricity_board.db"


def init_db():
    """Initializes the SQLite database and structures the connections data matrix."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS connections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            consumer_name TEXT NOT NULL,
            connection_type TEXT NOT NULL,
            sanctioned_load REAL NOT NULL,
            status TEXT DEFAULT 'Active'
        )
    """
    )
    conn.commit()
    conn.close()


def get_db_connection():
    """Establishes database connections for runtime queries."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    """Renders the master console dashboard view."""
    return render_template("index.html")


# --- RESTful API Routing System ---


@app.route("/api/connections", methods=["GET"])
def get_connections():
    """READ: Extracts all consumer grid allocation logs."""
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM connections").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


@app.route("/api/connections", methods=["POST"])
def create_connection():
    """CREATE: Provisions a new electrical consumer line record."""
    data = request.get_json()
    name = data.get("consumer_name")
    conn_type = data.get("connection_type")
    load = data.get("sanctioned_load")

    if not name or not conn_type or not load:
        return jsonify({"error": "All grid registration fields required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO connections (consumer_name, connection_type, sanctioned_load) VALUES (?, ?, ?)",
        (name, conn_type, float(load)),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return (
        jsonify(
            {
                "id": new_id,
                "consumer_name": name,
                "connection_type": conn_type,
                "sanctioned_load": load,
                "status": "Active",
            }
        ),
        201,
    )


@app.route("/api/connections/<int:id>", methods=["PUT"])
def update_connection(id):
    """UPDATE: Toggles the power supply transmission grid connection status."""
    data = request.get_json()
    status = data.get("status")

    conn = get_db_connection()
    conn.execute(
        "UPDATE connections SET status = ? WHERE id = ?", (status, id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": f"Connection line {id} changed state status."})


@app.route("/api/connections/<int:id>", methods=["DELETE"])
def delete_connection(id):
    """DELETE: Terminates line allocation metrics and wipes record row."""
    conn = get_db_connection()
    conn.execute("DELETE FROM connections WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Line {id} unlinked successfully."})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)