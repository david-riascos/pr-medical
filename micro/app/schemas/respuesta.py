from typing import Optional

from pydantic import BaseModel, Field


class Respuesta(BaseModel):
    """Respuesta estandar: ESTADO > 0 es exito, ESTADO 0 se devuelve como HTTP 400."""

    RESPUESTA: str
    ESTADO: int
    BASEDEDATOS: Optional[str] = Field(default=None)
