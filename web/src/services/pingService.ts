import type { Respuesta } from '../types/respuesta'
import { api } from './api'

export async function ping(): Promise<Respuesta> {
  const { data } = await api.get<Respuesta>('ping')
  return data
}
