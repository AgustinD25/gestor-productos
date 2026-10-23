from typing import List, Optional

from fastapi import HTTPException, status
from sqlmodel import Session, func, select

from app.database import guardar
from .models import Producto
from .schemas import ProductoCreate


def _validar_nombre_unico(
    session: Session, nombre: str, excluir_id: Optional[int] = None
) -> None:
    # Regla de negocio (HU-02): duplicado = mismo nombre, sin distinguir mayúsculas.
    # El schema ya recorta los espacios de los extremos.
    consulta = select(Producto).where(func.lower(Producto.nombre) == nombre.lower())
    if excluir_id is not None:
        consulta = consulta.where(Producto.id != excluir_id)
    if session.exec(consulta).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe un producto con el nombre '{nombre}'",
        )


def crear(session: Session, data: ProductoCreate) -> Producto:
    _validar_nombre_unico(session, data.nombre)
    # model_validate convierte el schema de entrada (Create) en el modelo de tabla.
    return guardar(session, Producto.model_validate(data))


def obtener_todos(session: Session, skip: int, limit: int) -> List[Producto]:
    consulta = select(Producto).order_by(Producto.id).offset(skip).limit(limit)
    return list(session.exec(consulta).all())


def obtener_por_id(session: Session, id: int) -> Optional[Producto]:
    return session.get(Producto, id)


def actualizar_total(
    session: Session, id: int, data: ProductoCreate
) -> Optional[Producto]:
    # Reemplazo total: Requiere todos los campos validables (ProductoCreate)
    producto = session.get(Producto, id)
    if not producto:
        return None
    _validar_nombre_unico(session, data.nombre, excluir_id=id)
    producto.sqlmodel_update(data.model_dump())
    return guardar(session, producto)


def desactivar(session: Session, id: int) -> Optional[Producto]:
    # Borrado lógico: Solo altera el estado 'activo'
    producto = session.get(Producto, id)
    if not producto:
        return None
    producto.activo = False
    return guardar(session, producto)


def obtener_estado_stock(session: Session, id: int) -> Optional[dict]:
    producto = session.get(Producto, id)
    if not producto:
        return None

    # La lógica de negocio vive aquí
    alerta_stock = producto.stock < producto.stock_minimo

    return {
        "stock": producto.stock,
        "bajo_stock_minimo": alerta_stock,
        "activo": producto.activo,
    }
