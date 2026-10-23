import os
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

# La URL de conexión se lee de la variable de entorno DATABASE_URL.
# Formato: postgresql+psycopg://usuario:password@host:puerto/base
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://user:password@localhost:5432/database_name",
)

# Una única instancia global para toda la aplicación.
# echo=True imprime en consola el SQL generado (útil para aprender y depurar).
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables() -> None:
    # Inspecciona los modelos con table=True ya importados y crea las tablas si no existen.
    SQLModel.metadata.create_all(engine)


def get_session():
    # Una sesión (transacción) por request; se cierra sola al terminar.
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def guardar(session: Session, obj: SQLModel) -> SQLModel:
    # add() registra el objeto, commit() ejecuta la transacción y refresh() recarga
    # el objeto desde la BD (así obtenemos el id generado). Si algo falla, rollback().
    try:
        session.add(obj)
        session.commit()
    except Exception:
        session.rollback()
        raise
    session.refresh(obj)
    return obj
