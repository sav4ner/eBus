<template>
  <div class="amenities">
      <div class="mid">
          <img :src="require('../assets/bus.jpeg')" alt="" class="img">
          <div class="first">
              <h2><center>Amenities</center></h2>
              We offer several amenities witj us. This icludes free wifi for those with smart-phones, water bottle to quench your thirst along the way, charger points, news paper to keep you occupied and facial tissues. Hope you will enjoy the journey with us.
          </div>
          <div class="second">
            <button type="button" class="btn btn-default btn-circle btn-xl"><i class="fa fa-wifi" aria-hidden="true">Wifi</i></button>
            <button type="button" class="btn btn-default btn-circle btn-xl"><i class="fa fa-tint" aria-hidden="true">Water</i></button>
            <button type="button" class="btn btn-default btn-circle btn-xl"><i class="fa fa-plug" aria-hidden="true">Charge</i></button>
            <button type="button" class="btn btn-default btn-circle btn-xl"><i class="fa fa-newspaper-o" aria-hidden="true">NewsPaper</i></button>
            <button type="button" class="btn btn-default btn-circle btn-xl"><i class="fa fa-pied-piper-pp" aria-hidden="true">FacialPaper</i></button>
            <button type="button" class="btn btn-default btn-circle btn-xl"><i class="fa fa-plus" aria-hidden="true">Safety</i>
</button>
          </div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang='scss' scoped>
.btn-circle.btn-xl {
  width: 70px;
  height: 70px;
  padding: 10px 16px;
  font-size: 24px;
  line-height: 1.33;
  border-radius: 35px;
}
.img{
    margin-top: -160px;
    width: 30%;
    height: auto;
    align-self: center;
}
.mid{
    background: #cbd0d6;
    width: 100%;
    height: 70%;
    margin-top: 10%;
    margin-bottom: 10%;
    color: rgb(20, 20, 20);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: inline-flex;
    flex-direction: column;
    justify-content: space-around;
}
.amenities{
    height: 100vh;

}
.first{
    align-self: left;
    width: 30%;
    padding-left: 15px;
    margin-top: -340px;
}
.second{
    display: inline-flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 10px;
    button{
        padding: 0 5px;
    }
}
</style>