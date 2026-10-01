import os

# Variables de entorno, con los mismos nombres que el backend Java.
DB_URL = os.getenv("DB_URL", ":memory:")
ORIGEN_PERMITIDO = os.getenv("ORIGEN_PERMITIDO", "http://localhost:3003")
