import type { Producto } from '../types/producto'

interface ProductoCardProps {
  producto: Producto
}

function ProductoCard({ producto }: ProductoCardProps) {
  const precioFormateado = producto.precio.toLocaleString('es-AR', {
    style: 'currency',
    currency: 'ARS',
  })

  return (
    <article className="flex flex-col justify-between rounded-lg border border-slate-200 bg-white p-5 shadow-sm">
      <div>
        <span className="text-xs font-medium uppercase tracking-wide text-slate-400">
          #{producto.id}
        </span>
        <h3 className="mt-1 text-lg font-semibold text-slate-800">{producto.nombre}</h3>
        <p className="mt-2 text-sm text-slate-600">{producto.descripcion}</p>
      </div>
      <p className="mt-4 text-xl font-bold text-indigo-600">{precioFormateado}</p>
    </article>
  )
}

export default ProductoCard
