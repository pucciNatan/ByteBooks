<template>
    <div class="star-rating">
      <span
        v-for="n in 5"
        :key="n"
        class="star"
        :class="{
          'star-filled': n <= filledStars,
          'star-half': n === halfStarPosition
        }"
      >
        ★
      </span>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StarRating',
    props: {
      rating: {
        type: Number,
        default: 0
      }
    },
    computed: {
      filledStars() {
        return Math.floor(this.rating);
      },
      halfStarPosition() {
        const decimal = this.rating - Math.floor(this.rating);
        return decimal >= 0.5 && decimal < 1 ? Math.ceil(this.rating) : -1;
      }
    }
  };
  </script>
  
  <style scoped>
  .star-rating {
    display: flex;
    flex-direction: row;
  }
  
  .star {
    font-size: 24px;
    color: #bbb;
    margin-right: 4px;
    position: relative;
  }
  
  .star-filled {
    color: gold;
  }
  
  .star-half {
    color: gold;
    overflow: hidden;
    display: inline-block;
    width: 12px;
  }
  </style>
  