# micro — backend FastAPI (stack React + FastAPI)

Backend de práctica en **Python + FastAPI**, con la misma forma que los demás stacks: `router → service → core`, respuesta estándar
`{"RESPUESTA","ESTADO"}` y un único endpoint `GET /api/ping`. Su frontend es `../web` (React). Todo el contenido es ficticio y educativo.

## Stack

| Pieza | Detalle |
|---|---|
| Lenguaje | Python 3.12 (instalado con winget el 2026-09-25) |
| Framework | FastAPI 0.115.6 (con Pydantic 2, que llega como dependencia) |
| Servidor | Uvicorn 0.32.1 |
| Base de datos | `sqlite3` de la biblioteca estándar, **en memoria** (no añade dependencias) |
| Puerto | **8083** |

Dependencias exactas en `requirements.txt` (solo `fastapi` y `uvicorn`).

## Cómo correrlo

```powershell
cd micro
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --port 8083      # http://localhost:8083/api/ping
```

Se usa `python -m uvicorn` a propósito: los lanzadores del entorno virtual (`uvicorn.exe`, `pip.exe`) guardan la ruta absoluta y se rompen si
se mueve o renombra la carpeta; con `python -m` no. Si `python` no se ve, reabre la terminal.

FastAPI publica su documentación interactiva por defecto: `http://localhost:8083/docs` (comprobado: responde 200).

## Endpoint

| Método y ruta | Respuesta |
|---|---|
| `GET /api/ping` | `200` `{"RESPUESTA":"pong","ESTADO":1,"BASEDEDATOS":"SQLite 3.49.1"}` |
| Error no controlado | `400` `{"RESPUESTA":"Ocurrio un error al procesar la solicitud","ESTADO":0}` — el detalle va solo al log |
| Ruta inexistente | `404` `{"detail":"Not Found"}` — **usa el formato por defecto de FastAPI, no el contrato estándar** |

## Configuración (variables de entorno)

| Variable | Por defecto | Para qué |
|---|---|---|
| `DB_URL` | `:memory:` | Base SQLite (una ruta a archivo la vuelve persistente) |
| `ORIGEN_PERMITIDO` | `http://localhost:3003` | Único origen aceptado por CORS |

## Estructura (`app/`)

| Archivo | Capa | Responsabilidad |
|---|---|---|
| `main.py` | arranque | Crea la app, CORS, registra el router con prefijo `/api` y el manejador de errores |
| `routers/ping_router.py` | router | Solo delega |
| `services/ping_service.py` | service | Lógica: consulta la versión de SQLite |
| `core/database.py` | core | Único acceso a la BD (`obtener_conexion`) |
| `schemas/respuesta.py` | modelo | Contrato `Respuesta` (Pydantic; `BASEDEDATOS` se omite si es nulo) |
| `config.py` | configuración | Lee las variables de entorno |

## Estado de verificación (2026-09-25)

- `ping` y CORS comprobados con `curl` ✔ · clic real desde el frontend React en Chrome ✔ · `/docs` ✔.
- **No tiene pruebas automáticas todavía** (no hay `pytest`).

## Limitaciones conocidas

- El 404 de rutas inexistentes no sigue el contrato estándar (habría que registrar un manejador para `StarletteHTTPException`).
- `DB_URL` con `:memory:` abre una BD nueva por conexión: sirve para el `ping`, pero cuando haya tablas habrá que usar un archivo.
