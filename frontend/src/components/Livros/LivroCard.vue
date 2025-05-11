<template>
  <div class="container">
    <router-link :to="`/paginaLivro/${livro.id}`" class="routerLink">
      <div class="cardLivro">
        <div @click="abrirDetalhesLivro" class="imgLivro">
          <img
            :src="`https://bytebooks-backend.fly.dev${livro.img}`"
            :alt="`Capa do livro ${livro.titulo}`"
          />
        </div>

        <div class="infosLivros">
          <div class="tituloEDesc">
            <div class="tituloLivro">{{ livro.titulo }}</div>
            <div class="autorLivro">{{ livro.autor }}</div>
          </div>

          <div v-if="!comprado" :class="precoClass">R$ {{ livro.preco }}</div>

          <div v-else class="compradoEm">
            <label>Comprado em</label><br />
            {{ formatDataCompra(livro.dataCompra) }}
          </div>
        </div>

        <button v-if="!comprado" class="botaoComprar">
          <img src="../../imgs/carrinhoDeCompras.png" alt="Carrinho de compras" />
          <span>Comprar</span>
        </button>
        <button v-else class="botaoComprar">
          <span>Ver produto</span>
        </button>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    livro: { type: Object, required: true },
    comprado: { type: Boolean, default: false }
  },
  computed: {
    precoClass() {
      const tamanho = String(this.livro.preco).replace(/\D/g, '').length;
      return tamanho >= 7 ? 'precoLivro precoPequeno' : 'precoLivro';
    }
  },
  methods: {
    formatDataCompra(dataString) {
      if (!dataString) return '';
      const data = new Date(dataString);
      const dia = String(data.getDate()).padStart(2, '0');
      const mes = String(data.getMonth() + 1).padStart(2, '0');
      const ano = data.getFullYear();
      const hora = String(data.getHours()).padStart(2, '0');
      const min = String(data.getMinutes()).padStart(2, '0');
      const seg = String(data.getSeconds()).padStart(2, '0');
      return `${dia}/${mes}/${ano} ${hora}:${min}:${seg}`;
    },
  }
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}

.cardLivro {
  width: 190px;
  background-color: #2c2c2c;
  color: #fff;
  font-family: 'Open Sans', sans-serif;
  cursor: pointer;
  border-radius: 8px;
  transition: transform 0.3s ease;
  display: flex;
  flex-direction: column;
}
.cardLivro:hover {
  transform: scale(1.03);
}

.imgLivro {
  padding: 7px;
  display: flex;
  height: 170px;
  background-color: #fff;
  justify-content: center;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
.imgLivro img {
  width: 70%;
  border-radius: 4px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.infosLivros {
  text-align: center;
  background-color: #333;
  padding: 10px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.tituloLivro {
  height: 50px;
  overflow: hidden;
  font-size: 18px;
  font-weight: bold;
  color: #f1f1f1;
}
.autorLivro {
  height: 35px;
  overflow: hidden;
  font-size: 12px;
  margin-top: 4px;
  color: #a0a0a0;
}

.precoLivro {
  font-size: 26px;
  margin: 10px 0;
  font-family: 'Montserrat', sans-serif;
  color: #dee204;
  line-height: 1;
  height: 30px;
  white-space: nowrap;
}
.precoPequeno {
  font-size: 20px;
}

.botaoComprar {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  background-color: #4caf50;
  color: #fff;
  height: 40px;
  border: none;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  transition: background-color 0.3s ease;
}
.botaoComprar:hover {
  background-color: #2d8031;
  cursor: pointer;
}
.botaoComprar img {
  width: 17px;
}
.botaoComprar span {
  font-size: 18px;
  margin-left: 6px;
}

.routerLink {
  text-decoration: none;
}

.compradoEm {
  font-size: 17px;
}
.compradoEm label {
  font-size: 12px;
}

@media (min-width: 481px) and (max-width: 1024px) {
  .cardLivro {
    width: 160px;
  }
  .imgLivro {
    height: 140px;
  }
  .tituloLivro {
    font-size: 16px;
    height: 46px;
  }
  .autorLivro {
    font-size: 11px;
    height: 32px;
  }
  .precoLivro {
    font-size: 22px;
  }
}

@media (max-width: 480px) {
  .cardLivro {
    width: 120px;
  }
  .imgLivro {
    height: 100px;
  }
  .tituloLivro {
    font-size: 16px;
    height: 46px;
  }
  .autorLivro {
    font-size: 11px;
    height: 32px;
  }
  .infosLivros {
    padding: 8px;
    height: 100px;

  }
  .precoLivro {
    font-size: 17px;
  }
  .botaoComprar {
    height: 36px;
  }
  .compradoEm {
    font-size: 10px;
  }
  .compradoEm label {
    font-size: 11px;
  }
}
</style>
