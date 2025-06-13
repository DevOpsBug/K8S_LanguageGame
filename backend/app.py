from flask import Flask, jsonify
import psycopg
from config import DB_CONFIG, API_CONFIG, ASSET_CONFIG
app = Flask(__name__)

@app.route("/assets/all", methods=["GET"])
def get_assets():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT asset_name, asset_category, image_filename FROM image_assets;")
            rows = cur.fetchall()
            return jsonify([dict(zip(["asset_name", "image_url"], [row[0], f"{ASSET_CONFIG['image_url_prefix']}{row[1]}/{row[2]}" ])) for row in rows])

@app.route("/assets/attribution", methods=["GET"])
def get_attribution():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT asset_name, asset_category, image_filename, source, download_url, download_date, license, license_version_date, license_pdf_url, attribution_text, attribution_html FROM image_assets WHERE attribution_html IS NOT NULL;")
            rows = cur.fetchall()
            return_list = []
            for row in rows:
                asset_name, asset_category, image_filename, source, download_url, download_date, license, license_version_date, license_pdf_url, attribution_text, attribution_html = row
                return_list.append(
                    {
                        "asset_name": asset_name,
                        "asset_category": asset_category,
                        "image_filename": image_filename,
                        "image_url": f"{ASSET_CONFIG['image_url_prefix']}{asset_category}/{image_filename}",
                        "source": source, 
                        "download_url": download_url, 
                        "download_date": download_date, 
                        "license": license, 
                        "license_version_date": license_version_date, 
                        "license_pdf_url": f"{ASSET_CONFIG['license_url_prefix']}{license_pdf_url}", 
                        "attribution_text": attribution_text, 
                        "attribution_html": attribution_html
                    })
                
            return jsonify(return_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=API_CONFIG["port"])
