<template>
    <div class="containerFilho" :style="containerStyle">
      <div class="iconePerfil" :style="avatarStyle">
        {{ inicialUsuario }}
      </div>
  
      <div class="campoGrande">
        <label>Username</label>
        <input type="text" v-model="infosUsuario.username" />
      </div>
  
      <div class="campoMetade">
        <input type="text" placeholder="Nome" v-model="infosUsuario.first_name" />
        <input
          type="text"
          placeholder="Sobrenome"
          v-model="infosUsuario.last_name"
        />
      </div>
  
      <div class="dataNascimento">
        <label>Data de nascimento:</label>
        <div class="data">
          <select
            class="input"
            aria-label="Dia"
            v-model="diaNascimento"
            required
          >
            <option v-for="dia in 31" :key="dia" :value="dia">{{ dia }}</option>
          </select>
          <select
            class="input"
            aria-label="Mês"
            v-model="mesNascimento"
            required
          >
            <option
              v-for="(nomeMes, index) in meses"
              :key="index"
              :value="index < 9 ? '0' + (index + 1) : (index + 1)"
            >
              {{ nomeMes }}
            </option>
          </select>
          <select
            class="input"
            aria-label="Ano"
            v-model="anoNascimento"
            required
          >
            <option v-for="ano in 100" :key="ano" :value="2024 - ano">
              {{ 2024 - ano }}
            </option>
          </select>
        </div>
      </div>
  
      <div class="campoGrande">
        <label>Email</label>
        <input type="text" v-model="infosUsuario.email" />
      </div>
  
      <div class="campoMetade">
        <input type="password" placeholder="Nova senha" />
        <input type="password" placeholder="Repetir nova senha" />
      </div>
  
      <div class="btnSalvar">Salvar</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        meses: [
          'Jan', 'Fev', 'Mar', 'Abr',
          'Mai', 'Jun', 'Jul', 'Ago',
          'Set', 'Out', 'Nov', 'Dez',
        ],
        diaNascimento: null,
        mesNascimento: null,
        anoNascimento: null,
      };
    },
    computed: {
      infosUsuario() {
        return this.$store.getters.getInfosUsuario;
      },
      inicialUsuario() {
        const nome = this.$store.getters.getNomeUsuario || '';
        return nome.charAt(0).toUpperCase();
      },
      corAvatar() {
        return this.$store.getters.getCorAvatar;
      },
      avatarColorHex() {
        const map = {
          blue: '#0000FF',
          green: '#008000',
          red: '#FF0000',
          purple: '#800080',
          orange: '#FFA500',
        };
        return map[this.corAvatar] || this.corAvatar;
      },
      avatarStyle() {
        return {
          backgroundColor: this.avatarColorHex,
        };
      },
      containerStyle() {
        const c = this.avatarColorHex;
        return {
          border: `2px solid ${c}80`,
          boxShadow: `0 0 2px ${c}CC, 0 0 6px ${c}99, 0 0 12px ${c}66, 0 0 24px ${c}33`,
        };
      },
    },
    watch: {
      // Quando infosUsuario chegar da API, preenche selects
      'infosUsuario.dataNascimento': {
        immediate: true,
        handler(val) {
          if (!val) return;
          const [year, month, day] = val.split('-');
          this.diaNascimento = Number(day);
          this.mesNascimento = month; // mantém 01‑12 com zero à esquerda
          this.anoNascimento = year;
        },
      },
    },
    created() {
      this.$store.dispatch('getCliente');
    },
  };
  </script>
  
  <style scoped>
  /* (os estilos originais permanecem) */
  .containerFilho {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    width: 350px;
    margin: 50px auto;
    height: 500px;
    color: white;
    padding: 5px 0;
    background-color: rgb(7, 7, 7);
    border-radius: 8px;
  }
  
  .iconePerfil {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    height: 70px;
    width: 70px;
    border-radius: 50%;
  }
  
  .campoGrande {
    width: 85%;
    display: flex;
    flex-direction: column;
  }
  .campoGrande > label {
    margin-bottom: 5px;
  }
  .campoGrande > input {
    height: 30px;
    border-radius: 8px;
    border: none;
    padding-left: 8px;
  }
  
  .campoMetade {
    display: flex;
    width: 85%;
    gap: 20px;
  }
  .campoMetade > input {
    width: 50%;
    height: 30px;
    border-radius: 8px;
    border: none;
    padding-left: 8px;
  }
  
  .dataNascimento {
    display: flex;
    flex-direction: column;
    width: 85%;
  }
  .data {
    display: flex;
    justify-content: space-between;
  }
  .input {
    width: 32%;
    height: 30px;
    border-radius: 8px;
    border: none;
    padding-left: 8px;
  }
  
  .btnSalvar {
    text-align: center;
    background-color: rgb(0, 185, 9);
    color: white;
    padding: 10px;
    border-radius: 8px;
    width: 80%;
    transition: 0.2s;
    cursor: pointer;
  }
  .btnSalvar:hover {
    background-color: rgb(0, 165, 8);
  }
  </style>
  