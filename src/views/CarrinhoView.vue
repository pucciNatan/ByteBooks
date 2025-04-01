<template>
    <div class="container">
        <CarrinhoComponent />
    </div>
</template>

<script>
import CarrinhoComponent from '@/components/carrinho/CarrinhoComponent.vue';

export default ({
    components:{ CarrinhoComponent },
    data(){
        return{

        }
    }
})
</script>

<style scoped>
.container{
    display: flex;
    justify-content: center;
}

</style>