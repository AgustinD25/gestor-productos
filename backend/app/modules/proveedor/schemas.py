from typing import Annotated, Optional

from pydantic import StringConstraints
from sqlmodel import Field, SQLModel

from app.tipos import CodigoStr

CuitStr = Annotated[
    str, StringConstraints(min_length=11, max_length=15, pattern=r"^\d{2}-\d{8}-\d$")
]


class ProveedorBase(SQLModel):
    codigo: CodigoStr = Field(schema_extra={"examples": ["PRO-01"]})
    razon_social: str = Field(min_length=3, schema_extra={"examples": ["Proveedor de Muebles S.A."]})
    cuit: CuitStr = Field(schema_extra={"examples": ["30-12345678-9"]})
    email: str = Field(default="", description="Correo electrónico")
    telefono: str = Field(default="", description="Número de teléfono")
    activo: bool = True


class ProveedorCreate(ProveedorBase):
    pass


class ProveedorUpdate(SQLModel):
    codigo: Optional[CodigoStr] = None
    razon_social: Optional[str] = Field(default=None, min_length=3)
    cuit: Optional[CuitStr] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    activo: Optional[bool] = None


class ProveedorRead(ProveedorBase):
    id: int
