const API_URL = 'http://35.232.39.106'

export async function loginUser(credentials) {

  const response = await fetch(`${API_URL}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })

  const data = await response.json()

  if (!response.ok) {
    throw new Error(data.message || 'Error al iniciar sesión')
  }

  return data
}

export async function getAppointments() {

  const token = localStorage.getItem('token')

  const response = await fetch(`${API_URL}/appointments`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  })

  return await response.json()
}

export async function createAppointment(appointmentData) {

  const token = localStorage.getItem('token')

  const response = await fetch(`${API_URL}/appointments`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(appointmentData)
  })

  return await response.json()
}

export async function deleteAppointment(id) {

  const token = localStorage.getItem('token')

  const response = await fetch(`${API_URL}/appointments/${id}`, {
    method: 'DELETE',
    headers: {
      Authorization: `Bearer ${token}`
    }
  })

  return await response.json()
}

export async function getUsers() {
  const token = localStorage.getItem('token')

  const response = await fetch(`${API_URL}/users`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  })

  return await response.json()
}

export async function createUser(userData) {
  const token = localStorage.getItem('token')

  const response = await fetch(`${API_URL}/users`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(userData)
  })

  return await response.json()
}