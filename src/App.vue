<template>
<div>
  <NavbarComponent/>
  <div class="container">
    <router-view/>
  </div>
  <RodapeComponent/>

  <button @click="teste">Acessar rota protegida</button>
</div>

</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
import RodapeComponent from './components/RodapeComponent.vue'

export default {
  components: { NavbarComponent, RodapeComponent },

  created(){
    this.$store.dispatch("carregarTokenDoStorage")
    this.$store.dispatch("carregarNomeStorage")
  },
  methods:{
    teste(){
      this.$store.dispatch("visitaRotaProtegida")
    }
  }
}

</script>

<style scoped>
.container{
  margin-top: 60px;
  margin-bottom: 60px;
}
</style>