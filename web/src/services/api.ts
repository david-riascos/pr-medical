import axios from 'axios'

/** Unico lugar donde se configura la URL del backend. */
export const api = axios.create({
  baseURL: import.meta.env.VITE_URL_API,
})
