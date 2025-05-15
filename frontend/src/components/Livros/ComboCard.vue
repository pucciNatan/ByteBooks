<template>
  <div v-if="combo" class="container">
    <router-link :to="'/paginaCombo/' + combo.id" class="routerLink">
      <div class="cardCombo">
        <div class="imgCombo">
          <img
            v-for="livro in combo.livros"
            :key="livro.id"
            :src="'http://127.0.0.1:8000' + livro.img"
            :alt="'Capa do livro ' + livro.titulo"
          />
        </div>

        <div class="infosCombo">
          <div class="tituloEDesc">
            <div class="tituloCombo">{{ combo.tituloCombo }}</div>
            <div class="descricaoCombo">{{ combo.chamadaDesc }}</div>
          </div>
          <div class="precoCombo">R$ {{ combo.preco }}</div>
        </div>

        <button class="botaoComprar">
          <img src="../../imgs/carrinhoDeCompras.png" alt="Carrinho de compras" />
          <span>Comprar</span>
        </button>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: ['combo'],
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}
.cardCombo {
  width: 260px;
  font-family: 'Open Sans', sans-serif;
  cursor: pointer;
  transition: transform 0.3s ease;
}
.cardCombo:hover { transform: scale(1.03); }

.imgCombo {
  position: relative;
  padding: 7px;
  height: 160px;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 8px 8px 0 0;
  overflow: hidden;
}
.imgCombo img {
  width: 100px;
  position: absolute;
  transition: transform 0.3s ease, z-index 0.3s ease;
}
.imgCombo img:nth-child(1) { transform: translate(-40px, 10px) rotate(-10deg); z-index: 1; }
.imgCombo img:nth-child(2) { transform: translate(0, -10px) rotate(5deg);  z-index: 2; }
.imgCombo img:nth-child(3) { transform: translate(40px, 10px) rotate(-5deg); z-index: 3; }
.imgCombo:hover img { transform: translateY(0) scale(1.1); }

.infosCombo{
  background:#333;
  padding:10px;
  height:140px;
  display:flex;
  flex-direction:column;
  justify-content:space-between;
  align-items:center;
}

.tituloCombo    { height: 50px; font-size: 18px; color: #f1f1f1; font-weight: bold; overflow: hidden; }
.descricaoCombo { height: 40px; font-size: 13px; color: #a0a0a0; overflow: hidden; }
.precoCombo     { height: 35px; font-size: 26px; color: #dee204; font-family: 'Montserrat', sans-serif; }

.botaoComprar {
  width: 100%;
  height: 40px;
  background: #4caf50;
  color: #fff;
  border: none;
  border-radius: 0 0 8px 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: background 0.3s ease;
}
.botaoComprar:hover { background: #2d8031; }
.botaoComprar img { width: 17px; }
.botaoComprar span { margin-left: 6px; font-size: 18px; }

.routerLink { text-decoration: none; }

@media (min-width: 481px) and (max-width: 1024px) {
  .cardCombo     { width: 200px; }
  .imgCombo      { height: 130px; }
  .imgCombo img  { width: 80px; }
  .tituloCombo   { font-size: 16px; height: 46px; }
  .descricaoCombo{ font-size: 12px; height: 34px; }
  .precoCombo    { font-size: 22px; }
}

@media (max-width: 480px) {
  .cardCombo     { width: 150px; }
  .imgCombo      { height: 100px; }
  .imgCombo img  { width: 40px; }
  .infosCombo    { padding: 8px; height: 120px; }
  .tituloCombo   { font-size: 14px; height: 40px; }
  .descricaoCombo{ font-size: 11px; height: 28px; }
  .precoCombo    { font-size: 18px; }
  .botaoComprar  { height: 36px; }
  .botaoComprar span { font-size: 16px; }
}
</style>
