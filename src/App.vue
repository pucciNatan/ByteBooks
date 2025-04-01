<template>
  <div id="app">
    <NavbarComponent />
    <div class="conteudoPrincipal">
      <router-view />
    </div>
    <RodapeComponent />
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
}

</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.conteudoPrincipal{
  flex: 1; 
  margin-top: 60px;
  margin-bottom: 100px;
}

</style>