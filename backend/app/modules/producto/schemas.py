from typing import Annotated, Optional

from pydantic import StringConstraints
from sqlmodel import Field, SQLModel

from app.tipos import CodigoStr

# RN-02: el nombre no puede quedar vacío ni contener solo espacios.
NombreStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class ProductoBase(SQLModel):
    nombre: NombreStr = Field(schema_extra={"examples": ["Silla de Oficina"]})
    descripcion: str = Field(default="", schema_extra={"examples": ["Silla ergonómica"]})
    categoria: CodigoStr = Field(schema_extra={"examples": ["MUE-01"]})
    precio: float = Field(ge=0, schema_extra={"examples": [150.50]})  # RN-03: precio >= 0
    stock: int = Field(ge=0, schema_extra={"examples": [20]})
    stock_minimo: int = Field(ge=0, schema_extra={"examples": [5]})
    activo: bool = True


class ProductoCreate(ProductoBase):
    pass  # Exige todos los campos obligatorios de Base


class ProductoUpdate(SQLModel):
    # Opcional: Se usa si en el futuro se implementa PATCH (actualización parcial)
    nombre: Optional[NombreStr] = None
    descripcion: Optional[str] = None
    categoria: Optional[CodigoStr] = None
    precio: Optional[float] = Field(default=None, ge=0)
    stock: Optional[int] = Field(default=None, ge=0)
    stock_minimo: Optional[int] = Field(default=None, ge=0)
    activo: Optional[bool] = None


class ProductoRead(ProductoBase):
    id: int  # Contrato de salida: siempre incluye el ID generado


class ProductoStockResponse(SQLModel):
    stock: int
    bajo_stock_minimo: bool
    activo: bool
