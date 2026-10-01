# pr-medical

Proyecto educativo de práctica: un sistema tipo **HIS** (Historia clínica / información hospitalaria) construido desde cero
en **React + FastAPI**, inspirado en los flujos reales de un sistema de salud (login, permisos, historia clínica...), pero
con **datos y escenarios totalmente ficticios**.

> Todo el contenido de este repositorio es ficticio y educativo. No contiene datos reales de pacientes, credenciales ni
> detalles internos de ningún sistema real.

## Estado actual

Por ahora el proyecto solo tiene el **esqueleto base**: un endpoint de prueba (`GET api/ping`) que confirma que el
frontend y el backend se comunican correctamente. Todavía no hay funcionalidad clínica.

**Siguiente paso:** login y permisos de usuarios (primer módulo real del sistema).

## Stack

| Carpeta | Rol | Tecnología | Puerto |
|---|---|---|---|
| [`micro/`](micro/) | Backend | Python 3.12 + FastAPI + Uvicorn + SQLite | `8083` |
| [`web/`](web/) | Frontend | React 18 + TypeScript + Vite | `3003` |

Cada carpeta tiene su propio `README.md` con el detalle de su stack, cómo correrla, su estructura interna y las trampas ya
resueltas. Este archivo es solo el índice general.

## Arquitectura (capas)

Backend y frontend siguen el mismo principio de capas, para que la lógica de negocio nunca quede mezclada con el
transporte HTTP ni con el acceso a datos:

```
router/controller → solo delega (recibe la petición, llama al service, devuelve la respuesta)
service           → la lógica de negocio vive aquí
core/repository    → única capa que toca la base de datos
```

Todas las respuestas del backend siguen un contrato común:

```json
{ "RESPUESTA": "...", "ESTADO": 1, "BASEDEDATOS": "..." }
```

- `ESTADO > 0` → éxito. `ESTADO = 0` → error (se responde con HTTP 400, sin exponer detalles internos del servidor).
- El frontend nunca muestra el detalle técnico de un error al usuario; cualquier excepción queda solo en el log del backend.

## Cómo correrlo

Backend (`micro/`):

```powershell
cd micro
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --port 8083
```

Frontend (`web/`), en otra terminal, con el backend ya encendido:

```powershell
cd web
yarn install
yarn dev
```

Luego abrir `http://localhost:3003` y pulsar **"Probar backend"**.

## Verificación

Antes de dar por terminada una funcionalidad, se verifica con clic real en un navegador (no solo peticiones HTTP) y,
cuando aplica, con pruebas automáticas del stack correspondiente (`pytest` en `micro`, `vitest`/Testing Library en `web`).

## Licencia

Proyecto personal de entrenamiento, sin licencia específica (todos los derechos reservados por defecto). Puedes añadir una
licencia abierta (MIT, por ejemplo) si en algún momento quieres que el código sea reutilizable por terceros.
