from flask import Flask, jsonify
import psycopg
from config import DB_CONFIG, API_CONFIG

app = Flask(__name__)

@app.route("/assets")
def get_assets():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT asset_name, image_filename FROM image_assets;")
            rows = cur.fetchall()
            return jsonify([dict(zip(["asset_name", "image_filename"], row)) for row in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=API_CONFIG["port"])
