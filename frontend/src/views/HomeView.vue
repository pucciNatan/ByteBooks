<template>
  <div class="main">
    <div class="sessao">
      <div class="titulo">Acabaram de chegar</div>
      <hr>
      <a href="" class="verTodos">Ver todos</a>
      <section>
        <CarroselComponent tipo = 'UltimosLancamentosLoja'/>
      </section>
    </div>

    <div class="sessao">
      <div class="titulo">Os mais vendidos</div>
      <hr>
      <a href="" class="verTodos">Ver todos</a>
      <section>
        <CarroselComponent tipo = 'maisVendidos'/>
      </section>
    </div>

    <div class="sessao">
      <div class="titulo">Combos</div>
      <hr>
      <a href="" class="verTodos">Ver todos</a>
      <section>
        <CarroselComponent tipo = 'combos'/>
      </section>
    </div>
  </div>
</template>

<script>
import CarroselComponent from '../components/Livros/CarroselComponent.vue'

export default {
  components: {CarroselComponent},
  created(){
    this.$store.dispatch('carregarItensCarrinho');
  }
}
</script>

<style scoped>
  .main{
    margin: 30px auto;
    display: flex;
    flex-direction: column;
    justify-content: start;
    width: 90%;
  }
  hr{
    border: 1px solid rgba(207, 207, 207, 0.2);
    border-radius: 20px;
  }
  .sessao{
    margin-top: 20px;
  }
  .titulo{
    height: 40px;
    color: white;
    font-family: 'Roboto', sans-serif;
    font-size: 30px;
  }
  .verTodos{
    color: white;
    font-family: 'Roboto', sans-serif;
    margin-top: 10px;
    display: inline-block;
  }
</style>