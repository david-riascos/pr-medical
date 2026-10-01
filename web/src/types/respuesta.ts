/** Respuesta estandar del backend: ESTADO > 0 es exito. */
export interface Respuesta {
  RESPUESTA: string
  ESTADO: number
  BASEDEDATOS?: string
}
