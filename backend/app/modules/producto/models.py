from typing import Optional

from sqlmodel import Field

from .schemas import ProductoBase


class Producto(ProductoBase, table=True):
    # table=True: esta clase se mapea a la tabla "producto" en PostgreSQL.
    # Hereda todos los campos de ProductoBase y agrega la clave primaria autogenerada.
    id: Optional[int] = Field(default=None, primary_key=True)
