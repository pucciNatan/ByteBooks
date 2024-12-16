<template>
<div>
  <NavbarComponent/>
  <router-view />
  <RodapeComponent/>
</div>

</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
import RodapeComponent from './components/RodapeComponent.vue'

export default {
  components: { NavbarComponent, RodapeComponent }
}
</script>

<style scoped>

</style>