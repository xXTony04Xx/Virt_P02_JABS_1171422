<template>
  <main class="users-container">
    <header>
      <h1>Gestión de usuarios</h1>
      <button @click="$router.push('/dashboard')">Volver</button>
    </header>

    <section class="form-section">
      <h2>Crear usuario</h2>

      <form @submit.prevent="handleCreateUser">
        <input v-model="form.name" type="text" placeholder="Nombre" required />
        <input v-model="form.email" type="email" placeholder="Correo" required />
        <input v-model="form.password" type="password" placeholder="Contraseña" required />

        <select v-model="form.role" required>
          <option value="user">Usuario</option>
          <option value="admin">Administrador</option>
        </select>

        <button type="submit">Crear usuario</button>
      </form>

      <p v-if="message">{{ message }}</p>
    </section>

    <section class="users-list">
      <h2>Usuarios registrados</h2>

      <div class="user-card" v-for="user in users" :key="user._id">
        <h3>{{ user.name }}</h3>
        <p><strong>Correo:</strong> {{ user.email }}</p>
        <p><strong>Rol:</strong> {{ user.role }}</p>
      </div>
    </section>
  </main>
</template>

<script>
import { getUsers, createUser } from '../services/api'

export default {
  name: 'UsersView',
  data() {
    return {
      users: [],
      message: '',
      form: {
        name: '',
        email: '',
        password: '',
        role: 'user'
      }
    }
  },
  methods: {
    async loadUsers() {
      this.users = await getUsers()
    },
    async handleCreateUser() {
      const result = await createUser(this.form)

      this.message = result.message || 'Usuario creado'

      this.form = {
        name: '',
        email: '',
        password: '',
        role: 'user'
      }

      await this.loadUsers()
    }
  },
  async mounted() {
    await this.loadUsers()
  }
}
</script>

<style scoped>
.users-container {
  min-height: 100vh;
  padding: 32px;
  background: #fff6fa;
  font-family: Arial, sans-serif;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.form-section,
.users-list {
  margin-top: 32px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 400px;
}

input,
select,
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

.user-card {
  background: white;
  padding: 20px;
  border-radius: 18px;
  margin-top: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
</style>