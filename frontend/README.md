# TP Integrador Unidad 5 - Parte B: Pantalla de Productos

Pantalla de productos hecha con **React + TypeScript + Vite** y estilos con **Tailwind CSS**.
Es solo maquetado: no hay llamadas a la API ni estado, los productos están hardcodeados en `App.tsx`.

## Instalación y ejecución

```bash
pnpm install
pnpm dev
```

Abrir la URL que muestra Vite (por defecto http://localhost:5173).

Para verificar que compila sin errores de TypeScript:

```bash
pnpm build
```

## Estructura del proyecto

```
src/
├── types/
│   └── producto.ts        # interface Producto (id, nombre, descripcion, precio)
├── components/
│   ├── Navbar.tsx         # barra de navegación con el nombre de la app
│   ├── ProductoCard.tsx   # tarjeta con los datos de un producto
│   ├── ProductoList.tsx   # recibe Producto[] y renderiza varias tarjetas
│   ├── ProductoForm.tsx   # formulario de alta (sin funcionalidad)
│   └── Footer.tsx         # pie de página
├── App.tsx                # arma la pantalla con productos hardcodeados
├── main.tsx               # punto de entrada
└── index.css              # importa Tailwind CSS
```

## Decisiones

- **Componentes puros:** todos son funciones sin `useState`, `useEffect` ni ningún otro hook.
  Los datos bajan desde `App.tsx` mediante props.
- **Tipado:** cada componente declara una `interface` para sus props. No se usa `any`.
  La interface `Producto` refleja los campos del modelo del backend.
- **Tailwind CSS:** configurado con el plugin `@tailwindcss/vite` (guía oficial para Vite) y
  `@import "tailwindcss"` en `index.css`. Los estilos son clases utilitarias dentro del JSX.
- **Responsive:** el listado usa `grid` (1 columna en móvil, 2 en tablet, 3 en escritorio) y
  la pantalla pasa a dos columnas (listado + formulario) desde el ancho `lg`.
- **Paleta consistente:** `indigo` como color de acento y `slate` para fondos, bordes y textos.
