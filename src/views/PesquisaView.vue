<template>
<div class="main">
    <p class="pesquisandoPor">Pesquisando por - {{ this.livro }}</p>
    <div class="livrosEncontrados">
        <div v-for="item in livros" :key="item.id" class="livroEncontrado">
          <LivroCard :livro="item"/>
        </div>
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
        this.$store.dispatch('pesquisarPorLivro', this.livro);
    },
    computed:{
        livros(){
            return this.$store.getters.getLivrosPesquisados;
        }
    },
    data(){
        return{
            livro: this.$route.params.livro
        }
    }
}
</script>

<style scoped>
    .main{
        width: 90%;
        margin: 30px auto;
        min-height: 600px;
    }
    .pesquisandoPor{
        margin-top: 50px;
        color: white;
        font-size: 30px;
        margin-bottom: 10px;
    }
    .livrosEncontrados{
    display: flex;
    flex-wrap: wrap;
    justify-content: start;
    padding: 20px;
    gap: 56px;
    }
    .livroEncontrado{
        margin-bottom: 25px;
    }
</style>
