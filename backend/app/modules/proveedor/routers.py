from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List, Optional

from app.database import SessionDep
from . import schemas, services

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])


@router.post(
    "/", response_model=schemas.ProveedorRead, status_code=status.HTTP_201_CREATED
)
def alta_proveedor(proveedor: schemas.ProveedorCreate, session: SessionDep):
    return services.crear(session, proveedor)


@router.get(
    "/", response_model=List[schemas.ProveedorRead], status_code=status.HTTP_200_OK
)
def listar_proveedores(
    session: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    activo: Optional[bool] = Query(None, description="True=activos, False=inactivos"),
):
    return services.obtener_todos(session, skip, limit, activo)


@router.get(
    "/{id}", response_model=schemas.ProveedorRead, status_code=status.HTTP_200_OK
)
def detalle_proveedor(session: SessionDep, id: int = Path(..., gt=0)):
    proveedor = services.obtener_por_id(session, id)
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado"
        )
    return proveedor


@router.put(
    "/{id}", response_model=schemas.ProveedorRead, status_code=status.HTTP_200_OK
)
def actualizar_proveedor(
    proveedor: schemas.ProveedorCreate, session: SessionDep, id: int = Path(..., gt=0)
):
    actualizado = services.actualizar_total(session, id, proveedor)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado"
        )
    return actualizado


@router.put(
    "/{id}/desactivar",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_200_OK,
)
def borrado_logico(session: SessionDep, id: int = Path(..., gt=0)):
    desactivado = services.desactivar(session, id)
    if not desactivado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado"
        )
    return desactivado
