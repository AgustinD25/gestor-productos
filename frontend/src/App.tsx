import Footer from './components/Footer'
import Navbar from './components/Navbar'
import ProductoForm from './components/ProductoForm'
import ProductoList from './components/ProductoList'
import type { Producto } from './types/producto'

// Datos hardcodeados: el TP pide solo maquetado, sin llamadas a la API.
const productos: Producto[] = [
  {
    id: 1,
    nombre: 'Silla Ergonómica',
    descripcion: 'Silla de oficina con respaldo lumbar y apoyabrazos regulables.',
    precio: 250000,
  },
  {
    id: 2,
    nombre: 'Escritorio Moderno',
    descripcion: 'Escritorio de madera de 140 cm con pasacables integrado.',
    precio: 420000.5,
  },
  {
    id: 3,
    nombre: 'Monitor 24 pulgadas',
    descripcion: 'Monitor Full HD con panel IPS y entrada HDMI.',
    precio: 310000,
  },
  {
    id: 4,
    nombre: 'Lámpara de Escritorio',
    descripcion: 'Lámpara LED con brazo articulado y tres niveles de luz.',
    precio: 38500.75,
  },
]

function App() {
  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar titulo="Gestor de Productos" />
      <main className="mx-auto grid max-w-6xl grid-cols-1 gap-8 px-4 py-8 sm:px-6 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <ProductoList productos={productos} />
        </div>
        <ProductoForm />
      </main>
      <Footer texto="TP Integrador Unidad 5 - Programación IV" />
    </div>
  )
}

export default App
