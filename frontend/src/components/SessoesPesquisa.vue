<template>
  <div class="sessao">
    <!-- Cabeçalho -->
    <p class="pesquisandoPor">
      <template v-if="tipo === 'lancamentos'">
        Últimos lançamentos
      </template>
      <template v-else-if="tipo === 'dados'">
        Dados
      </template>
      <template v-else-if="tipo === 'software'">
        Software
      </template>
      <template v-else-if="tipo === 'backend'">
        Backend
      </template>
      <template v-else>
        Pesquisando por – {{ livro }}
      </template>
    </p>

    <!-- Lista de livros -->
    <div v-if="livros.length" class="livrosEncontrados">
      <div
        v-for="item in livros"
        :key="item.id"
        class="livroEncontrado"
      >
        <LivroCard :livro="item" />
      </div>
    </div>

    <!-- Nenhum resultado -->
    <div v-else class="naoHaLivros">
      Não há livros para esta consulta.
    </div>
  </div>
</template>

<script>
import LivroCard from './Livros/LivroCard.vue';

export default {
  name: 'SessaoPesquisa',

  props: {
    tipo: { type: String, required: true },
    livro: { type: String, default: '' }
  },

  components: { LivroCard },

  /* ----------------------------------
     1ª chamada (quando componente nasce)
  ---------------------------------- */
  created() {
    this.buscarDados();
  },

  /* ----------------------------------
     quando props mudam, chamamos de novo
  ---------------------------------- */
  watch: {
    tipo()   { this.buscarDados(); },
    livro()  { this.buscarDados(); }
  },

  methods: {
    buscarDados() {
      // decide qual action chamar baseado no tipo
      switch (this.tipo) {
        case 'lancamentos':
          this.$store.dispatch('buscarUltimosLancamentosLoja');
          break;
        case 'dados':
        case 'backend':
        case 'software':
          this.$store.dispatch('pesquisarLivrosPorCategoria', this.tipo);
          break;
        default:
          this.$store.dispatch('pesquisarPorLivro', this.livro);
      }
    }
  },

  computed: {
    livros() {
      // se quiser diferenciar promoções etc., ajuste aqui
      if (this.tipo === 'lancamentos') {
        return this.$store.getters.getStateUltimosLancamentosLoja;
      }
      return this.$store.getters.getLivrosPesquisados;
    }
  }
};
</script>

<style scoped>
.sessao {
  width: 100%;
}

/* título */
.pesquisandoPor {
  font-family: 'Roboto', sans-serif;
  margin: 50px 0 30px;
  color: white;
  font-size: 30px;
}

/* grade responsiva */
.livrosEncontrados {
  display: grid;
  gap: 50px;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
}

.livroEncontrado {
  margin-bottom: 25px;
}

.naoHaLivros {
  font-family: 'Roboto', sans-serif;
  font-size: 20px;
  color: rgba(242, 242, 242, 0.9);
}
</style>
