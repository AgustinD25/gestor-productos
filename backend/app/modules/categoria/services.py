from typing import List, Optional

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.database import guardar
from .models import Categoria
from .schemas import CategoriaCreate


def cargar_datos_iniciales(session: Session) -> None:
    # Registros que antes vivían en la lista en memoria; solo se cargan si la tabla está vacía.
    if session.exec(select(Categoria)).first():
        return
    session.add_all(
        [
            Categoria(codigo="MUE-01", descripcion="Muebles de Oficina", activo=True),
            Categoria(codigo="ELE-02", descripcion="Electrónica", activo=True),
        ]
    )
    session.commit()


def _validar_codigo_unico(
    session: Session, codigo: str, excluir_id: Optional[int] = None
) -> None:
    consulta = select(Categoria).where(Categoria.codigo == codigo)
    if excluir_id is not None:
        consulta = consulta.where(Categoria.id != excluir_id)
    if session.exec(consulta).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe una categoría con el código '{codigo}'",
        )


def crear(session: Session, data: CategoriaCreate) -> Categoria:
    _validar_codigo_unico(session, data.codigo)
    return guardar(session, Categoria.model_validate(data))


def obtener_todas(session: Session, skip: int = 0, limit: int = 10) -> List[Categoria]:
    consulta = select(Categoria).order_by(Categoria.id).offset(skip).limit(limit)
    return list(session.exec(consulta).all())


def obtener_por_id(session: Session, id: int) -> Optional[Categoria]:
    return session.get(Categoria, id)


def actualizar_total(
    session: Session, id: int, data: CategoriaCreate
) -> Optional[Categoria]:
    categoria = session.get(Categoria, id)
    if not categoria:
        return None
    _validar_codigo_unico(session, data.codigo, excluir_id=id)
    categoria.sqlmodel_update(data.model_dump())
    return guardar(session, categoria)


def desactivar(session: Session, id: int) -> Optional[Categoria]:
    categoria = session.get(Categoria, id)
    if not categoria:
        return None
    categoria.activo = False
    return guardar(session, categoria)
