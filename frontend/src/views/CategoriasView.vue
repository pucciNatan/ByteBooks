<template>
    <div class="main">
        <p class="pesquisandoPor">Pesquisando por - {{ props }}</p>
        <div class="livrosEncontrados" v-if="livros.length > 0">
            <div v-for="item in livros" :key="item.id" class="livroEncontrado">
              <LivroCard :livro="item"/>
            </div>
        </div>
        <div v-else class="naoHaLivros">Não há livros para essa pesquisa.</div>
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
        },
        beforeRouteUpdate(to, from, next) {
            const novoLivro = to.params.livro;
            this.livro = novoLivro;
            this.$store.dispatch('pesquisarPorLivro', novoLivro);
            next();
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
        .naoHaLivros{
            font-size: 16px;
            color: rgb(255, 255, 255, 0.9);
        }
    </style>
    