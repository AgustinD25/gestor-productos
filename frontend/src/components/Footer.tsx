interface FooterProps {
  texto: string
}

function Footer({ texto }: FooterProps) {
  return (
    <footer className="mt-12 border-t border-slate-200 bg-white">
      <p className="mx-auto max-w-6xl px-4 py-6 text-center text-sm text-slate-500 sm:px-6">
        {texto}
      </p>
    </footer>
  )
}

export default Footer
