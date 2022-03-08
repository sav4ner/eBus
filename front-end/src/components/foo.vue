<template>
  <div class="">
      <div class="footer">
        
          <contact/>
        <hr>
      copyyright @ sav4ner 2022
        <br>
        <br>
      </div>
    </div>
</template>

<script>
import contact from '../views/Contact.vue'
export default {
    name: 'Footer',
    components : {
        contact
    }
}
</script>

<style scoped>
.footer{
  width: 100%;
  height: auto;
  bottom: 0;
  position: relative;
  background:rgb(25, 24, 68);
  color:azure;
  font:bolder;
  font-size: 20px;
  text-align: center;
  margin-top: 0;
  
  
}
</style>