<template>
  <form @submit.prevent="cadastrarCliente">
    <div class="card">
      <h2>Criar uma conta</h2>

      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>

      <div class="input-group">
        <label>Username:</label>
        <input
          type="text"
          placeholder="Ex: exemploDaSilva123"
          v-model="username"
          required
          :class="{ 'error-input': errors.emailOrUsernameExists }"
        />
      </div>

      <div class="nomeSobrenome">
        <input type="text" placeholder="Nome" v-model="nome" required />
        <input type="text" placeholder="Sobrenome" v-model="sobrenome" required />
      </div>

      <div class="input-group">
        <label>Data de nascimento:</label>
        <div class="data-nascimento">
          <select class="select" aria-label="Dia" v-model="diaNascimento" required>
            <option v-for="dia in 31" :key="dia" :value="dia">{{ dia }}</option>
          </select>
          <select class="select" aria-label="Mês" v-model="mesNascimento" required>
            <option
              v-for="(nomeMes, index) in meses"
              :key="index"
              :value="index < 9 ? '0' + (index + 1) : index + 1"
            >
              {{ nomeMes }}
            </option>
          </select>
          <select class="select" aria-label="Ano" v-model="anoNascimento" required>
            <option v-for="ano in 100" :key="ano" :value="2024 - ano">
              {{ 2024 - ano }}
            </option>
          </select>
        </div>
      </div>

      <div class="input-group">
        <input
          type="email"
          placeholder="Email"
          v-model="email"
          required
          :class="{ 'error-input': errors.emailOrUsernameExists }"
        />
      </div>

      <div class="input-group">
        <input
          :type="mostrarSenha ? 'text' : 'password'"
          placeholder="Senha"
          v-model="senha"
          required
          :class="{ 'error-input': errors.passwordComplexity || errors.passwordMismatch }"
        />
        <img :src="iconSenha" alt="Alternar senha" @click="toggleSenha" />
      </div>

      <div class="input-group">
        <input
          :type="mostrarSenhaRep ? 'text' : 'password'"
          placeholder="Repetir senha"
          v-model="senhaRepetida"
          required
          :class="{ 'error-input': errors.passwordMismatch }"
        />
        <img :src="iconSenhaRep" alt="Alternar senha" @click="toggleSenhaRep" />
      </div>

      <button
        ref="registerBtn"
        class="register-button"
        type="submit"
        :disabled="loading"
        :style="btnWidth ? { width: btnWidth } : null"
      >
        <img v-if="loading" :src="loadGif" alt="Carregando" class="loading-img" />
        <span v-else>Cadastre-se</span>
      </button>

      <router-link to="/login" class="routerLink">Já tem uma conta?</router-link>
    </div>
  </form>
</template>


<script>
import axios from 'axios'
import olhoAberto from '../../imgs/olhoAberto.svg'
import olhoFechado from '../../imgs/olhoFechado.svg'
import loadGif from '../../imgs/loadGif.gif'

export default {
  data() {
    return {
      username: '',
      nome: '',
      sobrenome: '',
      diaNascimento: null,
      mesNascimento: null,
      anoNascimento: null,
      email: '',
      senha: '',
      senhaRepetida: '',
      mostrarSenha: false,
      mostrarSenhaRep: false,
      loading: false,
      btnWidth: null,
      errorMessage: '',
      errors: {
        passwordComplexity: false,
        passwordMismatch: false,
        emailOrUsernameExists: false,
      },
      meses: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
      loadGif,
    }
  },
  computed: {
    iconSenha() {
      return this.mostrarSenha ? olhoFechado : olhoAberto
    },
    iconSenhaRep() {
      return this.mostrarSenhaRep ? olhoFechado : olhoAberto
    },
  },
  methods: {
    toggleSenha() {
      this.mostrarSenha = !this.mostrarSenha
    },
    toggleSenhaRep() {
      this.mostrarSenhaRep = !this.mostrarSenhaRep
    },
    validarSenha() {
      const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$/
      return regex.test(this.senha)
    },
    limparErros() {
      this.errorMessage = ''
      this.errors.passwordComplexity = false
      this.errors.passwordMismatch = false
      this.errors.emailOrUsernameExists = false
    },
    async cadastrarCliente() {
      this.limparErros()

      if (!this.validarSenha()) {
        this.errors.passwordComplexity = true
        this.errorMessage =
          'A senha deve ter pelo menos 8 caracteres, incluindo um caractere especial, um número e uma letra maiúscula.'
        return
      }

      if (this.senha !== this.senhaRepetida) {
        this.errors.passwordMismatch = true
        this.errorMessage = 'As senhas digitadas são diferentes.'
        return
      }

      const dados = {
        username: this.username,
        first_name: this.nome,
        last_name: this.sobrenome,
        dataNascimento: `${this.diaNascimento}/${this.mesNascimento}/${this.anoNascimento}`,
        email: this.email,
        password: this.senha,
      }

      try {
        this.loading = true
        this.btnWidth = this.$refs.registerBtn.offsetWidth + 'px'

        const response = await axios.post(
          //'http://127.0.0.1:8000/api/clientes/registro/',
          'https://bytebooks-backend.fly.dev/api/clientes/registro/',
          dados,
          { headers: { 'Content-Type': 'application/json' } }
        )

        if (response.status === 201) {
          this.$router.push('/login')
        }
      } catch (error) {
        if (error.response && error.response.status === 400) {
          const msg = error.response.data.msg || ''
          if (msg.includes('Email ou Username já cadastrado')) {
            this.errors.emailOrUsernameExists = true
            this.errorMessage = 'Email ou Username já cadastrado.'
          } else {
            this.errorMessage = msg || 'Erro ao cadastrar. Verifique os campos.'
          }
        } else {
          this.errorMessage = error.message || 'Ocorreu um erro inesperado.'
        }
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px auto;
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

.nomeSobrenome,
.input-group {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.nomeSobrenome {
  flex-direction: row;
}

.data-nascimento {
  display: flex;
  gap: 10px;
  align-items: center;
}

.input-group {
  position: relative;
}

.input-group img {
  position: absolute;
  right: 10px;
  top: 9px;
  width: 20px;
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

.error-input {
  border-color: red !important;
}

.register-button {
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
.register-button:hover {
  background-color: #1f1f1f;
}
.register-button:disabled {
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
  margin-top: -10px;
}

.routerLink {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .card {
    margin-top: 60px;
    width: 70%;
  }
}
</style>
