<template>
  <div class="main">
    <div class="todosLivros">
      <div class="titulo">Acabaram de chegar</div>
      <hr>
      <a href="" class="verMais">Ver todos</a>
      <section>
        <CarroselComponent/>
      </section>
    </div>
  </div>
</template>

<script>
import CarroselComponent from '../components/CarroselComponent.vue'

export default {
  components: {CarroselComponent},
}

</script>

<style scoped>
  .main{
    margin: auto;
    display: flex;
    flex-direction: column;
    justify-content: start;
    height: 1000px;
    width: 90%;
  }
  .todosLivros{
    margin-top: 70px;
  }

  .todosLivros > section{
    margin-top: 40px;
  }
  .titulo{
    display: inline-block;
    color: white;
    font-family: 'Roboto', sans-serif;
    font-size: 30px;
  }
  .verMais{
    color: white;
    font-family: 'Roboto', sans-serif;
    margin-top: 10px;
    display: inline-block;
  }
</style>