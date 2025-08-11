import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME", "language_game"),
    "user": os.getenv("DB_USER", "language_game"),
    "password": os.getenv("DB_PASSWORD", "secret"),
}

API_CONFIG = {
    "port": int(os.getenv("BACKEND_PORT", "5000")),
}

ASSET_CONFIG = {
    "image_url_prefix": os.getenv("IMAGE_URL_PREFIX"),
    "audio_url_prefix": os.getenv("AUDIO_URL_PREFIX"),
    "license_url_prefix": os.getenv("LICENSE_URL_PREFIX")
}