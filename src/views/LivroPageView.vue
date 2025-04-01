<template>
    <div class="containerPagProduto">
        <div class="conteudoEsquerda">
            <div class="imgProduto">
                <img :src="'http://localhost:8000' + livro.img" :alt="'Capa do livro ' + livro.titulo">
            </div>
            <div class="metadados">
                <div class="quadradosInfos">
                    <div class="quadrado">
                        <strong>Autor</strong>
                        <span>{{ livro.autor }}</span>
                    </div>
                    <div class="quadrado">
                        <strong>Editora</strong>
                        <span>{{ livro.editora }}</span>
                    </div>
                    <div class="quadrado">
                        <strong>Idioma</strong>
                        <span>{{ livro.idioma }}</span>
                    </div>
                </div>
                <div class="quadradosInfos">
                    <div class="quadrado">
                        <strong>Páginas</strong>
                        <span>{{ livro.qtdPaginas }}</span>
                    </div>
                    <div class="quadrado">
                        <strong>Estoque</strong>
                        <span>{{ livro.estoque }}</span>
                    </div>
                    <div class="quadrado">
                        <strong>Lançamento</strong>
                        <span>{{ livro.dataLancamento }}</span>
                    </div> 
                </div>
            </div>
            
        </div>

        <div class="conteudoDireita">
            <div class="titulo">{{ livro.titulo }}</div>

            <div v-if="livro.qtdVendas > 0" class="avaliacoes"><AvaliacaoEstrelas :rating="livro.avaliacaoGeral" /> ({{ livro.qtdAvaliacoes }})</div>

            <div class="descricao scrollMinimalista">{{ livro.descricao }}</div>

            <div class="preco">R$ {{ livro.preco }}</div>

            <div class="botoes">
                <div class="botao carrinho">Adicionar ao carrinho</div>
                <div class="botao compra">Comprar</div>
            </div>
        </div>
    </div>
</template>

<script>
import AvaliacaoEstrelas from '../components/AvaliacaoEstrelas.vue'

export default {
    components: {
        AvaliacaoEstrelas
    },
    created() {
        this.$store.dispatch('carregarDetalhesLivro', this.idLivro)
    },
    computed: {
        livro() {
        return this.$store.getters.getDetalhesLivro
        }
    },
    data() {
        return {
        idLivro: this.$route.params.idLivro
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
    overflow: auto;
    white-space: normal;       
    word-wrap: break-word;     
    overflow-wrap: break-word; 
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
    background-color: rgb(243, 243, 243);
    border-radius: 6px;
}
.imgProduto > img{
    height: 385px;
    border-radius: 6px;
}
.metadados{
    margin-top: 20px;
    width: 500px;
    flex-direction: column;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 130px
}
.quadradosInfos{
    display: flex;
    width: 470px;
    justify-content: space-between;
    background-color: rgb(9, 1, 1);
}
.quadrado{
    height: 60px;
    width: 150px;
    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content: center;
    font-size: 17px;
    border-radius: 6px;
    background-color: rgb(255, 255, 255);
    overflow: hidden;
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
    color: white;
}
.titulo{
    max-height: 100px;
    font-size: 33px;
    overflow: hidden;
}
.avaliacoes{
    height: 35px;
    display: flex;
    align-items: center;
}
.descricao{
    height: 210px;
    padding: 10px;
    border-radius: 5px;
    background-color: #2C2C2C;
    overflow: auto;
    line-height: 1.5;
}
.preco{
    font-size: 34px;
    color: #dee204;
    margin: 5px 0 15px;
    height: 60px;
    display: flex;
    align-items: center;
    overflow: hidden;
}
.botoes{
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.botao{
    display: flex;
    align-items: center;
    justify-content: center;
    color: black;
    width: 49%;
    height: 60px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
    border-radius: 5px;
    overflow: hidden;
    
}
.carrinho{
    background-color: rgb(254, 173, 0);
    color: white;
    font-size: 18px;
}
.carrinho:hover{
    background-color: rgb(203, 139, 0);
    
}
.compra{
    background-color: #4CAF50;
    color: white;
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
}
.compra:hover{
    background-color: #3b913e
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
.avaliacoes {
  display: flex;
  align-items: center;
}
.numero-avaliacoes {
  margin-left: 8px;
  font-size: 16px;
}
</style>