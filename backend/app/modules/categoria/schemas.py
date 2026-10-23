from typing import Optional

from sqlmodel import Field, SQLModel

from app.tipos import CodigoStr


class CategoriaBase(SQLModel):
    codigo: CodigoStr = Field(schema_extra={"examples": ["MUE-01"]})
    descripcion: str = Field(min_length=3, schema_extra={"examples": ["Muebles de Oficina"]})
    activo: bool = True


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(SQLModel):
    codigo: Optional[CodigoStr] = None
    descripcion: Optional[str] = Field(default=None, min_length=3)
    activo: Optional[bool] = None


class CategoriaRead(CategoriaBase):
    id: int
