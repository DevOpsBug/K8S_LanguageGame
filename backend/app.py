from flask import Flask, jsonify, request
import psycopg
from config import DB_CONFIG, API_CONFIG, ASSET_CONFIG
import random

app = Flask(__name__)

@app.route("/assets/all", methods=["GET"])
def get_assets():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT asset_name, asset_category, image_filename FROM image_assets;")
            rows = cur.fetchall()
            return jsonify([dict(zip(["asset_name", "image_url"], [row[0], f"{ASSET_CONFIG['image_url_prefix']}{row[1]}/{row[2]}" ])) for row in rows])

@app.route("/assets/asset_category/<asset_category>", methods=["GET"])
def get_assets_by_category(asset_category):
    print(f"Fetching assets for category: {asset_category}")
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT asset_name, asset_category, image_filename FROM image_assets WHERE asset_category = '{asset_category}';")
            rows = cur.fetchall()
            print(f"Got {len(rows)} items for category '{asset_category}'")
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
        
@app.route("/language-game", methods=["GET"])
def get_language_game():
    language = request.args.get("language")
    category = request.args.get("category")
    if not language or not category:
        return jsonify({"error": "Missing 'language' or 'category' parameter"}), 400

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
    SELECT asset_name, asset_category, {language}_word, image_filename, file_type, 
        image_width, image_height, {language}_audio_filename 
    FROM image_assets 
    WHERE asset_category = '{category}';
    """)
            rows = list(cur.fetchall())
            print(f"Fetched {len(rows)} rows for category '{category}'")
            random.shuffle(rows)
            random_rows = rows[:4]
            random_rows_json = list()
            for row in random_rows:
                (asset_name, asset_category, word, image_filename, file_type, 
        image_width, image_height, audio_filename) = row
                row_json = {
                    "asset_name": asset_name, 
                    "asset_category": asset_category, 
                    "word": word, 
                    "image_filename": f"{ASSET_CONFIG['image_url_prefix']}{asset_category}/{image_filename}",
                    "file_type": file_type, 
                    "image_width": image_width, 
                    "image_height": image_height, 
                    "audio_filename": f"{ASSET_CONFIG['audio_url_prefix']}{asset_category}/{audio_filename}"
                }
                random_rows_json.append(row_json)
            correct_element = random_rows_json[0]
            wrong_elements = random_rows_json[1:]
            return jsonify(
                {
                    "category": category,
                    "correctImage": correct_element['image_filename'],
                    "incorrectImages": [x['image_filename'] for x in wrong_elements],
                    "word": correct_element['word'],
                    "audioUrl": correct_element['audio_filename']
                }
                )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=API_CONFIG["port"])
