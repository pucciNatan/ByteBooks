<template>
    <div class="card">
        <h2>Criar uma conta</h2>
        <div class="input-group">
            <label>Username:</label>
            <input type="text" placeholder="Ex: exemploDaSilva123">
        </div>

        <div class="nomeSobrenome">
            <input type="text" placeholder="Nome">
            <input type="text" placeholder="Sobrenome">
        </div>

        <div class="input-group">
            <label>Data de nascimento:</label>
            <div class="data-nascimento">
                <select class="select" aria-label="Dia">
                    <option value="">Dia</option>
                    <option v-for="dia in 31" :key="dia" :value="dia">{{ dia }}</option>
                </select>
                <select class="select" aria-label="Mês">
                    <option value="">Mês</option>
                    <option v-for="mes in 12" :key="mes" :value="mes">{{ mes }}</option>
                </select>
                <select class="select" aria-label="Ano">
                    <option value="">Ano</option>
                    <option v-for="ano in 100" :key="ano" :value="2024 - ano">{{ 2024 - ano }}</option>
                </select>
            </div>
        </div>

        <div class="input-group">
            <input type="email" placeholder="Email">
        </div>

        <div class="input-group">
            <input type="password" placeholder="Senha">
        </div>

        <div class="input-group">
            <input type="password" placeholder="Repetir senha">
        </div>

        <button class="register-button">Cadastrar-se</button>
        <a href="">Já tem uma conta?</a>
    </div>
</template>


<style scoped>
    .card{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 40px auto;
        width: 350px;
        font-family: 'Montserrat', sans-serif;
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        gap: 20px;
    }
    h2{
        color: rgb(17, 17, 17);
        font-size: 28px;
    }
    .nomeSobrenome,
    .input-group{
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .nomeSobrenome{
        flex-direction: row;
        gap: 10px;
    }
    .data-nascimento{
        display: flex;
        flex-direction: row;
        gap: 10px;
        align-items: center;
    }
    input,
    .select{
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        width: 100%;
        box-sizing: border-box;
    }
    .radio-group{
        display: flex;
        gap: 15px;
        align-items: center;
        justify-content: space-between;
    }
    input[type="radio"]{
        width: 16px;
        height: 16px;
        margin-right: 5px;
        accent-color: #4CAF50;
    }
    label{
        font-size: 14px;
        display: flex;
        align-items: center;
    }
    .register-button{
        background-color: #0f0f0f;
        color: white;
        border: none;
        padding: 12px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }
    .register-button:hover{
        background-color: #1f1f1f;
    }
    a{
        text-decoration: none;
        color: rgb(0, 65, 139);
    }
</style>

