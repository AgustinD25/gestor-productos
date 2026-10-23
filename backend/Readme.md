# TP Integrador Unidad 5 - Gestor de Productos (FastAPI + SQLModel + PostgreSQL)

API REST de gestión de catálogo (Categorías, Productos y Proveedores) con persistencia en
PostgreSQL mediante SQLModel. Migración del TP 4, que guardaba los datos en memoria.

## Requisitos

- Python 3.10 o superior
- PostgreSQL instalado y en ejecución (puerto 5432 por defecto)

## Base de datos

Crear una base vacía (por ejemplo desde pgAdmin: *Databases → Create → Database*):

```
gestor_productos
```

Las tablas (`producto`, `categoria`, `proveedor`) se crean solas al iniciar la aplicación.
Además se cargan dos categorías iniciales (`MUE-01` y `ELE-02`) si la tabla está vacía.

## Variable de entorno `DATABASE_URL`

La conexión se lee de la variable de entorno `DATABASE_URL`, para no dejar credenciales en el código.

Formato:

```
postgresql+psycopg://USUARIO:PASSWORD@HOST:PUERTO/BASE
```

Ejemplo (reemplazar `TU_PASSWORD` por la contraseña del usuario `postgres`):

```powershell
# PowerShell (Windows)
$env:DATABASE_URL = "postgresql+psycopg://postgres:TU_PASSWORD@localhost:5432/gestor_productos"
```

```bash
# Linux / macOS
export DATABASE_URL="postgresql+psycopg://postgres:TU_PASSWORD@localhost:5432/gestor_productos"
```

La variable vale solo para la terminal donde se define. Si la contraseña tiene caracteres
especiales (`@`, `:`, `/`, `#`, `%`), hay que codificarlos en la URL (por ejemplo `@` → `%40`).

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` incluye `fastapi`, `uvicorn`, `sqlmodel` y `psycopg[binary]` (driver de PostgreSQL).

## Ejecución

Con `DATABASE_URL` definida en la misma terminal:

```bash
fastapi dev app/main.py
```

o, equivalente:

```bash
uvicorn app.main:app --reload
```

Documentación interactiva: http://localhost:8000/docs (Swagger UI) y http://localhost:8000/redoc

## Estructura del proyecto

```
app/
├── main.py            # Crea la app, registra routers y crea las tablas (lifespan)
├── database.py        # Engine, sesión por request (SessionDep) y helper guardar()
├── tipos.py           # Tipos compartidos (CodigoStr: formato AAA-00)
└── modules/
    ├── producto/      # schemas.py (validación) · models.py (tabla) · services.py (negocio) · routers.py (HTTP)
    ├── categoria/
    └── proveedor/
tests/                 # Archivos .http para REST Client (VS Code)
```

Arquitectura en capas: **Router** (HTTP) → **Service** (reglas de negocio) → **Model** (tabla) con
**Schemas** de entrada/salida separados del modelo de tabla.

## Endpoints

Los tres módulos exponen el mismo CRUD:

| Método | Endpoint | Código | Descripción |
|--------|----------|--------|-------------|
| POST | /{recurso}/ | 201 | Crear |
| GET | /{recurso}/ | 200 | Listar (`skip`, `limit`; proveedores también `activo`) |
| GET | /{recurso}/{id} | 200 | Detalle |
| PUT | /{recurso}/{id} | 200 | Reemplazo total |
| PUT | /{recurso}/{id}/desactivar | 200 | Borrado lógico |

`{recurso}` puede ser `productos`, `categorias` o `proveedores`. Productos suma
`GET /productos/{id}/stock` (alerta de stock bajo el mínimo).

## Validaciones y reglas de negocio

- **422** (schemas Pydantic): nombre de producto no vacío ni solo espacios, precio >= 0, stock >= 0,
  códigos con formato `AAA-00`, razón social/descripción de al menos 3 caracteres, CUIT `NN-NNNNNNNN-N`.
- **404**: el `id` no existe en la base de datos.
- **409** (reglas en el service): producto con nombre duplicado (sin distinguir mayúsculas),
  categoría o proveedor con código duplicado, proveedor ya desactivado.

## Pruebas

Archivos `.http` en `tests/` (extensión REST Client de VS Code): `test_productos.http`,
`test_categorias.http` y `test_proveedores.http`. Cada uno demuestra todo el CRUD y los escenarios
de error. Se ejecutan en orden con el servidor corriendo; los códigos y nombres se generan para que
puedan repetirse aunque los datos persistan entre corridas.
