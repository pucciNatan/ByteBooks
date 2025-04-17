<template>
  <div class="main">
    <!-- a chave força o Vue recriar o componente sempre que rota muda -->
    <SessaoPesquisa
      :key="`${$route.params.categoria || ''}-${$route.params.livro || ''}`"
      :tipo="categoria"
      :livro="livro"
    />
  </div>
</template>

<script>
import SessaoPesquisa from '../components/SessoesPesquisa.vue';

export default {
  name: 'PesquisaView',
  components: { SessaoPesquisa },

  computed: {
    livro() {
      return this.$route.params.livro || '';
    },
    categoria() {
      return this.$route.params.categoria || '';
    }
  }
};
</script>

<style scoped>
.main {
  width: 90%;
  margin: 30px auto;
  min-height: 600px;
}
</style>
