<template>

  <main class="appointments-container">

    <header>
      <h1>Gestión de citas</h1>

      <button @click="$router.push('/dashboard')">
        Volver
      </button>
    </header>

    <section class="form-section">

      <h2>Agendar cita</h2>

      <form @submit.prevent="handleCreateAppointment">

        <input
          v-model="form.clienteName"
          type="text"
          placeholder="Nombre cliente"
          required
        />

        <input
          v-model="form.manicuristsName"
          type="text"
          placeholder="Manicurista"
          required
        />

        <input
          v-model="form.service"
          type="text"
          placeholder="Servicio"
          required
        />

        <input
          v-model="form.date"
          type="date"
          required
        />

        <input
          v-model="form.time"
          type="time"
          required
        />

        <button type="submit">
          Crear cita
        </button>

      </form>

    </section>

    <section class="appointments-list">

      <h2>Citas</h2>

      <div
        class="appointment-card"
        v-for="appointment in appointments"
        :key="appointment._id"
      >

        <h3>{{ appointment.clienteName }}</h3>

        <p><strong>Servicio:</strong> {{ appointment.service }}</p>

        <p><strong>Fecha:</strong> {{ appointment.date }}</p>

        <p><strong>Hora:</strong> {{ appointment.time }}</p>

        <p><strong>Estado:</strong> {{ appointment.status }}</p>

        <button @click="handleDeleteAppointment(appointment._id)">
          Eliminar
        </button>

      </div>

    </section>

  </main>

</template>

<script>

import {
  getAppointments,
  createAppointment,
  deleteAppointment
} from '../services/api'

export default {

  name: 'AppointmentsView',

  data() {
    return {

      appointments: [],

      form: {
        clienteName: '',
        manicuristsName: '',
        service: '',
        date: '',
        time: '',
        status: 'Agendada'
      }
    }
  },

  methods: {

    async loadAppointments() {

    try {

      const data = await getAppointments()

      console.log(data)

      this.appointments = data

      } catch (error) {

        console.error(error)
      } 
    },

    async handleCreateAppointment() {

      await createAppointment(this.form)

      this.form = {
        clienteName: '',
        manicuristsName: '',
        service: '',
        date: '',
        time: '',
        status: 'Agendada'
      }

      await this.loadAppointments()
    },

    async handleDeleteAppointment(id) {

      await deleteAppointment(id)

      await this.loadAppointments()
    }
  },

  async mounted() {

    await this.loadAppointments()
  }
}

</script>

<style scoped>

.appointments-container {
  padding: 32px;
  font-family: Arial, sans-serif;
  background: #fff6fa;
  min-height: 100vh;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.form-section,
.appointments-list {
  margin-top: 32px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 400px;
}

input,
button {
  padding: 12px;
  border-radius: 10px;
  border: 1px solid #ccc;
}

button {
  background: #b84c7d;
  color: white;
  border: none;
  cursor: pointer;
}

.appointment-card {
  background: white;
  padding: 20px;
  border-radius: 18px;
  margin-top: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

</style>