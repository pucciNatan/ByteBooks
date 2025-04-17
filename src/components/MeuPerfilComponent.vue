<template>
    <div class="containerFilho">
        <div class="iconePerfil">
            {{ this.inicialUsuario }}
        </div>

        <div class="campoGrande">
            <label>Username</label>
            <input type="text" v-model="infosUsuario.username">
        </div>

        <div class="campoMetade">
            <input type="text" placeholder="Nome" v-model="infosUsuario.first_name">
            <input type="text" placeholder="Sobrenome" v-model="infosUsuario.last_name">
        </div>

        <div class="dataNascimento">
          <label>Data de nascimento:</label>
          <div class="data">
            <select class="input" aria-label="Dia" v-model="diaNascimento" required>
              <option v-for="dia in 31" :key="dia" :value="dia">{{ dia }}</option>
            </select>
            <select class="input" aria-label="Mês" v-model="mesNascimento" required>
              <option 
                v-for="(nomeMes, index) in meses" :key="index" :value="index < 9 ? '0' + (index+1) : (index+1)">
                {{ nomeMes }}
              </option>
            </select>
            <select  class="input" aria-label="Ano" v-model="anoNascimento" required>
              <option v-for="ano in 100" :key="ano" :value="2024 - ano">{{ 2024 - ano }}</option>
            </select>
          </div>
        </div>

        <div class="campoGrande">
            <label>Email</label>
            <input type="text" v-model="infosUsuario.email">
        </div>

        <div class="campoMetade">
            <input type="text" placeholder="Nova senha">
            <input type="text" placeholder="Repetir nova senha">
        </div>

        <div class="btnSalvar">
            Salvar
        </div>

    </div>
</template>

<script>
    export default{
        computed:{
            inicialUsuario() {
                return this.infosUsuario.username.charAt(0).toUpperCase()
            },
            infosUsuario(){
                return this.$store.getters.getInfosUsuario
            }
        },
        created(){
            this.$store.dispatch('getCliente')
        }
    }
</script>

<style scoped>
    .containerFilho{
        background-color: rgb(7, 7, 7);
        border: 2px solid rgba(0, 0, 255, 0.5);
        box-shadow:
            0 0 2px  rgba(0, 0, 255, 0.80),
            0 0 6px  rgba(0, 0, 255, 0.60), 
            0 0 12px rgba(0, 0, 255, 0.40),
            0 0 24px rgba(0, 0, 255, 0.20); 
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        margin-top: 50px;
        height: 500px;
        width: 350px;
        color: white;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    .iconePerfil{
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        background-color: blue;
        height: 70px;
        width: 70px;
        border-radius: 50px;
    }
    .campoGrande{
        width: 85%; 
        display: flex; 
        flex-direction: column; 
    }
    .campoGrande > input{
        height: 30px;
        border-radius: 8px;
        border: none;
    }
    
    .campoMetade{
        display: flex;
        width: 85%;
        gap: 20px;
    }
    .campoMetade > input{
        width: 50%;
        height: 30px;
        border-radius: 8px;
        border: none;
    }
    input{
        padding-left: 8px;
    }
    label{
        margin-bottom: 5px;
    }
    .dataNascimento{
        display: flex;
        flex-direction: column;
        width: 85%;
    }
    .data{
        display: flex;
        justify-content: space-between;
    }
    .input{
        width: 32%;
        height: 30px;
        border-radius: 8px;
        border: none;
    }
    .btnSalvar{
        text-align: center;
        background-color: rgb(0, 185, 9);
        color: white;
        padding: 10px;
        border-radius: 8px;
        width: 80%;
        transition: 0.2s;
    }
    .btnSalvar:hover{
        background-color: rgb(0, 165, 8);
        cursor: pointer;
    }

</style>