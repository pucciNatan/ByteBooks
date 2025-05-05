<template>
  <div class="pai">
    <!-- Mensagens -->
    <div v-if="mensagem" :class="['alerta', tipoMensagem]">
      {{ mensagem }}
    </div>

    <div class="containerFilho" :style="containerStyle">
      <!-- Avatar -->
      <div class="iconePerfil" :style="avatarStyle">
        {{ inicialUsuario }}
      </div>

      <!-- Username -->
      <div class="campoGrande">
        <label>Username</label>
        <input type="text" v-model="infosUsuario.username" />
      </div>

      <!-- Nome / Sobrenome -->
      <div class="campoMetade">
        <input
          type="text"
          placeholder="Nome"
          v-model="infosUsuario.first_name"
        />
        <input
          type="text"
          placeholder="Sobrenome"
          v-model="infosUsuario.last_name"
        />
      </div>

      <!-- Data de nascimento -->
      <div class="dataNascimento">
        <label>Data de nascimento:</label>
        <div class="data">
          <select class="input" v-model="diaNascimento" required>
            <option v-for="d in 31" :key="d" :value="d">{{ d }}</option>
          </select>
          <select class="input" v-model="mesNascimento" required>
            <option
              v-for="(m, idx) in meses"
              :key="idx"
              :value="idx < 9 ? '0' + (idx + 1) : idx + 1"
            >
              {{ m }}
            </option>
          </select>
          <select class="input" v-model="anoNascimento" required>
            <option v-for="a in 100" :key="a" :value="2024 - a">
              {{ 2024 - a }}
            </option>
          </select>
        </div>
      </div>

      <!-- Email -->
      <div class="campoGrande">
        <label>Email</label>
        <input type="text" v-model="infosUsuario.email" />
      </div>

      <!-- Senhas -->
      <div class="campoMetade">
        <input
          type="password"
          placeholder="Nova senha"
          v-model="novaSenha"
        />
        <input
          type="password"
          placeholder="Repetir nova senha"
          v-model="repetirSenha"
        />
      </div>

      <!-- Botão -->
      <button
        class="btnSalvar"
        :class="{ desabilitado: !formAlterado }"
        :disabled="!formAlterado"
        type="button"
        @click="salvar"
      >
        Salvar
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      meses: [
        'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
        'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
      ],
      diaNascimento: null,
      mesNascimento: null,
      anoNascimento: null,

      novaSenha: '',
      repetirSenha: '',
      mensagem: '',
      tipoMensagem: '',

      originalInfo: null     // snapshot inicial para comparação
    };
  },

  computed: {
    /* Vuex */
    infosUsuario() { return this.$store.getters.getInfosUsuario; },
    corAvatar()    { return this.$store.getters.getCorAvatar; },

    inicialUsuario() {
      const nome = this.$store.getters.getNomeUsuario || '';
      return nome.charAt(0).toUpperCase();
    },

    /* Cores */
    avatarColorHex() {
      const map = {
        blue: '#0000FF', green: '#008000', red: '#FF0000',
        purple: '#800080', orange: '#FFA500'
      };
      return map[this.corAvatar] || this.corAvatar || '#999';
    },
    avatarStyle()   { return { backgroundColor: this.avatarColorHex }; },
    containerStyle() {
      const c = this.avatarColorHex;
      return {
        border: `2px solid ${c}80`,
        boxShadow: `0 0 2px ${c}CC, 0 0 6px ${c}99, 0 0 12px ${c}66, 0 0 24px ${c}33`
      };
    },

    /* Datas no mesmo formato ISO yyyy-MM-dd */
    dataOriginalISO() { return this.originalInfo?.dataNascimento || ''; },
    dataAtualISO() {
      if (!this.anoNascimento || !this.mesNascimento || !this.diaNascimento)
        return '';
      return (
        this.anoNascimento +
        '-' +
        String(this.mesNascimento).padStart(2, '0') +
        '-' +
        String(this.diaNascimento).padStart(2, '0')
      );
    },

    /* Habilita / desabilita botão */
    formAlterado() {
      if (!this.originalInfo) return false;

      return (
        this.infosUsuario.username   !== this.originalInfo.username   ||
        this.infosUsuario.first_name !== this.originalInfo.first_name ||
        this.infosUsuario.last_name  !== this.originalInfo.last_name  ||
        this.infosUsuario.email      !== this.originalInfo.email      ||
        this.dataAtualISO            !== this.dataOriginalISO         ||
        this.novaSenha               !== ''                           ||
        this.repetirSenha            !== ''
      );
    }
  },

  watch: {
    /* guarda snapshot assim que infosUsuario chega */
    infosUsuario: {
      immediate: true,
      handler(val) {
        if (!val || this.originalInfo) return;
        this.originalInfo = JSON.parse(JSON.stringify(val));
      }
    },
    /* preenche selects */
    'infosUsuario.dataNascimento': {
      immediate: true,
      handler(val) {
        if (!val) return;
        const [y, m, d] = val.split('-');
        this.diaNascimento = Number(d);
        this.mesNascimento = m;
        this.anoNascimento = y;
      }
    }
  },

  created() {
    this.$store.dispatch('getCliente');
  },

  methods: {
    async salvar() {
      if (this.novaSenha && this.novaSenha !== this.repetirSenha) {
        this.mensagem = 'As senhas não são iguais.';
        this.tipoMensagem = 'erro';
        return;
      }

      const dataNasc =
        String(this.diaNascimento).padStart(2, '0') + '/' +
        this.mesNascimento + '/' +
        this.anoNascimento;

      const payload = {
        username:       this.infosUsuario.username,
        first_name:     this.infosUsuario.first_name,
        last_name:      this.infosUsuario.last_name,
        email:          this.infosUsuario.email,
        dataNascimento: dataNasc,
        password:       this.novaSenha || undefined
      };

      try {
        await this.$store.dispatch('atualizarInfosUsuario', payload);
        this.mensagem = 'Dados atualizados com sucesso!';
        this.tipoMensagem = 'sucesso';
        this.novaSenha = this.repetirSenha = '';
        // tira novo snapshot
        this.originalInfo = JSON.parse(JSON.stringify(this.infosUsuario));
        this.originalInfo.dataNascimento = this.dataAtualISO;
      } catch (err) {
        this.mensagem = err.message || 'Erro inesperado.';
        this.tipoMensagem = 'erro';
      }
    }
  }
};
</script>

