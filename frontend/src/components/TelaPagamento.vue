<template>
  <div class="main">
    <!-- COLUNA ESQUERDA -->
    <div class="colunas" v-if="!compradoComSucesso">
      <div class="colunaEsquerda">
      <label class="tituloColuna">Seu saldo</label>

      <div class="colunaSaldo">
        <span class="saldo">R$ {{ saldoCliente }}</span>
        <button class="botaoAdd" @click="atualizarSaldo50">+ R$ 50</button>
      </div>

      <div class="precoProduto">
        <label>Total da compra</label>
        <span>R$ {{ total }}</span>
      </div>

      <div class="saldoFinal">
        <label>Saldo final</label>
        <span>R$ {{ getSaldoFinal() }}</span>
      </div>

      <button class="botaoConfirmar" @click="finalizarCompra">
        Finalizar compra
      </button>
    </div>

    <!-- COLUNA DIREITA -->
    <div class="colunaDireita">
      <div class="carrinho">
        <ul class="listaLivros">
          <li v-for="(item,index) in itens" :key="index" class="itemLivro">
            <img
              :src="'http://localhost:8000'+item.livro.img"
              :alt="'Capa do livro' + item.livro.titulo"
            />
            <div class="detalhes">
              <span class="tituloLivro">{{ item.livro.titulo }}</span>
              <span class="quantidade">x{{ item.quantidade ?? 1 }}</span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <div v-else class="comprado">
    <h1>Compra realizada com sucesso!</h1>
    <p>Veja seus livros adquiridos: <router-link class="link" to="/minhasCompras">aqui</router-link></p>
  </div>

  <div class="fecharCompra" @click="fecharCompra">X</div>
</div>
    
</template>

<script>
import { getSaldoCliente, atualizarSaldoCliente50 } from "../api/apiService";

export default {
  name: "TelaPagamento",
  props: {
    itens: { type: Array, required: true },
    total: { type: String, required: true },
  },
  data() {
    return { 
      saldoCliente: 0,
      compradoComSucesso: false
    };
  },
  async created() {
    try {
      const res = await getSaldoCliente();
      this.saldoCliente = parseFloat(res.data);
    } catch (e) {
      console.error("Erro ao buscar saldo:", e);
    }
  },
  methods:{
    async finalizarCompra() {
      await Promise.all(
        this.itens.map(({ livro, quantidade }) =>
          this.$store.dispatch("comprarLivro", { idLivro: livro.id, quantidade }),
        )
      );

      await this.$store.dispatch("carregarItensCarrinho");
      const { data } = await getSaldoCliente();
      this.saldoCliente = Number(data.saldo ?? data);
      this.compradoComSucesso = true;
    },
    getSaldoFinal(){
      const saldoFinal = (this.saldoCliente - parseFloat(this.total)).toFixed(2)
      return saldoFinal
    },
    async atualizarSaldo50(){
      await atualizarSaldoCliente50()
      const res = await getSaldoCliente();
      this.saldoCliente = parseFloat(res.data);
    },
    fecharCompra(){
      this.$emit('confirmarCompra');
    }
  }
};
</script>
  
  <!-- VARIÁVEIS GLOBAIS -->
  <style>
  :root {
    --bg-card: #1f242d;
    --bg-input: #252b35;
    --bg-item: #2b3039;
    --border: #3a414c;
    --text: #dfe3ea;
    --primaria: #009405;
    --primaria-hover: #00b306;
    --radius: 8px;
    --item-h: 60px; /* ~90px capa + paddings */
  }
  </style>
  
  <style scoped>
  .main {
    position: relative;
    font-family: "Roboto", sans-serif;
    padding: 2rem;
    border-radius: var(--radius);
    background: var(--bg-card);
    width: min(100%, 700px);
    margin-inline: auto;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    color: var(--text);
    align-items: stretch;
  }

  .colunas{
    display: flex;
    gap: 2rem;
  }
  
  /* -------- ESQUERDA -------- (sem mudanças) */
  .colunaEsquerda {
    flex: 1 1 45%;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .tituloColuna {
    font-size: clamp(1rem, 2vw, 1.3rem);
    font-weight: 600;
  }
  
  .colunaSaldo {
    display: flex;
    gap: 0.5rem;
  }
  
  .saldo {
    flex: 1;
    background: var(--bg-input);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    display: flex;
    align-items: center;
    padding: 0.5rem 1rem;
    font-size: 1.4rem;
  }
  
  .botaoAdd {
    background: var(--primaria);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    padding: 0.5rem 0.75rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.15s ease;
  }
  .botaoAdd:hover { background: var(--primaria-hover); }
  
  .precoProduto,
  .saldoFinal {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg-input);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    padding: 0.75rem 1rem;
    font-size: clamp(0.9rem, 1.8vw, 1rem);
  }
  
  .botaoConfirmar {
    background: var(--primaria);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    padding: 0.75rem 1.5rem;
    font-size: 1.1rem;
    cursor: pointer;
    transition: background 0.15s ease;
    width: 100%;
  }
  .botaoConfirmar:hover { background: var(--primaria-hover); }
  
  /* -------- DIREITA -------- */
  .colunaDireita {
    flex: 1 1 45%;
    display: flex;
    flex-direction: column;
  }
  
  .carrinho {
    flex: 1;
    background: var(--bg-input);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    padding: 0.75rem;
    overflow-y: auto;
    max-height: calc(var(--item-h) * 3.7 + 2rem);
  }
  
  /* Scrollbar minimalista (WebKit) */
  .carrinho::-webkit-scrollbar {
    width: 4px;
  }
  .carrinho::-webkit-scrollbar-track {
    background: transparent;
  }
  .carrinho::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 3px;
  }
  
  /* lista */
  .listaLivros {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .itemLivro {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: var(--bg-item);
    border-radius: var(--radius);
    padding: 0.75rem;
    height: var(--item-h);
  }
  
  .itemLivro img {
    width: 50px;
    height: 70px;
    object-fit: cover;
    border-radius: 4px;
  }
  
  .detalhes {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex: 1;
  }
  
  .tituloLivro {
    font-size: 1rem;
    width: 80%;
    font-weight: 500;
    line-height: 1.2;
  }
  
  .quantidade {
    font-size: 0.9rem;
    opacity: 0.8;
  }

  .fecharCompra{
    top: 7px;
    right: 13px;
    position: absolute;
}

  .fecharCompra:hover{
      cursor: pointer;
  }

  .comprado{
    display: flex;
    gap:12px;
    flex-direction: column;
  }

  .comprado > h2{
    font-size: 20px;
  }

  .link{
    color: rgb(80, 80, 220);

  }
  
  /* -------- MOBILE -------- */
  @media (max-width: 600px) {
    .main { flex-direction: column; gap: 1.5rem; }
    .carrinho { max-height: calc(var(--item-h) * 2.5 + 1.5rem); }
  }
  </style>
  