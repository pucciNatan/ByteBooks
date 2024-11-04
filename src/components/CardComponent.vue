<template>
  <div class="container">
    <button class="cardLivro">
      <div class="imgLivro">
        <img :src="'http://localhost:8000' + livro.img" :alt="'Capa do livro ' + livro.titulo">
      </div>
      <div class="infosLivros">
        <div class="tituloEDesc">
          <div class="tituloLivro">
            {{ livro.titulo }}
          </div>
          <div class="autorLivro">
            {{ livro.autor }}
          </div>
        </div>
        <div class="precoLivro">
          {{ livro.preco }} R$
        </div>
      </div>
      <button class="botaoComprar">
        <img src="../imgs/carrinhoDeCompras.png" alt="Carrinho de compras">
        <h1>Comprar</h1>
      </button>
    </button>
  </div>
</template>

<script>
export default {
  props: ['livro'],
};
</script>

<style scoped>
.container {
  display: flex;
  align-content: center;
  justify-content: space-around;
  height: 350px;
}
.cardLivro {
  width: 190px;
  height: 380px;
  background-color: #2c2c2c;
  color: white;
  font-family: 'Open Sans', sans-serif;
  box-sizing: border-box;
  border: none;
  cursor: pointer;
  border-radius: 8px;
  transition: transform 0.3s ease;
}
.cardLivro:hover {
  transform: scale(1.03);
}
.imgLivro {
  padding: 7px;
  display: flex;
  height: 170px;
  background-color: #fff;
  justify-content: center;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
.imgLivro > img {
  width: 70%;
  border-radius: 4px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}
.infosLivros {
  text-align: center;
  background-color: #333333;
  padding: 10px;
  height: 140px;
}
.tituloLivro {
  height: 50px;
  overflow: hidden;
  font-size: 18px;
  font-weight: bold;
  color: #f1f1f1;
}
.autorLivro {
  overflow: hidden;
  height: 35px;
  font-size: 12px;
  margin-top: 4px;
  color: #a0a0a0;
}
.precoLivro {
  overflow: hidden;
  font-size: 26px;
  height: 40px;
  margin: 10px 0;
  font-family: 'Montserrat', sans-serif;
  color: #e3e700;
}
.botaoComprar {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  background-color: #4CAF50;
  color: white;
  height: 40px;
  border: none;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  transition: background-color 0.3s ease;
}
.botaoComprar:hover {
  background-color: #2d8031;
  cursor: pointer;
}
.botaoComprar > img {
  width: 17px;
}
.botaoComprar > h1 {
  font-size: 18px;
  margin-left: 6px;
  font-weight: normal;
}
</style>
