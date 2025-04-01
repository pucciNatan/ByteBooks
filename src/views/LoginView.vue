<template>
    <div class="container">
        <LoginComponent />
    </div>
</template>

<script>
    import LoginComponent from '../components/LoginCadastro/LoginComponent.vue'

    export default{
        components:{
            LoginComponent
        }
    }
</script>

<style scoped>
.container{
    height: 620px;
}
</style>