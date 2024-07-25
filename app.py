from flask import Flask, jsonify, render_template, request, redirect, url_for
import sqlite3
from threading import Thread
import os
import packet_sniffer  # Import the packet sniffer module

app = Flask(__name__)

# Ensure the database file is in the same directory as the script
db_path = os.path.join(os.path.dirname(__file__), 'packets.db')

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Route to fetch and display packet data
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM packets')
        rows = c.fetchall()
        conn.close()
        return render_template('index.html', packets=rows)
    except Exception as e:
        return str(e)

# Route to fetch packet data as JSON
@app.route('/api/packets')
def get_packets():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM packets')
        rows = c.fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])
    except Exception as e:
        return str(e)

# Route to start packet sniffing
@app.route('/start_sniffing', methods=['POST'])
def start_sniffing_route():
    count = int(request.form['count'])
    filter = request.form['filter']
    Thread(target=packet_sniffer.start_sniffing, args=(count, filter)).start()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5500)
