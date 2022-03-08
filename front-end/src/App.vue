<template>
  <div id="nav">
     <div class="na">
       <navigation/>
     </div>
      
  </div>
  <router-view />
  <foo/>

</template>
<script>
import axios from 'axios'

import navigation from './components/navigation.vue'
import foo from './components/foo.vue'
export default {
  name: 'app',
  components: {
    navigation,
    foo,

  },
  data() {
    return {
      loged: this.$store.state.isAuthenticated
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    localStorage.setItem('token', '')

    if (token) { 
      axios.defaults.headers.common['Authorization'] = "Token " + token
      
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }
  }

}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  body::-webkit-scrollbar {
  width: 1em;
  }
 
  body::-webkit-scrollbar-track {
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  }
  
  body::-webkit-scrollbar-thumb {
    background-color: darkgrey;
    outline: 1px solid slategrey;
  }
}

</style>
