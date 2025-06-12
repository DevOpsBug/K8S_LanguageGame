CREATE TABLE IF NOT EXISTS image_assets (
    id SERIAL PRIMARY KEY,
    asset_name TEXT,
    asset_category TEXT, 
    english_word TEXT, 
    german_word TEXT, 
    italian_word TEXT, 
    image_filename TEXT, 
    file_type TEXT, 
    image_width TEXT, 
    image_height TEXT, 
    source TEXT, 
    download_url TEXT, 
    download_date TEXT, 
    license TEXT, 
    license_version_date TEXT, 
    license_pdf_url TEXT, 
    attribution_text TEXT, 
    attribution_html TEXT, 
    english_audio_filename TEXT, 
    german_audio_filename TEXT, 
    italian_audio_filename TEXT
);

-- Import only the CSV columns (Postgres will generate the id automatically)
COPY image_assets(asset_name, asset_category, english_word, german_word, italian_word, image_filename, file_type, image_width, image_height, source, download_url, download_date, license, license_version_date, license_pdf_url, attribution_text, attribution_html, english_audio_filename, german_audio_filename, italian_audio_filename) FROM '/docker-entrypoint-initdb.d/data.csv' WITH CSV HEADER DELIMITER ';';
