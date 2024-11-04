<template>
<div>
  <NavbarComponent/>
  <HomeView/>

</div>

</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
import HomeView from './views/HomeView.vue'

export default {
  components: { NavbarComponent, HomeView }
}
</script>

<style scoped>

</style>