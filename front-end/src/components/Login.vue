<template>
  <div class="login">
    <form class="form-signin" @submit.prevent='submitForm'>
  <img class="mb-4" :src="require('../assets/logo.png')" alt=""   >
  <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
  <label for="inputEmail" class="sr-only">username</label>
  <input type="text" id="inputEmail" class="form-control" placeholder="Username" required="" autofocus="" v-model="username">
  <label for="inputPassword" class="sr-only">Password</label>
  <input type="password" id="inputPassword" class="form-control" placeholder="Password" required="" v-model="password">
  <div class="checkbox mb-3">
    <label>
      <input type="checkbox" value="remember-me"> Remember me
    </label>
  </div>
  <a href="/signup" style="float:right; margin-right:240px;">SignIn</a>
  <button class="btn btn-lg btn-primary btn-block" type="submit" style="margin-right:-240px;">Sign in</button>
  <p class="mt-5 mb-3 text-muted">© 2021-202</p>
</form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'login',
    data() {
      return {
        password: '',
        username: '',
      }
    },
    methods: {
      submitForm(){
        
        // const formData = {
        //   username: this.username,
        //   password: this.password 
        // }

        axios.post('/api/v1/token/login',{
    "password": this.password,
    "username": this.username
})
        .then(Response =>{
          console.log('Congrats post succsfully')
          console.log(Response)
          const token = Response.data.auth_token
          const user = localStorage.getItem('username')
          localStorage.setItem('username', this.username)
          this.$store.commit('setToken', token,user)

          axios.defaults.headers.common['Authorization'] = 'Token ' + token
          
          localStorage.setItem('token', token)

          
          this.$router.push("/");
        }).catch(error =>{
          console.log(error)
          console.log('Failed to post')
        })
      }
    },
}
</script>

<style scoped>
  .login{
    padding-top: 135px;
    width: 60%;
    background: aliceblue;
    margin-left: 20%;
    border-radius: 6px;
  }
  #inputPassword{
    width: 50%;
    margin-left: 25%;
  }
  #inputEmail{
    width: 50%;
    margin-left: 25%;
  }
</style>