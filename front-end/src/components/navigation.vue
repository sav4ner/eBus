<template>
  <div class="sticky" style="
    position: fixed;
    z-index:1;
    width: 100%;
">
      <info/>
      <br><br>
      
    
  </div>
</template>

<script>
import info from './info.vue'
export default {
  name: 'navigation',
  components: {
      info,
  },
  props: {
    msg: String
  }
}

  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss' scoped>

.na{
  position: fixed;
  top:0;
  width: 100%;
  display: inline-flex;
  flex-direction: column;
  margin-left: -800px;
  background: rgb(25, 24, 68);
}
.navbar{
  justify-content: space-between;
  margin: 0 10%;
  margin-left: 40%;
  
   /* position: absolute; */

  a{
    text-decoration: none;
  }
  a:active{
    color: #42b983;
  }
  a:hover{
    color: #42b983;
  }
}
.navbar {
  // padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }

    &.router-link-exact-hover {
      color: #42b983;
    }
  }
}


</style>
