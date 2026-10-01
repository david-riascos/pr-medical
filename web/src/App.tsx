import { useState } from 'react'
import { ping } from './services/pingService'

type Resultado = { exito: boolean; mensaje: string }

function App() {
  const [resultado, setResultado] = useState<Resultado | null>(null)
  const [cargando, setCargando] = useState(false)

  const probarBackend = async () => {
    setCargando(true)
    try {
      const { RESPUESTA, ESTADO, BASEDEDATOS } = await ping()
      setResultado({ exito: ESTADO > 0, mensaje: `${RESPUESTA} (${BASEDEDATOS})` })
    } catch {
      // No se muestran detalles tecnicos al usuario.
      setResultado({ exito: false, mensaje: 'No se pudo conectar con el backend' })
    } finally {
      setCargando(false)
    }
  }

  return (
    <main className="contenedor">
      <h1>Entrenamiento: React + FastAPI</h1>
      <button onClick={probarBackend} disabled={cargando}>
        {cargando ? 'Probando...' : 'Probar backend'}
      </button>
      {resultado && (
        <p className={resultado.exito ? 'ok' : 'error'}>{resultado.mensaje}</p>
      )}
    </main>
  )
}

export default App
