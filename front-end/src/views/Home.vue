<template>
  <div class="home" :style="cssProps">
    <div class="word">
      <h2><b>Welcome to Picasa Busses. Travel with us around the country</b></h2>
      <br>

        


      <br>
      <br>
      <!-- <h1><center>Wish you a happy and comfortable jouurney</center></h1> -->
    </div>
    <br>
   <!-- <img :src="require('../assets/back.jpeg')" alt=""> -->
    <booking/>
    <!-- <hire/> -->
  </div>
  <amenities/>
  <testimonials/>
</template>

<script>
// @ is an alias to /src

import booking from '../components/booking.vue'
import testimonials from '../components/testimonials.vue'
// import hire from '../components/hire.vue'
import amenities from '../components/amenities.vue'
export default {
  name: "Home",
  components: {
    booking,
    // hire,
    testimonials,
    amenities,
  },
  data() {
    return {
      cssProps: {
          backgroundImage: `url(${require('@/assets/home.jpg')})`
        }
      
    }
  },
};
</script>

<style lang='scss' scoped>
  .home{
    padding-top: 95px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    color: azure;
    .word{
      float: left;
      margin-left: 60%;
      margin-top: 70px;
      color: aliceblue !important;
      width: 20%;
      text-align: left;
      align-items: left;
      font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
      font-size: 24px;
      font-weight: bolder;
      padding-bottom:100px ;
    }
  }
</style>