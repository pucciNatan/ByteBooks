<template>
  <form @submit.prevent="logarCliente">
    <div class="card">
      <h2>Fazer login</h2>

      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>

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
          :type="mostrarSenha ? 'text' : 'password'"
          placeholder="Senha"
          v-model="senha"
          required
        />
        <img :src="iconSenha" alt="Alternar senha" @click="toggleSenha" />
      </div>

      <button
        ref="loginBtn"
        class="login-button"
        type="submit"
        :disabled="loading"
        :style="btnWidth ? { width: btnWidth } : null"
      >
        <img
          v-if="loading"
          :src="loadGif"
          alt="Carregando"
          class="loading-img"
        />
        <span v-else>Entrar</span>
      </button>

      <div>
        Não tem uma conta?
        <router-link to="/cadastro" class="routerLink"
          >Cadastre-se</router-link
        >
      </div>
    </div>
  </form>
</template>

<script>
import olhoAberto from '../../imgs/olhoAberto.svg'
import olhoFechado from '../../imgs/olhoFechado.svg'
import loadGif from '../../imgs/loadGif.gif'

export default {
  data() {
    return {
      emailUsername: '',
      senha: '',
      errorMessage: '',
      mostrarSenha: false,
      loading: false,
      btnWidth: null,
      loadGif,
    }
  },
  computed: {
    iconSenha() {
      return this.mostrarSenha ? olhoFechado : olhoAberto
    },
  },
  methods: {
    toggleSenha() {
      this.mostrarSenha = !this.mostrarSenha
    },
    logarCliente() {
      this.errorMessage = ''
      this.loading = true
      this.btnWidth = this.$refs.loginBtn.offsetWidth + 'px'

      const dados = {
        emailUsername: this.emailUsername,
        password: this.senha,
      }
      this.$store
        .dispatch('logarUsuario', dados)
        .then(() => this.$router.push('/'))
        .catch((error) => {
          this.errorMessage = error.message
        })
        .finally(() => {
          this.loading = false
        })
    },
  },
}
</script>

<style scoped>
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
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.input-group img {
  position: absolute;
  right: 10px;
  top: 9px;
  width: 20px;
  margin-left: 20px;
}
.input-group img:hover {
  cursor: pointer;
}

.input-group input {
  padding-right: 46px;
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
  width: 100%;
  padding: 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
}
.login-button:hover {
  background-color: #1f1f1f;
}
.login-button:disabled {
  opacity: 0.8;
  cursor: default;
}

.loading-img {
  width: 20px;
  height: 20px;
  transform: scale(1.4);
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

  .input-group img {
    top: 12px;
  }
}
</style>
