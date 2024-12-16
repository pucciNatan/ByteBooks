<template>
  <div class="carroselContainer">
    <div class="carrossel">
      <div class="carroselItens" :style="{ transform: `translateX(-${offset}%)` }">
        <div v-for="item in livros" :key="item.id" :style="{ flex: `0 0 calc(100% / ${itensVisiveis})` }" class="itemCarrosel">
          <LivroCard 
            v-if="tipo !== 'combos'" :livro="item"/>
          <ComboCard 
            v-else :combo="item"/>
        </div>
      </div>
      <transition name="fade">
        <button v-if="indiceAtual > 0" @click="anterior" class="seta setaEsquerda">
          &lt;
        </button>
      </transition>
      <transition name="fade">
        <button v-if="indiceAtual + itensVisiveis < livros.length" @click="proximo" class="seta setaDireita">
          &gt;
        </button>
      </transition>
    </div>
  </div>
</template>

<script>
import LivroCard from './LivroCard.vue';
import ComboCard from './ComboCard.vue';

export default {
  props: ['tipo'],
  components: {
    LivroCard,
    ComboCard,
  },
  data() {
    if(this.tipo == 'combos'){
      return{
        itensVisiveis: 4,
        indiceAtual: 0,
      }
    }
    return {
      itensVisiveis: 5,
      indiceAtual: 0,
      
    };
  },
  created() {
    if (this.tipo === 'UltimosLancamentosLoja') {
      this.$store.dispatch('buscarUltimosLancamentosLoja');
    } else if (this.tipo === 'maisVendidos') {
      this.$store.dispatch('buscarMaisVendidos');
    } else if (this.tipo === 'combos') {
      this.$store.dispatch('buscarTodosCombos');
    }
  },
  computed: {
    livros() {
      if (this.tipo === 'UltimosLancamentosLoja') {
        return this.$store.getters.getStateUltimosLancamentosLoja;
      } else if (this.tipo === 'maisVendidos') {
        return this.$store.getters.getStateMaisVendidos;
      } else if (this.tipo === 'combos') {
        return this.$store.getters.getTodosCombos;
      } else {
        return [];
      }
    },
    larguraItem() {
      return 100 / this.itensVisiveis;
    },
    offset() {
      return this.indiceAtual * this.larguraItem;
    },
  },
  methods: {
    proximo() {
      if (this.indiceAtual + this.itensVisiveis < this.livros.length) {
        this.indiceAtual += 1;
      } else {
        this.indiceAtual = this.livros.length - this.itensVisiveis;
        if (this.indiceAtual < 0) {
          this.indiceAtual = 0;
        }
      }
    },
    anterior() {
      if (this.indiceAtual > 0) {
        this.indiceAtual -= 1;
        if (this.indiceAtual < 0) {
          this.indiceAtual = 0;
        }
      }
    },
  },
};
</script>

<style scoped>
.carroselContainer {
  width: 100%;
  overflow: hidden;
  height: 390px;
  padding-top: 40px;
}
.sessao {
  display: flex;
}
.carrossel {
  position: relative;
  width: 100%;
}

.carroselItens {
  display: flex;
  transition: transform 0.5s ease;
}

.itemCarrosel {
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

.setaEsquerda {
  left: 0;
}

.setaDireita {
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
