<template>
    <div class="navbar">
        <router-link to="/">
            <div class="logo">
                <img src="../imgs/logoComNome.png" alt="Logo Bytebooks">
            </div>
        </router-link>

        <ul class="listaItens">
            <router-link to="/" class="rotasNavbar lancamentos"> 
                <div class="item">
                    <img src="../imgs/lancamentosNormal.png" alt="ícone de um foguete" class="fogueteImg normal">
                    <img src="../imgs/lancamentosSelecionado.png" alt="ícone de foguete azul" class="fogueteImg hover">
                    <li>Lançamentos</li> 
                </div>
            </router-link>
            <router-link to="/" class="rotasNavbar ofertas"> 
                <div class="item">
                    <img src="../imgs/ofertasNormal.png" alt="Ícone de ofertas" class="ofertasImg normal">
                    <img src="../imgs/ofertasSelecionado.png" alt="Ícone de ofertas amarelo" class="ofertasImg hover">
                    <li>Promoções</li> 
                </div>
            </router-link>
            <router-link to="/" class="rotasNavbar backend"> 
                <div class="item">
                    <img src="../imgs/backendNormal.png" alt="ícone de código" class="backendImg normal">
                    <img src="../imgs/backendSelecionado.png" alt="ícone de código vermelho" class="backendImg hover">
                    <li>Backend</li> 
                </div>
            </router-link>
            <router-link to="/" class="rotasNavbar frontend"> 
                <div class="item">
                    <img src="../imgs/frontendNormal.png" alt="Ícone de um PC" class="frontendImg normal">
                    <img src="../imgs/frontendSelecionado.png" alt="Ícone de PC verde" class="frontendImg hover">
                    <li>Frontend</li> 
                </div>
            </router-link>
        </ul>

        <div class="barraPesquisa">
            <input type="text">
            <button>
                <img src="../imgs/lupa.png" alt="Lupa">
            </button>
        </div>

        <div class="cadastroELogin">
            <router-link to="login" class="botaoEntrar">
                Entrar
                <img src="../imgs/userIcon.png" alt="">
            </router-link>
        </div>
    </div>
</template>

<style scoped>
    .logo > img {
        width: 130px;
        transition: transform 0.3s ease;
    }

    .logo:hover > img {
        transform: scale(1.05);
    }
    
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-around;
        background-color: rgb(3, 1, 10);  
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2), 0 2px 6px rgba(0, 0, 0, 0.3);
        width: 100%;
        height: 80px;
        color: white;
        font-family: 'Roboto', sans-serif;
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

    /* Barra colorida no hover */
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

    /* Efeito para trocar as imagens no hover */
    .item .hover {
        display: none;
    }

    .rotasNavbar:hover .normal {
        display: none; /* Esconde a imagem normal no hover */
    }

    .rotasNavbar:hover .hover {
        display: inline; /* Mostra a imagem "selecionada" no hover */
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

    .cadastroELogin {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        position: relative; /* Necessário para o posicionamento da barra roxa */
    }

    /* Barra roxa no hover do botão "Entrar" */
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
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .botaoEntrar > img {
        width: 20px;
    }
</style>
