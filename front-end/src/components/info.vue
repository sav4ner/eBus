<template>
  <div class="info">
      
        <img :src="require('../assets/logo.png')" alt="Sav4ner" class="logo">
      <i class="fa fa-phone" aria-hidden="true"> +254745673444</i>
      <i class="fa fa-envelope" aria-hidden="true"> info@tukonect.com</i>
      <nav class="navbar">
          
          <hr>
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/booking">Manage Booking</router-link>
        <router-link to="/cancellation">Cancellation</router-link>
        <!-- <router-link to="/contact">Contact Us</router-link> -->
      </nav>

    <div v-if='!$store.state.isAuthenticated'>
      <div class="sign">
         <router-link to="/login"><i class="fa fa-user" aria-hidden="true"> Login / SignUp
        </i></router-link>
      </div>
    </div>
    <div class='sign' v-if="$store.state.isAuthenticated">
      <b>{{user}}</b>
    </div>
    
  </div>
    <br>  
    <hr style="color:white;">
    
  
</template>

<script>
export default {
  data() {
    return {
      loged: localStorage.getItem('token'),
      user: localStorage.getItem('username')
    }
  },
}

</script>

<style lang='scss' scoped>
    .info{
        width: 100%;
        top: 0;
        position: absolute;        
        height: 60px;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        background: rgb(25, 24, 68);
        color: antiquewhite;
        display: inline-flex;
        flex-direction: row;
        vertical-align: middle;
        justify-content: space-between;
        padding-top: 25px;
        margin-left: -50%;
        z-index: 2;
        i{
            vertical-align: middle;
            padding-left: 5px;
        }

        .sign{
            float: right;
            // margin-left: ;
            margin-right: 10px;
            vertical-align: middle;
            display: inline-flex                                                                                                                                                                                                                                                                                            ;
            flex-direction: row;
            color:white;
            margin-top: -5px;
             i{
            vertical-align: middle;
        }
        a{
            color: azure;
            text-decoration: none;
        }
        a:hover{
            color: #42b983;
        }
        a:active{
            color: #42b983;                     
        }

        }   
        .logo{
            
            scale: 47px;
            vertical-align: middle;
            margin-top: -10px;

        }  
        .navbar{
            justify-content: space-between;
            // margin: 0 10%;
            margin-top: -15px;
            margin-left: 1%;
            
            /* position: absolute; */

            a{
                text-decoration: none;
                padding: 0 20px;
            }
            a:active{
                // color: #42b983;
                color: #42b983;
            }
            a:hover{
                // color: #42b983;
                color: #42b983;
            }
        }
.navbar {
  // padding: 30px;

  a {
    font-weight: bold;
    //color: #2c3e50;
    color: azure;

    &.router-link-exact-active {
      color: #42b983;
    }

    &.router-link-exact-hover {
      color: #42b983;
    }
  }
  a:active{
                // color: #42b983;
               color: #42b983;
            }
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    }
</style>