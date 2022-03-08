<template>
  <div class="contact">
      <div id="contact" class="footer">
            <div class="container">
               <div class="row pdn-top-30">
                  <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">
                     <ul class="location_icon">
                        <li> <a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
                        <li> <a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
                        <li> <a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
                        <li> <a href="#"><i class="fa fa-instagram" aria-hidden="true"></i></a></li>
                     </ul>
                  </div>
                  <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12">
                     <div class="Follow">
                        <h3>CONTACT US</h3>
                        <span>123 Second Street Fifth <br>Avenue,<br>
                        Manhattan, New York<br>
                        +987 654 3210</span>
                     </div>
                  </div>
                  <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12">
                     <div class="Follow">
                        <h3>ADDITIONAL LINKS</h3>
                        <ul class="link">
                           <li> <a href="#">About us</a></li>
                           <li> <a href="#">Terms and conditions</a></li>
                           <li> <a href="#"> Privacy policy</a></li>
                           <li> <a href="#">News</a></li>
                           <li> <a href="#"> Contact us</a></li>
                        </ul>
                     </div>
                  </div>
                  <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                     <div class="Follow">
                        <h3> Contact</h3>
                        <div class="row">
                           <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                              <input class="Newsletter" placeholder="Name" type="text">
                           </div>
                           <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                              <input class="Newsletter" placeholder="Email" type="text">
                           </div>
                           <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">
                              <textarea class="textarea" placeholder="comment" type="text">Comment</textarea>
                           </div>
                        </div>
                        <button class="Subscribe">Submit</button>
                     </div>
                  </div>
               </div>
               
            </div>
         </div>
  </div>
</template>

<script>
export default {
    name: 'Contact'
}
</script>

<style lang='scss'>
.contact{
    height: auto;
    margin-top: 0;
    color: azure;
    a{
        text-decoration: none;
    }
    li{
        list-style: none;
    }
    .location_icon{
        display: inline-flex;
        flex-direction: row;
        justify-content: space-evenly;
        color: azure;
        li{
            padding: 0 15px;
        }
    }
}
</style>