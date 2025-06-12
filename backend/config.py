import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME", "language_game"),
    "user": os.getenv("DB_USER", "language_game"),
    "password": os.getenv("DB_PASSWORD", "secret"),
}

API_CONFIG = {
    "port": int(os.getenv("API_PORT", "5000")),
}

ASSEST_CONFIG = {
    "image_url_prefix": "https://devopsbug.com/media/projects/openlingua/images/",
    "audio_url_prefix": "https://devopsbug.com/media/projects/openlingua/audio/",
}