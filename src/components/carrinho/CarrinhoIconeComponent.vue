<template>
    <div class="carrinhoDeCompras">
        <div class="notificacoes">
            {{numItensCarrinho}}
        </div>
        <img src="../../imgs/carrinho.png" alt="Carrinho de compras">
    </div>
</template>

<script>
export default ({
    data(){
        return{
            numItensCarrinho:1
        }
    },
    computed:{

    },
    methods:{
        
    }
})
</script>

<style scoped>
.carrinhoDeCompras{
    position: relative;
    transition: 0.3s ease;
}

.carrinhoDeCompras:hover {
    transform: scale(1.05);
    cursor: pointer;
}

.carrinhoDeCompras > img{
    width: 30px;
}

.notificacoes{
    position: absolute;
    left: 25px;
    bottom: 25px;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    font-size: 13px;
    display: flex;
    align-items: center;
    color: black;
    justify-content: center;
    background-color: rgb(255, 255, 255);
    height: 20px;
    width: 20px;
    border-radius: 50%;
}
</style>