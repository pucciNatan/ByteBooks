<template>
    <div class="containerPagProduto">
        <div class="conteudoEsquerda">
            <div class="imgProduto" :alt="'Imagem do combo ' + combo.tituloCombo">
                <img v-for="livro in combo.livros" :key="livro.id" :src="'http://localhost:8000' + livro.img">
            </div>
            
            <div class="detalhesCombo scrollMinimalista">
                - Descrição: <br> <br>
                {{ combo.descricao }}
            </div>
            
        </div>

        <div class="conteudoDireita">
            <div class="titulo">{{ combo.tituloCombo }}</div>

            <div v-if="combo.estoque > 0" class="estoque">{{ combo.qtdVendas }} unidades vendidas</div>
            <div v-else class="estoque">ESGOTADO</div>

            <div class="descricao scrollMinimalista" v-html="formatarDescricao(combo.descricaoDetalhada)"></div>

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
    this.$store.dispatch('carregarDetalhesCombo', this.idCombo)
  },
  computed: {
    combo() {
      return this.$store.getters.getDetalhesCombo
    }
  },
  data() {
    return {
      idCombo: this.$route.params.idCombo
    }
  }, methods:{
    formatarDescricao(texto) {
      if (!texto) {
        return "";
      }
      return texto.replace(/\n/g, "<br>");
    }
  }
}
</script>

<style scoped>
.containerPagProduto {
    margin: auto;
    height: 570px;
    width: 940px;
    justify-content: space-between;
    padding: 20px;
    border-radius: 6px;
    display: flex; 
    overflow: hidden;
    background-color: #131313;
    font-family: 'Roboto', sans-serif;
}
.conteudoEsquerda {
    width: 550px;
}
.imgProduto{
    display: flex;
    align-items: center;
    width: 470px;
    justify-content: center;
    padding: 15px;
    height: 390px;
    background-color: rgb(243, 243, 243);
    border-radius: 6px;
    position: relative;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}
.imgProduto > img{
    height: 330px;
    border-radius: 6px;
    position: absolute;
    transition: transform 0.3s ease, z-index 0.3s ease;
}
.imgProduto img:nth-child(1){
  transform: translateX(-80px) translateY(10px) rotate(-10deg);
  z-index: 1;
}
.imgProduto img:nth-child(2){
  transform: translateX(0px) translateY(-10px) rotate(5deg);
  z-index: 2;
}
.imgProduto img:nth-child(3){
  transform: translateX(80px) translateY(10px) rotate(15deg);
  z-index: 3;
}
.detalhesCombo{
    padding: 10px;
    color: rgb(229, 229, 229);
    margin-top: 20px;
    width: 480px;
    background-color: #2C2C2C;
    height: 110px;
    overflow: auto;
    white-space: normal;       
    word-wrap: break-word;     
    overflow-wrap: break-word;  
    border-radius: 6px;
    line-height: 1.5;
}
.scrollMinimalista::-webkit-scrollbar {
    width: 6px;          
    height: 6px;          
    background: transparent;
}

.scrollMinimalista::-webkit-scrollbar-track {
    background: transparent;
}

.scrollMinimalista::-webkit-scrollbar-thumb {
    background: #e3e3e3;
    border-radius: 10px;
}

.scrollMinimalista::-webkit-scrollbar-thumb:hover {
    background: #bbb;
}

.scrollMinimalista::-webkit-scrollbar-button {
    background: transparent;
}

.scrollMinimalista::-webkit-scrollbar-button:hover {
    background: #fff;
}
.quadrado > strong{
    font-size: 15px;
    margin-bottom: 6px;
}
.conteudoDireita {
    border-radius: 6px;
    width: 400px;
    background-color: #1f1f1f;
    max-height: 540px;
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    color: rgb(229, 229, 229);
}
.titulo{
    max-height: 100px;
    font-size: 33px;
    overflow: hidden;
}
.estoque{
    height: 20px;
    color: #c2c2c2;
}
.descricao{
    height: 210px;
    padding: 10px;
    border-radius: 5px;
    background-color: #2C2C2C;
    overflow: auto;
    white-space: pre-wrap;     
    word-wrap: break-word;     
    overflow-wrap: break-word;  
    line-height: 1.5;
}
.preco{
    font-size: 34px;
    color: #dee204;
    font-weight: 500;
    margin: 5px 0 15px;
    height: 50px;
    display: flex;
    align-items: center;
    overflow: hidden;
}
.botoes{
    display: flex;
    font-family: 'Roboto', sans-serif;
    font-weight: 600;
    align-items: center;
    justify-content: space-between;
}
.botao{
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgb(255, 255, 255);
    width: 49%;
    height: 60px;
    border: none;
    transition: background-color 0.3s;
    border-radius: 5px;
    overflow: hidden;
    background-color: #3f3f3f;
    
}

</style>