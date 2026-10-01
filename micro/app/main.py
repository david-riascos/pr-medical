import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import ORIGEN_PERMITIDO
from app.routers import ping_router

logger = logging.getLogger("entrenamiento")

app = FastAPI(title="Entrenamiento FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ORIGEN_PERMITIDO],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ping_router.router, prefix="/api")


@app.exception_handler(Exception)
async def error_generico(_: Request, error: Exception) -> JSONResponse:
    # El detalle va al log; al cliente no se le exponen datos internos.
    logger.exception("Error no controlado", exc_info=error)
    return JSONResponse(
        status_code=400,
        content={"RESPUESTA": "Ocurrio un error al procesar la solicitud", "ESTADO": 0},
    )
