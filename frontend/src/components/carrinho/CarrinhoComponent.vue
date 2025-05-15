<template>
    <div class="containerCarrinho">

        <div class="tituloPrincipal">Carrinho de Compras</div>

        <div class="ladoDireitoEsquerdo">
            <div class="ladoEsquerdo">
                <div class="listaItensCarrinho" v-if="itensCarrinho.length">
                    <div class="itemCarrinho" v-for="(item, indice) in itensCarrinho" :key="indice">
                        <div class="informacoesItem">
                            <img class="imagemItem" :src="'http://127.0.0.1:8000' + item.livro.img" :alt="'Capa do livro ' + item.livro.titulo" />
                            <div class="detalhesItem">
                                <div class="nomeItem">{{ item.livro.titulo }}</div>
                                <p class="precoItem">R$ {{ item.livro.preco }}</p>
                            </div>
                        </div>
                        <div class="acoesItem">
                            <div class="quantidadeControle">
                                <button class="botaoDiminuir" @click="diminuirQuantidade(item)">
                                    <div v-if="item.quantidade > 1">-</div>
                                    <div v-else>
                                        <img src="../../imgs/lixeira.svg" alt="ícone lixeira" style="width: 20px; margin-top: 4px;">
                                    </div>
                                </button>
                                <input class="quantidadeItem" type="text" :value="item.quantidade" readonly />
                                <button class="botaoAumentar" @click="aumentarQuantidade(item)">+</button>
                            </div>
                            <button class="botaoRemover" @click="removerItem(indice, item.livro.id)">Remover</button>
                        </div>
                    </div>
                </div>
                <div class="carrinhoVazio" v-else><p>Não há itens no carrinho.</p></div>
            </div>

            <div class="ladoDireito" v-if="itensCarrinho.length">
                <div class="resumoCarrinho">
                    <p class="textoResumo">
                        Total:
                        <strong>
                            R$ {{ totalCarrinho }}
                            <span v-if="descontoAplicado">(cupom aplicado)</span>
                        </strong>
                    </p>

                    <div class="cupomDesconto">
                        <input
                            class="campoCupom"
                            type="text"
                            placeholder="Insira seu cupom"
                            v-model="cupomDesconto"
                            @keyup.enter="aplicarCupom"
                        />
                        <button class="botaoAplicarCupom" @click="aplicarCupom">Aplicar</button>
                    </div>

                    <button class="botaoFinalizar" @click="irParaCompra">Finalizar Compra</button>
                </div>
            </div>
        </div>

        <div v-if="finalizarCompra" class="finalizarCompra">
            <TelaPagamento
                :itens="itensCarrinho"
                :total="Number(totalCarrinho)"
                @confirmarCompra="fecharCompra"
            />
        </div>
    </div>
</template>

<script>
import TelaPagamento from '../TelaPagamento.vue';

export default {
    components: { TelaPagamento },

    created() {
        this.$store.dispatch('carregarItensCarrinho');
    },

    data() {
        return {
            cupomDesconto: '',
            finalizarCompra: false,
            descontoAplicado: 0
        };
    },

    computed: {
        totalCarrinho() {
            const subtotal = this.itensCarrinho.reduce(
                (soma, item) => soma + parseFloat(item.livro.preco) * item.quantidade,
                0
            );
            const totalComDesconto = subtotal * (1 - this.descontoAplicado);
            return totalComDesconto.toFixed(2);
        },
        itensCarrinho() {
            return this.$store.getters.getItensCarrinho;
        }
    },

    methods: {
        aumentarQuantidade(item) {
            this.$store.dispatch('atualizarQuantidade', { idLivro: item.livro.id, adicionar: true });
        },
        diminuirQuantidade(item) {
            this.$store.dispatch('atualizarQuantidade', { idLivro: item.livro.id, adicionar: false });
        },
        removerItem(indice, id) {
            this.$store.dispatch('removerLivroDoCarrinho', id);
            this.itensCarrinho.splice(indice, 1);
        },

        aplicarCupom() {
            const cupons = {
                CUPOM30: 0.30,
                CUPOM50: 0.50,
                CUPOM10: 0.10
            };
            const codigo = this.cupomDesconto.trim().toUpperCase();

            if (codigo in cupons) {
                this.descontoAplicado = cupons[codigo];
            } else {
                this.descontoAplicado = 0;
                alert('Cupom inválido. Tente CUPOM30, CUPOM50 ou CUPOM10.');
            }
        },

        irParaCompra() {
            this.finalizarCompra = true;
        },
        fecharCompra() {
            this.finalizarCompra = false;
        }
    }
};
</script>

<style scoped>
.containerCarrinho {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90%;
    margin: 40px auto;
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
  width: 6px;           
}

.listaItensCarrinho::-webkit-scrollbar-track {
  background: #2f2f2f;     
}

.listaItensCarrinho::-webkit-scrollbar-thumb {
  background-color: #444;  
  border-radius: 4px;      
}

.listaItensCarrinho::-webkit-scrollbar-thumb:hover {
  background-color: #555;  
}

.listaItensCarrinho {
  scrollbar-width: thin;           
  scroll-margin-right: 10px;
  scrollbar-color: #444 #2f2f2f;    
}

.finalizarCompra{
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    background-color: rgb(16, 21, 26, 0.9);
}

@media (max-width: 1024px) {
  .ladoDireitoEsquerdo {
    width: 100%;
    gap: 20px;
  }

  .ladoEsquerdo{
    width: 70%;                 
    margin-right: 0 auto;
  }
  .ladoDireito{
    width: 250px;
  }

  .listaItensCarrinho {
    height: 45vh;              
  }
}

@media (max-width: 765px) {

    .containerCarrinho{
        margin-top: 90px;
    }

  .tituloPrincipal {
    font-size: 1.6rem;
    margin-bottom: 1.5rem;
    width:300px;
  }

  .itemCarrinho {
    flex-direction: column;
    width: 150px;
    align-items: flex-start;
    gap: 12px;
    margin-right: 5px;
  }

  .informacoesItem > img {
    width: 60px;
  }

  .nomeItem {
    font-size: 1rem;
  }

  .precoItem {
    font-size: 0.9rem;
  }

  .acoesItem {
    width: 100%;
    justify-content: space-between;
  }

  .quantidadeItem {
    width: 42px;
  }

  .botaoRemover {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }

  .ladoDireito {
    padding: 1rem;
  }

  .textoResumo {
    font-size: 1rem;
  }

  .botaoFinalizar {
    width: 100%;
    font-size: 0.95rem;
  }
}

@media (max-width: 679px) {
    .ladoDireitoEsquerdo{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 70%;
    }
    .containerCarrinho {
        width: 400px;
        min-width: 400px;
        margin: 50px auto;
    }

    .ladoEsquerdo{
        width: 250px;
        margin-left: 6px;
    }
    .listaItensCarrinho {
        height: 36vh;
        justify-content: center;
        align-items: center;
        max-height: 45vh;
    }

    .informacoesItem {
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
        margin: 1px auto;
    }

    .acoesItem {
        flex-direction: column;
        align-items: center;
        gap: 6px;
    }

  .quantidadeControle {
    gap: 2px;
  }

  .botaoDiminuir,
  .botaoAumentar {
    width: 28px;
    height: 28px;
    font-size: 1rem;
  }

  .botaoRemover {
    width: 70%;
    text-align: center;
  }

  .cupomDesconto {
    flex-direction: column;
    gap: 8px;
  }

  .campoCupom,
  .botaoAplicarCupom {
    width: 100%;
  }
}


</style>
