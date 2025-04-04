<template>
    <div class="containerCarrinho">

        <div class="tituloPrincipal">Carrinho de Compras</div>

        <div class="ladoDireitoEsquerdo">
            <div class="ladoEsquerdo">
                <div class="listaItensCarrinho" v-if="itensCarrinho.length">
                    <div class="itemCarrinho" v-for="(item, indice) in itensCarrinho" :key="indice" >
                        <div class="informacoesItem">
                            <img class="imagemItem" :src="'http://localhost:8000' + item.img" :alt="'Capa do livro ' + item.titulo" />
                            <div class="detalhesItem">
                                <div class="nomeItem">{{ item.titulo }}</div>
                                <p class="precoItem">R$ {{ item.preco }}</p>
                            </div>
                        </div>
                        <div class="acoesItem">
                            <div class="quantidadeControle">
                                <button class="botaoDiminuir" @click="diminuirQuantidade()">−</button>
                                <input class="quantidadeItem" type="text" :value="quantidade"/>
                                <button class="botaoAumentar" @click="aumentarQuantidade()">+</button>
                            </div>
                            <button class="botaoRemover" @click="removerItem(indice, item.id)">Remover</button>
                        </div>
                    </div>
                </div>
                <div class="carrinhoVazio" v-else><p>Não há itens no carrinho.</p></div>
            </div>

            <div class="ladoDireito" v-if="itensCarrinho.length" >
                <div class="resumoCarrinho">
                    <p class="textoResumo">Total: <strong>R$ {{ totalCarrinho }}</strong></p>
                    <div class="cupomDesconto">
                        <input class="campoCupom" type="text" placeholder="Insira seu cupom" v-model="cupomDesconto" />
                        <button class="botaoAplicarCupom" @click="aplicarCupom">Aplicar</button>
                    </div>
                    <button class="botaoFinalizar" @click="finalizarCompra">Finalizar Compra</button>
                </div>
            </div>
        </div>
        

    </div>
</template>

<script>
export default ({
    created(){
        this.$store.dispatch('carregarItensCarrinho');
    },
    data() {
        return {
            cupomDesconto: ''
        }
    },
    computed: {
        totalCarrinho() {
            return this.itensCarrinho.reduce((acumulador, item) => acumulador + item.preco * item.quantidade, 0)
        },
        itensCarrinho(){
            return this.$store.getters.getItensCarrinho
        },
        quantidade(){
            return 0
        }
    },
    methods: {
        aumentarQuantidade() {
            this.quantidade++
        },
        diminuirQuantidade() {
            if (this.quantidade > 1) {
                this.quantidade--
            }
        },
        removerItem(indice, id) {
            this.$store.dispatch('removerLivroDoCarrinho', id)
            this.itensCarrinho.splice(indice, 1)
        },
        aplicarCupom() {
            alert(this.cupomDesconto ? `Cupom "${this.cupomDesconto}" aplicado!` : 'Digite um cupom primeiro!')
        },
        finalizarCompra() {
            alert('Compra finalizada! Obrigado por escolher ByteBooks.')
        }
    }
})
</script>

<style scoped>
.containerCarrinho {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90%;
    margin: 0 auto;
    font-family: 'Roboto', sans-serif;
    min-height: calc(100vh - 200px);
    color: #e5e5e5;
}

.tituloPrincipal {
    font-size: 2rem;
    font-weight: 600;
    margin-bottom: 2rem;
    text-align: center;
}

.ladoDireitoEsquerdo{
    display: flex;
    justify-content: space-around;
    width: 90%;
}

.ladoEsquerdo, .ladoDireito {
    background-color: #2f2f2f;
    border-radius: 10px;
    padding: 1rem;
}

.ladoEsquerdo { 
    width: 65%; 
    margin-right: 2%; 
}

.ladoDireito { 
    padding-right: 25px;
    width: 20%; 
    height: fit-content; 
}

.containerCarrinho > .ladoEsquerdo, .containerCarrinho > .ladoDireito {
    display: inline-block;
    vertical-align: top;
}

.listaItensCarrinho {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    height: 50vh;
    padding-right: 5px;
    overflow-y: scroll;
}

.itemCarrinho {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #3a3a3a;
    padding: 1rem;
    border-radius: 8px;
}

.informacoesItem {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.informacoesItem > img{
    width: 70px;
}
.imagemItem {
    object-fit: cover;
    border-radius: 4px;
}

.detalhesItem {
    display: flex;
    flex-direction: column;
}

.nomeItem {
    margin: 0;
    font-size: 1.2rem;
}

.precoItem {
    margin: 0.2rem 0 0;
    font-weight: 500;
}

.acoesItem {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.quantidadeControle {
    display: flex;
    align-items: center;
    gap: 4px;
}

.quantidadeItem {
    width: 50px;
    padding: 0.3rem;
    border: 1px solid #444;
    border-radius: 4px;
    background-color: #2f2f2f;
    color: #fff;
    text-align: center;
}

.botaoDiminuir, .botaoAumentar {
    background-color: #444;
    border: none;
    color: #fff;
    font-size: 1.1rem;
    width: 30px;
    height: 30px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.botaoDiminuir:hover, .botaoAumentar:hover {
    background-color: #555;
}

.botaoRemover {
    background-color: #d9534f;
    color: #fff;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: 0.3s;
}

.botaoRemover:hover {
    background-color: #c9302c;
}

.carrinhoVazio {
    text-align: center;
    font-style: italic;
    opacity: 0.8;
}

.resumoCarrinho {
    text-align: left;
}

.textoResumo {
    font-size: 1.2rem;
    margin-bottom: 1rem;
}

.cupomDesconto {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 1rem;
}

.campoCupom {
    flex: 1;
    border: 1px solid #444;
    border-radius: 4px;
    background-color: #121212;
    color: #fff;
    padding: 0.5rem;
}

.botaoAplicarCupom {
    background-color: #444;
    border: none;
    border-radius: 4px;
    color: #fff;
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: background-color 0.3s;
}

.botaoAplicarCupom:hover {
    background-color: #555;
}

.botaoFinalizar {
    transition: 0.3s;
    background-color: #28a745;
    color: #fff;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
}

.botaoFinalizar:hover {
    background-color: #218838;
}

.listaItensCarrinho::-webkit-scrollbar {
  width: 6px;               /* Largura da barra */
}

.listaItensCarrinho::-webkit-scrollbar-track {
  background: #2f2f2f;      /* Cor do "trilho" */
}

.listaItensCarrinho::-webkit-scrollbar-thumb {
  background-color: #444;   /* Cor do "thumb" */
  border-radius: 4px;       /* Bordas arredondadas */
}

.listaItensCarrinho::-webkit-scrollbar-thumb:hover {
  background-color: #555;   /* Ao passar o mouse */
}

.listaItensCarrinho {
  scrollbar-width: thin;            /* Deixa mais fino */
  scroll-margin-right: 10px;
  scrollbar-color: #444 #2f2f2f;    /* thumb | track */
}

</style>
