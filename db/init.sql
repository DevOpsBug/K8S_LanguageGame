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
    url TEXT,
    license TEXT,
    download_date TEXT,
    attribution_text TEXT,
    attribution_html TEXT
);

-- Import only the CSV columns (Postgres will generate the id automatically)
COPY image_assets(asset_name, asset_category, english_word, german_word, italian_word, image_filename, file_type, image_width, image_height, source, url, license, download_date, attribution_text, attribution_html) FROM '/docker-entrypoint-initdb.d/data.csv' WITH CSV HEADER DELIMITER ';';
