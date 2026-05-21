<template>
  <main class="dashboard">
    <header class="header">
      <div>
        <h1>Omy Beauty Salon</h1>
        <p>Bienvenido/a, {{ user?.name || 'Usuario' }}</p>
      </div>

      <button @click="logout">Cerrar sesión</button>
    </header>

    <section class="services">
      <h2>Servicios disponibles</h2>

      <div class="service-grid">
        <div class="service-card" v-for="service in services" :key="service.name">
          <h3>{{ service.name }}</h3>
          <p>{{ service.description }}</p>
        </div>
      </div>
    </section>

    <section class="actions">
      <button @click="$router.push('/appointments')">
        Ver / agendar citas
      </button>

      <button 
        v-if="user?.role === 'admin'"
        @click="$router.push('/users')"
      >
        Crear usuarios
      </button>
    </section>
  </main>
</template>

<script>
export default {
  name: 'DashboardView',
  data() {
    return {
      user: null,
      services: [
        {
          name: 'Manicure',
          description: 'Cuidado y diseño básico de uñas.'
        },
        {
          name: 'Pedicure',
          description: 'Tratamiento y cuidado para pies.'
        },
        {
          name: 'Uñas acrílicas',
          description: 'Aplicación y diseño personalizado.'
        },
        {
          name: 'Diseño de uñas',
          description: 'Decoración, colores y estilos especiales.'
        }
      ]
    }
  },
  mounted() {
    const storedUser = localStorage.getItem('user')

    if (!storedUser) {
      this.$router.push('/')
      return
    }

    this.user = JSON.parse(storedUser)
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  padding: 32px;
  background: #fff6fa;
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #b84c7d;
  color: white;
  padding: 24px;
  border-radius: 18px;
}

.header h1 {
  margin: 0;
}

.header p {
  margin: 6px 0 0;
}

button {
  border: none;
  padding: 12px 18px;
  border-radius: 10px;
  cursor: pointer;
  font-weight: bold;
}

.header button {
  background: white;
  color: #b84c7d;
}

.services {
  margin-top: 32px;
}

.services h2 {
  color: #333;
}

.service-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin-top: 16px;
}

.service-card {
  background: white;
  padding: 24px;
  border-radius: 18px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

.service-card h3 {
  color: #b84c7d;
  margin-top: 0;
}

.service-card p {
  color: #555;
}

.actions {
  margin-top: 32px;
  display: flex;
  gap: 16px;
}

.actions button {
  background: #b84c7d;
  color: white;
}

.actions button:hover {
  background: #9f3e6a;
}
</style>