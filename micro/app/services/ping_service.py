from app.core.database import obtener_conexion
from app.schemas.respuesta import Respuesta


def ping() -> Respuesta:
    """Responde pong y confirma que la base de datos contesta."""
    with obtener_conexion() as conexion:
        version = conexion.execute("SELECT sqlite_version()").fetchone()[0]
    return Respuesta(RESPUESTA="pong", ESTADO=1, BASEDEDATOS=f"SQLite {version}")
