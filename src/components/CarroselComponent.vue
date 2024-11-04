<template>
  <div class="carrossel-container">
    <div class="carrossel">
      <div
        class="carrossel-items"
        :style="{ transform: `translateX(-${offset}%)` }"
      >
        <div
          class="item-carrossel"
          v-for="livro in livros"
          :key="livro.id"
          :style="{ flex: `0 0 calc(100% / ${itensVisiveis})` }"
        >
          <CardComponent :livro="livro" class="card"/>
        </div>
      </div>
      <transition name="fade">
        <button
          v-if="indiceAtual > 0"
          @click="anterior"
          class="seta seta-esquerda"
        >
          &lt;
        </button>
      </transition>
      <transition name="fade">
        <button
          v-if="indiceAtual + itensVisiveis < livros.length"
          @click="proximo"
          class="seta seta-direita"
        >
          &gt;
        </button>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import CardComponent from './CardComponent.vue'; // Ajuste o caminho conforme necessário

export default {
  components: {
    CardComponent,
  },
  data() {
    return {
      livros: [],
      indiceAtual: 0,
      itensVisiveis: 4,
    };
  },
  created() {
    this.buscarTodosLivros();
  },
  computed: {
    larguraItem() {
      return 100 / this.itensVisiveis;
    },
    offset() {
      return this.indiceAtual * this.larguraItem;
    },
  },
  methods: {
    async buscarTodosLivros() {
      try {
        const res = await axios.get(
          'http://localhost:8000/api/livros/todosLivros'
        );
        this.livros = res.data;
      } catch (error) {
        console.error('Ocorreu um erro: ' + error);
      }
    },
    proximo() {
      if (this.indiceAtual + this.itensVisiveis < this.livros.length) {
        this.indiceAtual++;
      }
    },
    anterior() {
      if (this.indiceAtual > 0) {
        this.indiceAtual--;
      }
    },
  },
};
</script>

<style scoped>
.carrossel-container {
  width: 100%;
  overflow: hidden;
  height: 390px;
}

.carrossel {
  position: relative;
  width: 100%;
}

.carrossel-items {
  display: flex;
  transition: transform 0.5s ease;
}

.item-carrossel {
  box-sizing: border-box;
  padding: 0 10px;
  text-align: center;
}

.seta {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255, 255, 255, 0.897);
  cursor: pointer;
  font-size: 4em;
  background: none;
  border: none;
  z-index: 1;
}

.seta-esquerda {
  left: 0;
}

.seta-direita {
  right: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
