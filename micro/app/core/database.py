import sqlite3

from app.config import DB_URL


def obtener_conexion() -> sqlite3.Connection:
    """Abre una conexion a la base de datos (equivalente a DBPool del backend Java)."""
    return sqlite3.connect(DB_URL)
