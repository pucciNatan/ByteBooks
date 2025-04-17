<template>
    <div class="containerPai">
        <MeuPerfilComponent />
    </div>
</template>

<script>
    import MeuPerfilComponent from '../components/MeuPerfilComponent.vue'

    export default{
        components: {MeuPerfilComponent},
    }
</script>

<style scoped>
    .containerPai{
        font-family: 'Roboto', sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>