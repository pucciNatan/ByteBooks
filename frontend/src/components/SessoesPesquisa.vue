<template>
  <div class="sessao">
    <!-- Cabeçalho -->
    <p class="pesquisandoPor">
      <template v-if="tipo === 'lancamentos'">Últimos lançamentos</template>
      <template v-else-if="tipo === 'dados'">Dados</template>
      <template v-else-if="tipo === 'software'">Software</template>
      <template v-else-if="tipo === 'backend'">Backend</template>
      <template v-else>Pesquisando por – {{ livro }}</template>
    </p>

    <div v-if="livros.length" class="livrosEncontrados">
      <div v-for="item in livros" :key="item.id" class="livroEncontrado">
        <LivroCard :livro="item" />
      </div>
    </div>

    <div v-else class="naoHaLivros">Não há livros para esta consulta.</div>
  </div>
</template>

<script>
import LivroCard from "./Livros/LivroCard.vue";

export default {
  name: "SessaoPesquisa",
  props: {
    tipo: { type: String, required: true },
    livro: { type: String, default: "" },
  },
  components: { LivroCard },
  created() {
    this.buscarDados();
  },
  watch: {
    tipo() {
      this.buscarDados();
    },
    livro() {
      this.buscarDados();
    },
  },
  methods: {
    buscarDados() {
      if (this.tipo === "lancamentos") {
        this.$store.commit("limparUltimosLancamentos");
      } else {
        this.$store.commit("limparLivrosPesquisados");
      }

      switch (this.tipo) {
        case "lancamentos":
          this.$store.dispatch("buscarUltimosLancamentosLoja");
          break;
        case "dados":
        case "backend":
        case "software":
          this.$store.dispatch("pesquisarLivrosPorCategoria", this.tipo);
          break;
        default:
          this.$store.dispatch("pesquisarPorLivro", this.livro);
      }
    },
  },
  computed: {
    livros() {
      return this.tipo === "lancamentos"
        ? this.$store.getters.getStateUltimosLancamentosLoja
        : this.$store.getters.getLivrosPesquisados;
    },
  },
};
</script>

<style scoped>
.sessao { width: 98%; }

.pesquisandoPor {
  font-family: "Roboto", sans-serif;
  margin: 50px 0 30px;
  color: #ffffff;
  font-size: 2rem;
}

.livrosEncontrados {
  display: grid;
  gap: 50px;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
}
.livroEncontrado { margin-bottom: 25px; }

.naoHaLivros {
  font-family: "Roboto", sans-serif;
  font-size: 1.25rem; /* 20px */
  color: rgba(242, 242, 242, 0.9);
  text-align: center;
}

@media (max-width: 1024px) {
  .livrosEncontrados {
    gap: 40px;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  }
}

@media (max-width: 600px) {
  .pesquisandoPor { font-size: 1.5rem; margin-bottom: 20px; }
  .livrosEncontrados {
    gap: 20px;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  }
  .naoHaLivros { font-size: 1rem; }
}

@media (max-width: 360px) {
  .pesquisandoPor { font-size: 1.25rem; }
  .livrosEncontrados {
    gap: 20px;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  }
}
</style>
