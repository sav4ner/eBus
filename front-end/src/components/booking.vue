<template>
  <div class="container mt-5 pt-1 pb-5 " style="height: 100vh;">
    <div class="row d-flex justify-content-center" style="width:100%; height:280px; ">
        <div class="col-md-10 " style="margin-top: -60px;" >
            <div class="bg-white" style="height:280px; border-radius:10px;">
                <ul class="nav nav-tabs nav-fill" id="myTab" role="tablist">
                    <li class="nav-item" role="presentation"> <button class="nav-link" id="faq_tab_4-tab" data-bs-toggle="tab" data-bs-target="#faq_tab_4" type="button" role="tab" aria-controls="faq_tab_4" aria-selected="false">
                            <div class="d-flex flex-column lh-lg"> <i class='bx bxs-plane-alt'></i> <span>Booking Status</span> </div>
                        </button> </li>
                    <!-- <li class="nav-item" role="presentation"> <button class="nav-link active" id="faq_tab_1-tab" data-bs-toggle="tab" data-bs-target="#faq_tab_1" type="button" role="tab" aria-controls="faq_tab_1" aria-selected="true">
                            <div class="d-flex flex-column lh-lg"> <i class='bx bxs-plane-alt'></i> <span>Travels</span> </div>
                        </button> </li> -->
                    <li class="nav-item" role="presentation"> <button class="nav-link" id="faq_tab_2-tab" data-bs-toggle="tab" data-bs-target="#faq_tab_2" type="button" role="tab" aria-controls="faq_tab_2" aria-selected="false">
                            <div class="d-flex flex-column lh-lg"> <i class='bx bxs-shopping-bag'></i> <span>My Trips</span> </div>
                        </button> </li>
                    <!-- <li class="nav-item" role="presentation"> <button class="nav-link" id="faq_tab_3-tab" data-bs-toggle="tab" data-bs-target="#faq_tab_3" type="button" role="tab" aria-controls="faq_tab_3" aria-selected="false">
                            <div class="d-flex flex-column lh-lg"> <i class='bx bx-check-circle'></i> <span>Check-in</span> </div>
                        </button> </li> -->
                    
                </ul>
                <div class="tab-content" id="myTabContent">
                     <!-- <div class="tab-pane fade active show" id="faq_tab_1" role="tabpanel" aria-labelledby="faq_tab_1-tab">
                        <div class="container p-3">
                            <div class="input-group mb-3"> <input type="text" class="form-control" placeholder="From" v-model="from"> <input type="text" class="form-control" placeholder="To" v-model="to"> </div>
                            <div class="input-group mb-3"> <input type="text" class="form-control" placeholder="Date of Departure" v-model="date"> <input type="text" class="form-control" placeholder="No. of Passengers" v-model="passengers"> </div>
                             <div class="input-group mb-3"> <select class="form-select form-control" id="inputGroupSelect02">
                                    <option selected>Passenger</option>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3+</option>
                                    </select> 
                                  <select class="form-select form-control" id="inputGroupSelect02">
                                    <option selected>Cabin</option>
                                    <option value="1">One</option>
                                    <option value="2">Two</option>
                                    <option value="3">Three</option>
                                </select>  </div> 
                            <div class="mt-4 d-flex justify-content-end"> <button class="btn btn-success custom-button px-5" @click="showModal = !showModal">Show Busses</button> </div>
                            <showbuses :visible="showModal"></showbuses>
                        </div>
                    </div> --> 
                    <div class="tab-pane fade " id="faq_tab_2" role="tabpanel" aria-labelledby="faq_tab_2-tab">
                        <div class="container p-3 scroll-y" style="color: black; height:200px;">
                            <div class="p-3 d-flex justify-content-between align-items-center">
                                <div class="d-flex flex-column"> 
                                    <!-- <span>Departure</span> -->
                                    <div class="d-flex justify-content-between align-items-center"> <span>Nairobi -</span> <i class='bx bxs-plane-take-off ms-3 me-3 text-warning'></i> <span>Eldoret</span> </div>
                                </div>
                                <div> <span>3 hours 22 minutes</span> </div>
                            </div>
                            <div class="border-top p-3 d-flex justify-content-between align-items-center">
                                <div class="d-flex flex-column"> 
                                    <!-- <span>Departure</span> -->
                                    <div class="d-flex justify-content-between align-items-center"> <span>Nakuru -</span> <i class='bx bxs-plane-take-off ms-3 me-3 text-warning'></i> <span>Nairobi</span> </div>
                                </div>
                                <div> <span>13 hours 12 minutes</span> </div>
                            </div>
                            <div class="border-top p-3 d-flex justify-content-between align-items-center">
                                <div class="d-flex flex-column">
                                     <!-- <span>Departure</span> -->
                                    <div class="d-flex justify-content-between align-items-center"> <span>Embu -</span> <i class='bx bxs-plane-take-off ms-3 me-3 text-warning'></i> <span>Nairobi</span> </div>
                                </div>
                                <div> <span>5 hours 12 minutes</span> </div>
                            </div>
                            <div class="border-top p-3 d-flex justify-content-between align-items-center">
                                <div class="d-flex flex-column"> 
                                    <!-- <span>Departure</span> -->
                                    <div class="d-flex justify-content-between align-items-center"> <span>Nairobi -</span> <i class='bx bxs-plane-take-off ms-3 me-3 text-warning'></i> <span>Kisumu</span> </div>
                                </div>
                                <div> <span>8 hours 12 minutes</span> </div>
                            </div>
                            <div class="border-top p-3 d-flex justify-content-between align-items-center">
                                <div class="d-flex flex-column"> 
                                    <!-- <span>Departure</span> -->
                                    <div class="d-flex justify-content-between align-items-center"> <span>Eldoret -</span> <i class='bx bxs-plane-take-off ms-3 me-3 text-warning'></i> <span>Nairobi</span> </div>
                                </div>
                                <div> <span>13 hours 12 minutes</span> </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="faq_tab_3" role="tabpanel" aria-labelledby="faq_tab_3-tab">
                        <div class="container p-3 mt-4">
                            <div class="input-group mb-3"> <input type="text" class="form-control" placeholder="Search hotels..."> <input type="text" class="form-control" placeholder="Location"> </div>
                            <div class="input-group mb-3"> <select class="form-select form-control" id="inputGroupSelect02">
                                    <option selected>Rooms</option>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3+</option>
                                </select> <select class="form-select form-control" id="inputGroupSelect02">
                                    <option selected>Members</option>
                                    <option value="1">One</option>
                                    <option value="2">Two</option>
                                    <option value="3">Three</option>
                                    <option value="3">Four</option>
                                    <option value="3">Five</option>
                                </select> </div>
                            <div class="mt-4 d-flex justify-content-end"> <button class="btn btn-success custom-button px-5">Search Hotels</button> </div>
                        </div>
                    </div>
                    <div class="tab-pane fade active show" id="faq_tab_4" role="tabpanel" aria-labelledby="faq_tab_4-tab">
                        <div class="container p-3">
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="input-group mb-3"> <select class="form-select form-control" id="inputGroupSelect02">
                                            <option selected>Select Route</option>
                                            <option value="2">Nairobi-Eldoret</option>
                                            <option value="3">Nairobi-Nakuru</option>
                                            <option value="4">Nairobi-Mombasa</option>
                                            <option value="5">Nairobi-Embu</option>
                                            <option value="6">Nairobi-Kitale</option>
                                        </select> </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-group mb-3"> <input type="text" class="form-control" placeholder="Receipt Number"> <button class="btn btn-outline-secondary custom-button" type="button" @click="showModal = !showModal">Search</button>
                                    <showbuses :visible="showModal"></showbuses>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>


