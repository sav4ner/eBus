<template>
  <div class="Tours">
         <div class="container">
            <div class="row">
               <div class="col-md-12">
                  <div class="titlepage">
                     <h2>The Best Tours</h2>
                     <span>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,</span> 
                  </div>
               </div>
            </div>
            <section id="demos">
               <div class="row">
                  <div class="col-md-12">
                     <div class="owl-carousel owl-theme owl-loaded owl-drag">
                     <div class="owl-stage-outer"><div class="owl-stage" style="transform: translate3d(-700px, 0px, 0px); transition: all 0s ease 0s; width: 2800px;"><div class="owl-item cloned" style="width: 340px; margin-right: 10px;"><div class="item">
                           <img class="img-responsive" :src="require('../images/3.jpg')" alt="#">
                           <h3>Nairobi</h3>
                           <p>A humble a busy city full of flourishing bussinesses</p>
                        </div></div><div class="owl-item cloned" style="width: 340px; margin-right: 10px;"><div class="item">
                           <img class="img-responsive" :src="require('../images/2.jpg')" alt="#">
                           <h3>Nakuru</h3>
                           <p>Fourth Largest city in the country. It's found on your way to the western part of the country. It hosts alot of hotels</p>
                        </div></div><div class="owl-item active" style="width: 340px; margin-right: 10px;"><div class="item">
                           <img class="img-responsive" :src="rquire('..images/1.jpg')" alt="#">
                           <h3>Eldoret</h3>
                           <p>The food busket of the country and the source of champions. It is a town best for tour visits due to its ever welcoming people.</p>
                       
                          
                        </div></div></div></div><div class="owl-nav"><button type="button" role="presentation" class="owl-prev"><span aria-label="Previous">‹</span></button><button type="button" role="presentation" class="owl-next"><span aria-label="Next">›</span></button></div><div class="owl-dots"><button role="button" class="owl-dot active"><span></span></button><button role="button" class="owl-dot"><span></span></button></div></div>
                  </div>
               </div>
            </section>
         </div>
      </div>
</template>

<script>
export default {

}
</script>

<style>

</style>