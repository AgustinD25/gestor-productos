# Gestor de Productos

API REST para gestionar un catálogo de **productos, categorías y proveedores**, con persistencia en
PostgreSQL, más una pantalla de productos maquetada en React.

Trabajo práctico integrador de Programación IV (Tecnicatura Universitaria en Programación a Distancia).

## Stack

| Parte | Tecnologías |
|-------|-------------|
| Backend | Python, FastAPI, SQLModel (SQLAlchemy + Pydantic), PostgreSQL, psycopg 3 |
| Frontend | React, TypeScript, Vite, Tailwind CSS, pnpm |

## Estructura

```
backend/    API FastAPI en capas (router → service → model, con schemas separados)
frontend/   Pantalla de productos con componentes funcionales puros
```

## Qué incluye

**Backend**
- CRUD de productos, categorías y proveedores contra PostgreSQL, con una sesión de base de datos por request.
- Modelos de tabla separados de los schemas de entrada/salida.
- Reglas de negocio en la capa de servicio: `404` si el id no existe, `409` por duplicados
  (nombre de producto, código de categoría y de proveedor), `422` por datos inválidos.
- Borrado lógico, paginación y filtro por estado.
- Documentación interactiva automática en `/docs` y archivos `.http` para probar cada endpoint.

**Frontend**
- Componentes tipados con TypeScript (`Navbar`, `ProductoCard`, `ProductoList`, `ProductoForm`, `Footer`).
- Diseño responsive con Tailwind CSS (grid y flex).
- Es solo maquetado: por ahora trabaja con datos de ejemplo y todavía no consume la API.

## Cómo ejecutarlo

Cada parte tiene su propio README con el detalle:

- [Backend](backend/Readme.md): requiere PostgreSQL y la variable de entorno `DATABASE_URL`.
- [Frontend](frontend/README.md): `pnpm install` y `pnpm dev`.
