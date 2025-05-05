<template>
    <div class="navbar">
        <router-link to="/">
            <div class="logo">
                <img src="../imgs/logoComNome.png" alt="Logo Bytebooks">
            </div>
        </router-link>
        <ul class="listaItens">
            <router-link to="/categorias/lancamentos" class="rotasNavbar lancamentos"> 
                <div class="item">
                    <img src="../imgs/lancamentosNormal.png" alt="ícone de um foguete" class="fogueteImg normal">
                    <img src="../imgs/lancamentosSelecionado.png" alt="ícone de foguete azul" class="fogueteImg hover">
                    <li>Lançamentos</li> 
                </div>
            </router-link>
            <router-link to="/categorias/dados" class="rotasNavbar ofertas"> 
                <div class="item">
                    <img src="../imgs/dadosNormal.png" alt="Ícone de dados" class="dadosImg normal">
                    <img src="../imgs/dadosSelecionado.png" alt="Ícone de dados amarelo" class="dadosImg hover">
                    <li>Dados</li> 
                </div>
            </router-link>
            <router-link to="/categorias/backend" class="rotasNavbar backend"> 
                <div class="item">
                    <img src="../imgs/backendNormal.png" alt="ícone de código" class="backendImg normal">
                    <img src="../imgs/backendSelecionado.png" alt="ícone de código vermelho" class="backendImg hover">
                    <li>Backend</li> 
                </div>
            </router-link>
            <router-link to="/categorias/software" class="rotasNavbar frontend"> 
                <div class="item">
                    <img src="../imgs/frontendNormal.png" alt="Ícone de um PC" class="frontendImg normal">
                    <img src="../imgs/frontendSelecionado.png" alt="Ícone de PC verde" class="frontendImg hover">
                    <li>Software</li> 
                </div>
            </router-link>
        </ul>
        
        <div class="barraPesquisa">
            <input v-model="pesquisa" type="text" @keyup.enter="pesquisar" placeholder="Buscar livros...">
            <button @click="pesquisar" @keydown="pesquisar">
                <img src="../imgs/lupa.png" alt="Lupa">
            </button>
        </div>
        <router-link to="/carrinho" v-if="isAuthenticated">
            <div class="carrinho">
                <CarrinhoIconeComponent />
            </div>
        </router-link>
        <router-link to="/meuPerfil" v-if="isAuthenticated" class="rota"> 
            <div class="avatar-wrapper logadoDeslogado" :style="{backgroundColor: avatarColor}">
                {{ inicialUsuario }}
                <OpcoesPerfil class="opcoes"/>
            </div>
        </router-link>
        
        <div v-else class="entrar">
            <router-link to="/login" class="cadastroELogin">
                <div class="botaoEntrar">
                    Entrar
                    <img src="../imgs/userIcon.png" alt="">
                </div>
            </router-link>
        </div>
    </div>
</template>

<script>
import CarrinhoIconeComponent from './carrinho/CarrinhoIconeComponent.vue'
import OpcoesPerfil from './OpcoesPerfil.vue'

export default ({
    components:{ CarrinhoIconeComponent, OpcoesPerfil},
    data() {
      return {
        pesquisa: ''
      }
    },
    computed: {
      isAuthenticated() {
        return this.$store.getters.getToken !== ''
      },
      nomeUsuario() {
        return this.$store.getters.getNomeUsuario || ''
      },
      inicialUsuario() {
        return this.nomeUsuario.charAt(0).toUpperCase()
      },
      avatarColor() {
        const colors = ['blue', 'green', 'red', 'purple', 'orange']
        const index = this.inicialUsuario.charCodeAt(0) % colors.length
        this.$store.dispatch("corAvatar" , colors[index]);
        return colors[index]
      }
    },
    methods: {
      pesquisar() {
        if (this.pesquisa == ''){
            return
        }
        this.$router.push({ path: `/pesquisa/${this.pesquisa}` });
        this.pesquisa = ''
      }
    }
  })
  </script>

<style scoped>
    .rota{
        text-decoration: none;
    }
    .logo > img {
        width: 130px;
        transition: transform 0.3s ease;
    }

    .logo:hover > img {
        transform: scale(1.05);
    }
    
    .navbar {
        position: fixed;
        display: flex;
        align-items: center;
        justify-content: space-around;
        background-color: rgb(3, 1, 10);  
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2), 0 2px 6px rgba(0, 0, 0, 0.3);
        width: 100%;
        height: 80px;
        color: white;
        font-family: 'Roboto', sans-serif;
        z-index: 1000;
    }


    .rotasNavbar {
        position: relative;
        text-decoration: none;
        color: white;
        display: flex;
        width: 100%;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .rotasNavbar:hover::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 3px;
    }
    .rotasNavbar.lancamentos:hover::after {
        background-color: #2c07ff;
    }
    .rotasNavbar.ofertas:hover::after {
        background-color: #ffee07;
    }
    .rotasNavbar.backend:hover::after {
        background-color: #ff3460;
    }
    .rotasNavbar.frontend:hover::after {
        background-color: #07ff28;
    }

    .item .hover {
        display: none;
    }

    .rotasNavbar:hover .normal {
        display: none;
    }

    .rotasNavbar:hover .hover {
        display: inline;
    }

    .listaItens {
        display: flex;
        align-items: center;
        list-style: none;
        font-size: 20px;
        height: 100%;
        width: 50%;
    }

    .item {
        display: flex;
        align-items: center;
        cursor: pointer;
    }

    .item > img {
        width: 40px;
    }

    .barraPesquisa {
        display: flex;
        padding: 3px;
        justify-content: space-around;
        background-color: rgb(255, 255, 255); 
        border-radius: 10px;
        width: 200px;
    }

    .barraPesquisa > input {
        border: none;
        outline: none;
    }

    button {
        border: none;
        background: transparent;
        cursor: pointer;
    }

    button > img {
        width: 20px;
    }

    .logadoDeslogado {
        position: relative;
    }

    .opcoes {
        position: absolute;
        right: 0px;
        top: 50px;
        font-weight: normal;
        visibility: hidden;
        opacity: 0;
        transition: visibility 0.1s, opacity 0.1s ease;
    }

    /* Quando o mouse estiver sobre o container pai */
    .logadoDeslogado:hover .opcoes {
        visibility: visible;
        opacity: 1;
    }

    .cadastroELogin {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        position: relative;
        text-decoration: none;
    }

    .entrar{
        height: 100%;
    }

    .avatar-wrapper {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        font-weight: bold;
        cursor: pointer;
    }

    .cadastroELogin:hover::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background-color: #d600d6;
    }

    .botaoEntrar {
        margin: auto;
        display: flex;
        align-items: center;
        justify-content: space-around;
        width: 80px;
        color: rgb(4, 0, 20);  
        border-radius: 10px;
        padding: 5px;
        background-color: rgb(255, 255, 255);
        transition: color 0.3s ease;
    }

    .botaoEntrar > img {
        width: 20px;
    }

    .item > img.dadosImg {
        width: 24px;
        height: auto;
        margin-right: 6px;
    }    
    
    .item > img.backendImg {
        margin-right: 3px;
    }
    

</style>
