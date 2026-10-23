from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import Session

from app.database import create_db_and_tables, engine
from app.modules.categoria import models as categoria_models  # noqa: F401  (registra la tabla)
from app.modules.categoria import services as categoria_services
from app.modules.producto import models as producto_models  # noqa: F401  (registra la tabla)
from app.modules.proveedor import models as proveedor_models  # noqa: F401  (registra la tabla)
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
from app.modules.proveedor.routers import router as proveedor_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Se ejecuta una vez al arrancar: crea las tablas que no existan en PostgreSQL
    # y carga las categorías iniciales si la tabla está vacía.
    create_db_and_tables()
    with Session(engine) as session:
        categoria_services.cargar_datos_iniciales(session)
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 1",
        description="Conceptos: Path, Query, Body, Pydantic, Errores.",
        version="1.0.0",
        lifespan=lifespan,
    )

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(proveedor_router)

    return app

app = create_app()
