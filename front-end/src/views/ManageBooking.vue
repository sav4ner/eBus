<template>
  <div class="buses">
     <div class="container">
				<div class="gallary-header text-center">
					<h2>
						Buses to book
					</h2>
					<p>
						These are the lists of Buses that have been approved by our organisation. Most of them are in the optimum condition to operate in the country
					</p>
				</div><!--/.gallery-header-->
				<div class="packages-content" v-if="info.status=='Active'">
					<div class="row">
                        <!-- <div v-for="data in info" :key="data.photo"> -->
                            <div class="col-md-3 col-sm-4" v-for="data in info" :key="data.busId">
                                <div class="single-package-item">
                                    <!-- <img :src="data.imageurl" alt="package-place"> -->
                                    <div class="single-package-item-txt">
                                        <h3 class='name'>{{data.platenumber}} </h3>
                                        <div class="packages-para">
                                            <p>
                                                <!-- <span>
                                                    <i class="fa fa-angle-right"></i> 5iption daays 6 nights
                                                </span> -->
                                                <i class="fa fa-angle-right"></i> {{data.bustype}}
                                            </p>
                                            
                                                <hr>
                                                <span>
                                                    <i class="fa fa-angle-right"></i><b>Number of Seats:</b> {{data.seats}}
                                                </span>
                                                
                                            
                                        </div><!--/.packages-para-->
                                        <div class="packages-review">
                                            
                                                <p v-if="data.rating==5">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==4">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==3">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==2">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==1">
                                                    <i class="fa fa-star"></i>
                                                    
                                                </p>
                                                <!-- <span class="pull-right">{{data.price+' KSH'}}</span> -->
                                            
                                        </div><!--/.packages-review-->
                                        <div class="about-btn">
                                            <button class="about-view packages-btn">
                                                book now
                                            </button>
                                        </div><!--/.about-btn-->
                                    </div><!--/.single-package-item-txt-->
                                </div><!--/.single-package-item-->

                            </div><!--/.col-->
                        <!-- </div> -->

					</div><!--/.row-->
				</div><!--/.packages-content-->
			</div>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ManageBooking',
    data() {
        return {
            info : null,
            images:[]
            
        } 

    },
    methods: {
        refreshData(){
            axios.get('/api/v1/bus')
            .then((response)=>{
                this.info=response.data
            });
        },
        fetchinage(){
            for (let index = 0; index < this.info.length; index++) {
                this.images[index] = this.info.photo;
                console.log(this.images);
            }
        }
        
    },
    
    mounted:function() {
//     this.$axios
//   .get('http://localhost:8000/users')
//   .then(response => (this.info = response.data.bpi));
//     console.log(this.info)
        this.refreshData();
        this.fetchinage();
        console.log(this.info)

    //   console.log(this.hotels);
    
  }

  

}
</script>

<style scoped>
    .buses{
    padding-top:74px;
}
</style>