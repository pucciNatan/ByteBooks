<template>
<div v-if="combo" class="container">
  <div class="cardCombo">
    <div @click="a" class="imgCombo" :alt="'Imagem do combo ' + combo.tituloCombo">
      <img v-for="livro in combo.livros" :key="livro.id" :src="'http://localhost:8000' + livro.img">
    </div>
    <div class="infosCombo">
      <div class="tituloEDesc">
        <div class="tituloCombo">
          {{ combo.tituloCombo }}
        </div>
        <div class="descricaoCombo">
          {{ combo.descricao }}
        </div>
      </div>
      <div class="precoCombo">
        R$ {{ combo.preco }}
      </div>
    </div>
    <button class="botaoComprar">
      <img src="../../imgs/carrinhoDeCompras.png" alt="Carrinho de compras">
      <span>Comprar</span>
    </button>
  </div>
</div>
</template>


<script>
export default {
  props: ['combo'],
};
</script>

<style scoped>
.container{
  display: flex;
  align-content: center;
  justify-content: space-around;
}
.cardCombo{
  transition: transform 0.3s ease;
  font-family: 'Open Sans', sans-serif;
  cursor: pointer;
  width: 260px;
}
.cardCombo:hover{
  transform: scale(1.03);
}
.imgCombo{
  padding: 7px;
  display: flex;
  background-color: #fff;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  position: relative;
  height: 160px;
}
.imgCombo img{
  width: 100px;
  position: absolute;
  transition: transform 0.3s ease, z-index 0.3s ease;
}
.imgCombo img:nth-child(1){
  transform: translateX(-40px) translateY(10px) rotate(-10deg);
  z-index: 1;
}
.imgCombo img:nth-child(2){
  transform: translateX(0px) translateY(-10px) rotate(5deg);
  z-index: 2;
}
.imgCombo img:nth-child(3){
  transform: translateX(40px) translateY(10px) rotate(-5deg);
  z-index: 3;
}
.imgCombo:hover img{
  transform: translateY(0px) scale(1.1);
}
.infosCombo{
  text-align: center;
  background-color: #333333;
  padding: 10px;
  height: 140px;
}
.tituloCombo{
  height: 50px;
  margin-bottom: 6px;
  overflow: hidden;
  font-size: 18px;
  font-weight: bold;
  color: #f1f1f1;
}
.descricaoCombo{
  overflow: hidden;
  height: 50px;
  font-size: 12px;
  margin-bottom: 6px;
  color: #a0a0a0;
}
.precoCombo{
  overflow: hidden;
  font-size: 26px;
  height: 35px;
  font-family: 'Montserrat', sans-serif;
  color: #dee204;
}
.botaoComprar{
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
.botaoComprar:hover{
  background-color: #2d8031;
  cursor: pointer;
}
.botaoComprar > img{
  width: 17px;
}
.botaoComprar > span{
  font-size: 18px;
  margin-left: 6px;
  font-weight: normal;
}
</style>
