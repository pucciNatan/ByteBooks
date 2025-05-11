<template>
  <div class="containerPagProduto">
    <div class="conteudoEsquerda">
      <div class="imgProduto">
        <img v-for="livro in combo.livros" :key="livro.id" :src="'https://bytebooks-backend.fly.dev' + livro.img" :alt="'Capa do livro ' + livro.titulo" />
      </div>

      <div class="detalhesCombo scrollMinimalista">
        - Descrição: <br /><br />
        {{ combo.descricao }}
      </div>
    </div>

    <div class="conteudoDireita">
      <div class="titulo">{{ combo.tituloCombo }}</div>

      <div v-if="combo.estoque > 0" class="estoque">
        {{ combo.qtdVendas }} unidades vendidas
      </div>
      <div v-else class="estoque">ESGOTADO</div>

      <div
        class="descricao scrollMinimalista"
        v-html="formatarDescricao(combo.descricaoDetalhada)"
      ></div>

      <div class="preco">R$ {{ combo.preco }}</div>

      <div class="botoes">
        <div class="botao carrinho">Adicionar ao carrinho</div>
        <div class="botao compra">Comprar</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    this.$store.dispatch("carregarDetalhesCombo", this.idCombo);
  },
  computed: {
    combo() {
      return this.$store.getters.getDetalhesCombo;
    },
  },
  data() {
    return {
      idCombo: this.$route.params.idCombo,
    };
  },
  methods: {
    formatarDescricao(texto) {
      return texto ? texto.replace(/\n/g, "<br>") : "";
    },
  },
};
</script>

<style scoped>
.containerPagProduto {
    margin: auto;
    height: 570px;
    width: 940px;
    display: flex;
    justify-content: space-between;
    padding: 20px;
    border-radius: 6px;
    background-color: #131313;
    font-family: 'Roboto', sans-serif;
}

.conteudoEsquerda {
    width: 550px;
}

/* CAPAS SOBREPOSTAS */
.imgProduto {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 470px;
    height: 390px;
    padding: 15px;
    background-color: #f3f3f3;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

.imgProduto img {
    height: 330px;
    position: absolute;
    border-radius: 6px;
    transition: transform 0.3s ease, z-index 0.3s ease;
}

.imgProduto img:nth-child(1) {
    transform: translateX(-80px) translateY(10px) rotate(-10deg);
    z-index: 1;
}

.imgProduto img:nth-child(2) {
    transform: translateX(0px) translateY(-10px) rotate(5deg);
    z-index: 2;
}

.imgProduto img:nth-child(3) {
    transform: translateX(80px) translateY(10px) rotate(15deg);
    z-index: 3;
}

.detalhesCombo {
    margin-top: 20px;
    width: 480px;
    height: 110px;
    padding: 10px;
    background-color: #2C2C2C;
    border-radius: 6px;
    color: #e5e5e5;
    overflow: auto;
    line-height: 1.5;
}

.conteudoDireita {
    width: 400px;
    max-height: 540px;
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #1f1f1f;
    color: #e5e5e5;
    border-radius: 6px;
}

.titulo {
    font-size: 33px;
    max-height: 100px;
    overflow: hidden;
}

.estoque {
    height: 20px;
    color: #c2c2c2;
}

.descricao {
    height: 210px;
    padding: 10px;
    background-color: #2C2C2C;
    border-radius: 5px;
    overflow: auto;
}

.preco {
    font-size: 34px;
    color: #dee204;
    margin: 5px 0 15px;
    height: 50px;
    display: flex;
    align-items: center;
}

.botoes {
    display: flex;
    justify-content: space-between;
    font-weight: 600;
}

.botao {
    width: 49%;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    background-color: #3f3f3f;
    border-radius: 5px;
    transition: background-color 0.3s;
}

/* -------- TABLET (≤ 1024 px) -------- */
@media (max-width: 1024px) {
    .containerPagProduto {
        flex-direction: column;
        align-items: center;
        width: 600px;
        height: auto;
        margin-top: 70px;
    }

    .conteudoEsquerda,
    .conteudoDireita {
        width: 100%;
    }

    .estoque {
        margin: 20px 0px;
        color: #c2c2c2;
    }

    .imgProduto {
        width: 95%;
        height: 320px;
    }

    .imgProduto img {
        height: 270px;
    }

    .detalhesCombo {
        width: 97%;
    }

    .conteudoDireita {
        max-height: none;
        margin-top: 24px;
    }
}

/* -------- MOBILE (≤ 768 px) -------- */
@media (max-width: 768px) {
    .titulo {
        font-size: 26px;
    }

    .descricao {
        height: 160px;
        font-size: 14px;
    }

    .preco {
        font-size: 28px;
    }

    .botao {
        height: 52px;
        font-size: 16px;
    }
}

/* -------- SMALL MOBILE (≤ 480 px) -------- */
@media (max-width: 480px) {
    .containerPagProduto {
        width: 80%;
    }

    .imgProduto {
        height: 260px;
        padding: 10px;
    }

    .imgProduto img {
        height: 180px;
    }

    .detalhesCombo {
        width: 96%;
    }

    .descricao {
        height: 140px;
    }

    .botoes {
        flex-direction: column;
        gap: 10px;
    }

    .botao {
        width: 100%;
    }
}
</style>
