import type { Producto } from '../types/producto'
import ProductoCard from './ProductoCard'

interface ProductoListProps {
  productos: Producto[]
}

function ProductoList({ productos }: ProductoListProps) {
  return (
    <section>
      <h2 className="mb-4 text-2xl font-semibold text-slate-800">Productos</h2>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {productos.map((producto) => (
          <ProductoCard key={producto.id} producto={producto} />
        ))}
      </div>
    </section>
  )
}

export default ProductoList
