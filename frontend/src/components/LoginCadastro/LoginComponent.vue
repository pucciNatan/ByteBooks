<template>
  <form @submit.prevent="logarCliente">
    <div class="card">
      <h2>Fazer login</h2>

      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>

      <div class="input-group">
        <label>Email ou Username</label>
        <input
          type="text"
          placeholder="Ex: exemploDaSilva123"
          v-model="emailUsername"
          required
        />
      </div>

      <div class="input-group">
        <input
          type="password"
          placeholder="Senha"
          v-model="senha"
          required
        />
      </div>

      <input class="login-button" type="submit" value="Entrar" />
      <div>
        Não tem uma conta?
        <router-link to="/cadastro" class="routerLink">Cadastre-se</router-link>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  data() {
    return {
      emailUsername: '',
      senha: '',
      errorMessage: ''
    }
  },
  methods: {
    logarCliente() {
      this.errorMessage = ''

      const dados = {
        emailUsername: this.emailUsername,
        password: this.senha
      }

      this.$store
        .dispatch('logarUsuario', dados)
        .then(() => {
          this.$router.push('/')
        })
        .catch(error => {
          this.errorMessage = error.message
        })
    }
  }
}
</script>

<style scoped>
/* ===== DESKTOP / BASE ===== */
.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 70px auto;
  width: 350px;
  font-family: 'Montserrat', sans-serif;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  gap: 20px;
}

h2 {
  color: #111;
  font-size: 28px;
}

.input-group {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input,
.select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
  width: 100%;
  box-sizing: border-box;
}

.login-button {
  background-color: #0f0f0f;
  color: #fff;
  border: none;
  padding: 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}
.login-button:hover {
  background-color: #1f1f1f;
}

a {
  text-decoration: none;
  color: rgb(0, 65, 139);
}

.error-message {
  color: red;
  font-size: 14px;
  text-align: center;
}

.routerLink {
  text-decoration: underline;
}

/* ===== MOBILE ===== */
@media (max-width: 480px) {
  .card {
    width: 70%;
    padding: 16px;
    gap: 16px;
  }

  h2 {
    font-size: 22px;
  }

  input,
  .select {
    padding: 12px;
    font-size: 16px;
  }

  .login-button {
    padding: 14px;
    font-size: 18px;
  }
}
</style>
