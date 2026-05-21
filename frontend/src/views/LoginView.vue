<template>
  <main class="login-container">
    <section class="login-card">
      <h1>Omy Beauty Salon</h1>
      <p>Inicia sesión para gestionar tus citas</p>

      <form @submit.prevent="handleLogin">
        <label>Correo</label>
        <input 
          type="email" 
          v-model="email" 
          placeholder="admin@salon.com"
          required
        />

        <label>Contraseña</label>
        <input 
          type="password" 
          v-model="password" 
          placeholder="********"
          required
        />

        <button type="submit">Ingresar</button>
      </form>

      <p v-if="errorMessage" class="error">
        {{ errorMessage }}
      </p>
    </section>
  </main>
</template>

<script>
import { loginUser } from '../services/api'

export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    async handleLogin() {
      try {
        const result = await loginUser({
          email: this.email,
          password: this.password
        })

        localStorage.setItem('token', result.token)
        localStorage.setItem('user', JSON.stringify(result.user))

        this.$router.push('/dashboard')
      } catch (error) {
        this.errorMessage = error.message
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f8e8ef;
  font-family: Arial, sans-serif;
}

.login-card {
  width: 360px;
  background: white;
  padding: 32px;
  border-radius: 18px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

h1 {
  text-align: center;
  color: #b84c7d;
  margin-bottom: 8px;
}

p {
  text-align: center;
  color: #555;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 24px;
}

label {
  font-weight: bold;
  color: #444;
}

input {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 10px;
}

button {
  margin-top: 16px;
  padding: 12px;
  border: none;
  border-radius: 10px;
  background: #b84c7d;
  color: white;
  font-weight: bold;
  cursor: pointer;
}

button:hover {
  background: #9f3e6a;
}

.error {
  color: #c0392b;
  margin-top: 16px;
}
</style>