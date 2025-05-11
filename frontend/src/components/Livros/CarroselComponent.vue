<template>
  <div class="carroselContainer">
    <div class="carrossel">
      <div class="carroselItens" :style="{ transform: `translateX(-${offset}%)` }">
        <div v-for="item in livros" :key="item.id" :style="{ flex: `0 0 calc(100% / ${itensVisiveis})` }" class="itemCarrosel">
          <LivroCard v-if="tipo !== 'combos'" :livro="item" />
          <ComboCard v-else :combo="item" />
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
import LivroCard from './LivroCard.vue'
import ComboCard from './ComboCard.vue'

export default {
  props: ['tipo'],
  components: { LivroCard, ComboCard },
  data() {
    return {
      itensVisiveis: 5,
      indiceAtual: 0
    }
  },
  created() {
    this.definirItensVisiveis()
    window.addEventListener('resize', this.definirItensVisiveis)

    if (this.tipo === 'UltimosLancamentosLoja') {
      this.$store.dispatch('buscarUltimosLancamentosLoja')
    } else if (this.tipo === 'maisVendidos') {
      this.$store.dispatch('buscarMaisVendidos')
    } else if (this.tipo === 'combos') {
      this.$store.dispatch('buscarTodosCombos')
    }
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.definirItensVisiveis)
  },
  computed: {
    livros() {
      if (this.tipo === 'UltimosLancamentosLoja')
        return this.$store.getters.getStateUltimosLancamentosLoja
      if (this.tipo === 'maisVendidos')
        return this.$store.getters.getStateMaisVendidos
      if (this.tipo === 'combos') return this.$store.getters.getTodosCombos
      return []
    },
    larguraItem() {
      return 100 / this.itensVisiveis
    },
    offset() {
      return this.indiceAtual * this.larguraItem
    }
  },
  methods: {
    definirItensVisiveis() {
      const w = window.innerWidth
      const tipoCombo = this.tipo === 'combos'

      if (w <= 480) {
        this.itensVisiveis = tipoCombo ? 2 : 2
      } else if (w <= 768) {
        this.itensVisiveis = tipoCombo ? 2 : 3
      } else if (w <= 1024) {
        this.itensVisiveis = tipoCombo ? 3 : 4
      } else {
        this.itensVisiveis = tipoCombo ? 4 : 5
      }

      /* garante que índice não estoure quando a tela diminui */
      if (this.indiceAtual + this.itensVisiveis > this.livros.length) {
        this.indiceAtual = Math.max(
          0,
          this.livros.length - this.itensVisiveis
        )
      }
    },
    proximo() {
      if (this.indiceAtual + this.itensVisiveis < this.livros.length) {
        this.indiceAtual++
      }
    },
    anterior() {
      if (this.indiceAtual > 0) {
        this.indiceAtual--
      }
    }
  }
}
</script>

<style scoped>
.carroselContainer {
  width: 100%;
  overflow: hidden;
  height: 390px;
  padding-top: 40px;
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
  color: rgba(255, 255, 255, 0.9);
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

@media (max-width: 768px) {
  .carroselContainer {
    height: 310px;
    padding-top: 30px;
  }
  .seta {
    font-size: 3em;
  }
}
@media (max-width: 480px) {
  .carroselContainer {
    height: 330px;
    padding-top: 25px;
  }
  .seta {
    font-size: 2.4em;
  }
}
</style>