<style scoped>
/* layout geral */
.pai {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  margin: 35px auto;
  max-height: 700px;
}

.containerFilho {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  width: 350px;
  height: 500px;
  min-height: 500px;
  padding: 5px 0;
  background: rgb(7, 7, 7);
  color: white;
  border-radius: 8px;
}

/* avatar */
.iconePerfil {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 70px;
  height: 70px;
  font-size: 40px;
  border-radius: 50%;
}

/* campos */
.campoGrande {
  width: 85%;
  display: flex;
  flex-direction: column;
}
.campoGrande > label { margin-bottom: 5px; }
.campoGrande > input {
  height: 30px;
  border: none;
  border-radius: 8px;
  padding-left: 8px;
}

.campoMetade {
  width: 85%;
  display: flex;
  gap: 20px;
}
.campoMetade > input {
  width: 50%;
  height: 30px;
  border: none;
  border-radius: 8px;
  padding-left: 8px;
}

.dataNascimento {
  width: 85%;
  display: flex;
  flex-direction: column;
}
.data {
  display: flex;
  justify-content: space-between;
}
.input {
  width: 32%;
  height: 30px;
  border: none;
  border-radius: 8px;
  padding-left: 8px;
}

/* botão */
.btnSalvar {
  width: 80%;
  padding: 10px;
  text-align: center;
  background: rgb(0, 185, 9);
  color: white;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.2s;
}
.btnSalvar:hover {
  background: rgb(0, 165, 8);
}
.btnSalvar.desabilitado,
.btnSalvar:disabled {
  background: #555;
  cursor: not-allowed;
  opacity: 0.6;
}

/* mensagens */
.alerta {
  width: 300px;
  padding: 8px 12px;
  text-align: center;
  font-weight: 600;
  border-radius: 6px;
}
.sucesso { background: #00800033; color: #32cd32; }
.erro    { background: #ff000033; color: #ff4500; }
</style>
