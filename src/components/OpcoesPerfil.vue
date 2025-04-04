<template>
    <div class="balaoOpcoes">
        <div class="opcao ponta cima">Meu perfil</div>
        <div class="opcao">Minhas compras</div>
        <div class="opcao ponta baixo" @click="sairDaConta">Sair</div>
    </div>
</template>

<script>
    export default{
        methods:{
            sairDaConta(){
                localStorage.setItem('token', '')
                localStorage.setItem('nomeUsuario', '')
                window.location.replace('/login')
            }
        }
    }
</script>

<style>
    .balaoOpcoes{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        background-color: rgb(40, 40, 40);
        width: 90px;
        height: 110px;
        border-radius: 10px;
        color: rgb(248, 248, 248);
    }
    .opcao{
        text-align: center;
        padding: 3px;
        cursor: pointer;
        width: 95%;
        font-size: 15px;
        transition: 0.3s;
        transform: scale(1.02);
    }
    .opcao:hover{
        background-color: rgb(51, 51, 51);
    }
    .ponta{
        border-radius: 10px;
    }
    .cima{
        padding-top: 6px;
    }
    .baixo{
        padding-bottom: 6px;
    }
</style>