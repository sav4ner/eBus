<template>
  <div class="row">
 <svg xmlns="http://www.w3.org/2000/svg" viewBox=" 0 120 1440 190">
  <path fill="rgb(25, 24, 68)" fill-opacity="1" d="M0,320L1440,224L1440,0L0,0Z"></path>
</svg>
    <div class="col-md-3">
      <h2><b>ABOUT US</b></h2>
      Picaso busses is a transport company that allows users to book their buses online at their own convenience. It makes it easy to book, pay, or cancell a ticket. We are located at the cbd opposite to the Afya Center
        <br><br><br><br>
      <div class="d-grid gap-2 d-md-flex justify-content-md-end">
  <button class="btn btn-primary me-md-2" type="button"><a href="/" style="color: azure; text-decoration: none;">Learn More</a></button>
  
</div>
    </div>
    <div class="col-md-8">
      <video :src="require('../assets/about1.mp4')"></video>
    </div>
  
  </div>
</template>

<script>


export default ({
 name: 'About'
})
</script>

<style lang="scss" scoped>
  .row{
    padding-top:-45px ;
    height: 100vh;
    margin-bottom: 200px;
    // width: 102%;
  .col-md-3{
    margin-top: -70px;
    margin-left: 25px;
    color: rgb(60, 62, 63);
    font-weight: bold;
    font-size: 18px;
    
    h2{
      padding-bottom: 10px;
      color: azure;
      font-size: 36px;
      font-weight: bolder;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .col-md-8{
      margin-top: -300px;
      height: 90%;
    }
  }
  }
</style>