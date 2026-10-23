from typing import List, Optional

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.database import guardar
from .models import Proveedor
from .schemas import ProveedorCreate


def _validar_codigo_unico(
    session: Session, codigo: str, excluir_id: Optional[int] = None
) -> None:
    consulta = select(Proveedor).where(Proveedor.codigo == codigo)
    if excluir_id is not None:
        consulta = consulta.where(Proveedor.id != excluir_id)
    if session.exec(consulta).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe un proveedor con el código '{codigo}'",
        )


def crear(session: Session, data: ProveedorCreate) -> Proveedor:
    _validar_codigo_unico(session, data.codigo)
    return guardar(session, Proveedor.model_validate(data))


def obtener_todos(
    session: Session, skip: int, limit: int, activo: Optional[bool] = None
) -> List[Proveedor]:
    consulta = select(Proveedor)
    if activo is not None:
        consulta = consulta.where(Proveedor.activo == activo)
    consulta = consulta.order_by(Proveedor.id).offset(skip).limit(limit)
    return list(session.exec(consulta).all())


def obtener_por_id(session: Session, id: int) -> Optional[Proveedor]:
    return session.get(Proveedor, id)


def actualizar_total(
    session: Session, id: int, data: ProveedorCreate
) -> Optional[Proveedor]:
    proveedor = session.get(Proveedor, id)
    if not proveedor:
        return None
    _validar_codigo_unico(session, data.codigo, excluir_id=id)
    proveedor.sqlmodel_update(data.model_dump())
    return guardar(session, proveedor)


def desactivar(session: Session, id: int) -> Optional[Proveedor]:
    proveedor = session.get(Proveedor, id)
    if not proveedor:
        return None
    if not proveedor.activo:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El proveedor ya se encuentra desactivado",
        )
    proveedor.activo = False
    return guardar(session, proveedor)
