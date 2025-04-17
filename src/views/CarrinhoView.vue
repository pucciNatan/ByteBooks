<template>
    <div class="container">
        <CarrinhoComponent />
    </div>
</template>

<script>
import CarrinhoComponent from '@/components/carrinho/CarrinhoComponent.vue';

export default ({
    components:{ CarrinhoComponent },
    created(){
        this.$store.dispatch('visitaRotaProtegida')
    },
})
</script>

<style scoped>
.container{
    display: flex;
    justify-content: center;
}

</style>