<template>
    <div class="main">
        <p class="pesquisandoPor">Seus livros:</p>
        <div class="livrosEncontrados" v-if="livros.length > 0">
            <div v-for="item in livros" :key="item.id" class="livroEncontrado">
              <LivroCard :livro="item" comprado="true"/>
            </div>
        </div>
        <div v-else class="naoHaLivros">
            Você ainda não comprou livros =(
        </div>
    </div>
    </template>

<script>
import LivroCard from '../components/Livros/LivroCard.vue'
export default{
    components:{
        LivroCard
    },
    created(){
        this.$store.dispatch('getCliente');
    },
    computed:{
        livros(){
            return this.$store.getters.getLivrosComprados;
        }
    },
}
</script>

<style scoped>
    .main{
        font-family: 'Roboto', sans-serif;
        width: 90%;
        margin: 30px auto;
        min-height: 600px;
    }
    .pesquisandoPor{
        margin-top: 50px;
        color: white;
        font-size: 30px;
        margin-bottom: 30px;
    }
    .livrosEncontrados{
        display: grid;
        gap: 50px;                            
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    }
    .livroEncontrado{
        margin-bottom: 25px;
    }
    .naoHaLivros{
        font-size: 20px;
        color: rgba(242, 242, 242, 0.9);
    }
</style>
