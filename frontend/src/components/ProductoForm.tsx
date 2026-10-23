const inputClasses =
  'mt-1 w-full rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-800 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500'

// Solo maquetado: sin estado ni envío (el TP no pide funcionalidad).
function ProductoForm() {
  return (
    <section className="rounded-lg border border-slate-200 bg-white p-5 shadow-sm">
      <h2 className="mb-4 text-2xl font-semibold text-slate-800">Nuevo producto</h2>
      <form className="space-y-4">
        <div>
          <label htmlFor="nombre" className="block text-sm font-medium text-slate-700">
            Nombre
          </label>
          <input id="nombre" type="text" placeholder="Silla de oficina" className={inputClasses} />
        </div>
        <div>
          <label htmlFor="descripcion" className="block text-sm font-medium text-slate-700">
            Descripción
          </label>
          <textarea
            id="descripcion"
            rows={3}
            placeholder="Describí el producto"
            className={inputClasses}
          />
        </div>
        <div>
          <label htmlFor="precio" className="block text-sm font-medium text-slate-700">
            Precio
          </label>
          <input id="precio" type="number" min="0" step="0.01" placeholder="0.00" className={inputClasses} />
        </div>
        <button
          type="button"
          className="w-full rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white hover:bg-indigo-700"
        >
          Agregar producto
        </button>
      </form>
    </section>
  )
}

export default ProductoForm
