from fastapi import APIRouter

from app.schemas.respuesta import Respuesta
from app.services import ping_service

router = APIRouter()


@router.get("/ping", response_model=Respuesta, response_model_exclude_none=True)
def ping() -> Respuesta:
    # El endpoint solo delega; la logica vive en el service.
    return ping_service.ping()
