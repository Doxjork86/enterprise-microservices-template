import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )

@app.route('/api/status')
def status():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"status": "OK", "service": "Backend Enterprise", "db": db_version[0]})
    except Exception as e:
        return jsonify({"status": "ERROR", "error": str(e)}), 500

@app.route('/health')
def health():
    return "OK", 200