</template>

<script>
 import axios from 'axios'
import showbuses from './showbuses.vue'
export default {
    data() {
        return {
            data: null,
            route: null,
            booking: null,
            showModal: false,
            link: '/api/v1/bookings/'+this.booking+'/'
        }
    },
    methods: {
        get(){
            axios.get(this.link).then(res=>{
                this.data = res.data
                alert(res.data)
            }).catch(err=>{
                this.data= 'Error'
                console.log(err)
            })
        }
    },

    props: {
        visible: {date: null,
            to: null,
            from: null,
            passengers: '',
            default: false
        },
        title: {
            default: "🔥 Boo!"
        },
        closeIcon: {
            default: '<span>&#x274C;</span>'
        },
        content: {
            default: '<p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet a tenetur delectus reprehenderit'},
        footer: {
        default: '<button>I do nothing!</button>'
        }
    },
    components: {
        showbuses,
    }
}
</script>

<style scoped>
/* body {
    background-image: linear-gradient(to right top, #9A1550, #4D0525);
    background-repeat: no-repeat;
    height: 100vh
} */

::-webkit-scrollbar {
    width: 6px
}

::-webkit-scrollbar-track {
    background: #f1f1f1
}

::-webkit-scrollbar-thumb {
    background: #888
}

::-webkit-scrollbar-thumb:hover {
    background: #555
}

.nav-tabs .nav-link.active {
    border-color: transparent;
    background-color: #fff !important;
    color: #9a1550 !important;
    border-bottom: 4px solid #9a1550 !important
}

.nav-fill .nav-item .nav-link,
.nav-justified .nav-item .nav-link {
    width: 100%;
    color: #000
}

.nav-tabs .nav-link {
    border-top-left-radius: 0rem !important;
    border-top-right-radius: 0rem !important
}

.nav-tabs .nav-link.active {
    border-color: transparent;
    background-color: #60D0FF;
    color: #fff;
    font-weight: 600
}

.nav-link {
    height: 77px;
    font-size: 13px;
    background-color: #fff
}

.nav-link:hover {
    border: none
}

.nav-link:focus {
    outline: none
}

.tab-pane {
    height: 300px
}

.form-control {
    height: 45px;
    position: relative
}

.form-control:focus {
    outline: none;
    box-shadow: none;
    border: 1px solid #9a1550
}

.flight-where-from:after {
    position: absolute;
    content: '23';
    width: 20px;
    height: 20px;
    border-radius: 50%
}

.custom-button {
    height: 45px;
    background-color: #9a1550;
    border: none;
    color: #fff
}

.custom-button:hover,
.custom-button:focus {
    background-color: #9a1550;
    box-shadow: none;
    outline: none
}

.scroll-y {
    overflow-y: scroll;
    height: 300px
}

/* Modal css instructions */

body {
    height: 100vh;
    justify-content: center;
    align-items: center;
    display: flex;
    background-color: #eee
}


</style>