<template>
  <div id="booking" class="section">
    <div class="section-center">
        <div class="container">
            <div class="row">
                <div class="booking-form">
                    <div class="form-header">
                        <h1>Make your reservation</h1>
                    </div>
                    <form>
                        <div class="form-group"> <input class="form-control" type="text" placeholder="Fullname..." v-model="fname"> <span class="form-label">Destination</span> </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group"> <input class="form-control" type="date" required v-model="date"> <span class="form-label">Date of travel</span> </div>
                            </div>
                            <!-- <div class="col-md-6">
                                <div class="form-group"> <input class="form-control" type="date" required> <span class="form-label">Check out</span> </div>
                            </div> -->
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group"> <select class="form-control" required v-model="pas">
                                        <option value="" selected hidden>no of Passengers</option>
                                        <option>1</option>
                                        <option>2</option>
                                        <option>3</option>
                                        <option>4</option>
                                        <option>5</option>
                                    </select> <span class="select-arrow"></span> <span class="form-label">Rooms</span> </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group"> <select class="form-control" required v-model="route">
                                        <option value="" selected hidden>Route</option>
                                        <option value="Nairobi-Eldoret">Nairobi-Eldoret</option>
                                        <option value="Nairobi-Nakuru">Nairobi-Nakuru</option>
                                        <option value="Nairobi-Mombasa">Nairobi-Mombasa</option>
                                        <option value="Nairobi-Embu">Nairobi-Embu</option>
                                        <option value="Nairobi-Kitale">Nairobi-Kitale</option>
                                    </select> <span class="select-arrow"></span> <span class="form-label">Adults</span> </div>
                            </div>
                            <!-- <div class="col-md-4">
                                <div class="form-group"> <select class="form-control" required>
                                        <option value="" selected hidden>no of children</option>
                                        <option>0</option>
                                        <option>1</option>
                                        <option>2</option>
                                    </select> <span class="select-arrow"></span> <span class="form-label">Children</span> </div>
                            </div> -->
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <div class="form-group"> <input class="form-control" type="text" placeholder="Destination" v-model="destination"> <span class="form-label" >Destination</span> </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group"> <input class="form-control" type="email" placeholder="Enter your Email" v-model="email"> <span class="form-label" >Email</span> </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group"> <input class="form-control" type="tel" placeholder="Enter you Phone number" v-model="phone"> <span class="form-label" >Phone</span> </div>
                            </div>
                        </div>
                        <div class="form-btn"> <button class="submit-btn" data-toggle="modal" data-target="#staticBackdrop" @click="authenticate">Book Now</button> </div>
                        
                    </form>
                    <div class="container">
  
  <!-- Trigger the modal with a button -->
  
  </div>
                </div>
            </div>
        </div>
    </div>
    
<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-body">
                <div class="text-right"> <i class="fa fa-close close" data-dismiss="modal"></i> </div>
                <div class="tabs mt-3">
                    <ul class="nav nav-tabs" id="myTab" role="tablist">
                        <li class="nav-item" role="presentation"> <a class="nav-link active" id="visa-tab" data-toggle="tab" href="#visa" role="tab" aria-controls="visa" aria-selected="true"> <img src="https://i.imgur.com/sB4jftM.png" width="80"> </a> </li>
                        <li class="nav-item" role="presentation"> <a class="nav-link" id="paypal-tab" data-toggle="tab" href="#paypal" role="tab" aria-controls="paypal" aria-selected="false"> <img src="https://i.imgur.com/yK7EDD1.png" width="80"> </a> </li>
                    </ul>
                    <div class="tab-content" id="myTabContent">
                        <div class="tab-pane fade show active" id="visa" role="tabpanel" aria-labelledby="visa-tab">
                            <div class="mt-4 mx-4">
                                <div class="text-center">
                                    <h5>Credit card</h5>
                                </div>
                                <div class="form mt-3">
                                    <div class="inputbox"> <input type="text" name="name" class="form-control" required="required"> <span>Cardholder Name</span> </div>
                                    <div class="inputbox"> <input type="text" name="name" min="1" max="999" class="form-control" required="required"> <span>Card Number</span> <i class="fa fa-eye"></i> </div>
                                    <div class="d-flex flex-row">
                                        <div class="inputbox"> <input type="text" name="name" min="1" max="999" class="form-control" required="required"> <span>Expiration Date</span> </div>
                                        <div class="inputbox"> <input type="text" name="name" min="1" max="999" class="form-control" required="required"> <span>CVV</span> </div>
                                    </div>
                                    <div class="px-5 pay"> <button class="btn btn-success btn-block">Add card</button> </div>
                                </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="paypal" role="tabpanel" aria-labelledby="paypal-tab">
                            <div class="px-5 mt-5">
                                <div class="inputbox"> <input type="text" name="name" class="form-control" required="required"> <span>Paypal Email Address</span> </div>
                                <div class="pay px-5"> <button class="btn btn-primary btn-block">Add paypal</button> </div>
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
export default {
    name: 'book',
    data() {
        return {
            data: null,
            route: null,
            pas: null,
            date: null,
            fname: null,
            email: null,
            phone: null,
            destination: null,
            bill: null,
        }
    },
    methods: {
        authenticate(){
            if (this.$store.state.isAuthenticated) {
                const username= localStorage.getItem('username')
                console.log(username)
                
                axios.post('/api/v1/bookings',{
    "name": this.fname,
    "user": localStorage.getItem('username'),
    "email": this.email,
    "contact": this.phone,
    "date": this.date,
    "time": '06:00:00',
    "fro": this.route,
    "destination": this.destination,
    "bill": 800
    // "name": "levin",
    // "user": "admin",
    // "email": "levin@gmail.com",
    // "contact": "0773834848",
    // "date": "2022-03-12",
    // "time": "06:04:00",
    // "fro": "Eldoret",
    // "destination": "Nairobi",
    // "bill": null

     
})
                .then(
                    res=>{
                        console.log(res.data.status)
                        alert('Succesfully Booked')
                        this.$router.push('/')
                    }).catch(error=>{
                        console.log(error)
                        alert('Error')
                    })
            } else {
                alert('Please Log In')
            }
        }
    },

}
</script>

<style scoped>
  /* body {
    background-image: linear-gradient(to right, #7B1FA2, #E91E63)
} */
#booking{
    z-index: 0;
    padding-top: 75px;
    padding-bottom: 75px;
}
.section {
    position: relative;
    height: 100vh
}

.section .section-center {
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%)
}

#booking {
    font-family: 'Raleway', sans-serif
}

.booking-form {
    position: relative;
    max-width: 642px;
    width: 100%;
    margin: auto;
    padding: 40px;
    overflow: hidden;
    background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnxLbQ-gEuPa9w8SuX_8-o8409bXzo2USoGg&usqp=CAU');
    background-size: cover;
    border-radius: 5px;
    z-index: 20
}

.booking-form::before {
    content: '';
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
    background: rgba(0, 0, 0, 0.7);
    z-index: -1
}

.booking-form .form-header {
    text-align: center;
    position: relative;
    margin-bottom: 30px
}

.booking-form .form-header h1 {
    font-weight: 700;
    text-transform: capitalize;
    font-size: 42px;
    margin: 0px;
    color: #fff
}

.booking-form .form-group {
    position: relative;
    margin-bottom: 30px
}

.booking-form .form-control {
    background-color: rgba(255, 255, 255, 0.2);
    height: 60px;
    padding: 0px 25px;
    border: none;
    border-radius: 40px;
    color: #fff;
    -webkit-box-shadow: 0px 0px 0px 2px transparent;
    box-shadow: 0px 0px 0px 2px transparent;
    -webkit-transition: 0.2s;
    transition: 0.2s
}

.booking-form .form-control::-webkit-input-placeholder {
    color: rgba(255, 255, 255, 0.5)
}

.booking-form .form-control:-ms-input-placeholder {
    color: rgba(255, 255, 255, 0.5)
}

.booking-form .form-control::placeholder {
    color: rgba(255, 255, 255, 0.5)
}

.booking-form .form-control:focus {
    -webkit-box-shadow: 0px 0px 0px 2px #ff8846;
    box-shadow: 0px 0px 0px 2px #ff8846
}

.booking-form input[type="date"].form-control {
    padding-top: 16px
}

.booking-form input[type="date"].form-control:invalid {
    color: rgba(255, 255, 255, 0.5)
}

.booking-form input[type="date"].form-control+.form-label {
    opacity: 1;
    top: 10px
}

.booking-form select.form-control {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none
}

.booking-form select.form-control:invalid {
    color: rgba(255, 255, 255, 0.5)
}

.booking-form select.form-control+.select-arrow {
    position: absolute;
    right: 15px;
    top: 50%;
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
    width: 32px;
    line-height: 32px;
    height: 32px;
    text-align: center;
    pointer-events: none;
    color: rgba(255, 255, 255, 0.5);
    font-size: 14px
}

.booking-form select.form-control+.select-arrow:after {
    content: '\279C';
    display: block;
    -webkit-transform: rotate(90deg);
    transform: rotate(90deg)
}

.booking-form select.form-control option {
    color: #000
}

.booking-form .form-label {
    position: absolute;
    top: -10px;
    left: 25px;
    opacity: 0;
    color: #ff8846;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.3px;
    height: 15px;
    line-height: 15px;
    -webkit-transition: 0.2s all;
    transition: 0.2s all
}

.booking-form .form-group.input-not-empty .form-control {
    padding-top: 16px
}

.booking-form .form-group.input-not-empty .form-label {
    opacity: 1;
    top: 10px
}

.booking-form .submit-btn {
    color: #fff;
    background-color: #e35e0a;
    font-weight: 700;
    height: 60px;
    padding: 10px 30px;
    width: 100%;
    border-radius: 40px;
    border: none;
    text-transform: uppercase;
    font-size: 16px;
    letter-spacing: 1.3px;
    -webkit-transition: 0.2s all;
    transition: 0.2s all
}

.booking-form .submit-btn:hover,
.booking-form .submit-btn:focus {
    opacity: 0.9
}

/* modal css */
.launch {
    height: 50px
}

.close {
    font-size: 21px;
    cursor: pointer
}

.modal-body {
    height: 450px
}

.nav-tabs {
    border: none !important
}

.nav-tabs .nav-link.active {
    color: #495057;
    background-color: #fff;
    border-color: #ffffff #ffffff #fff;
    border-top: 3px solid blue !important
}

.nav-tabs .nav-link {
    margin-bottom: -1px;
    border: 1px solid transparent;
    border-top-left-radius: 0rem;
    border-top-right-radius: 0rem;
    border-top: 3px solid #eee;
    font-size: 20px
}

.nav-tabs .nav-link:hover {
    border-color: #e9ecef #ffffff #ffffff
}

.nav-tabs {
    display: table !important;
    width: 100%
}

.nav-item {
    display: table-cell
}

.form-control {
    border-bottom: 1px solid #eee !important;
    border: none;
    font-weight: 600
}

.form-control:focus {
    color: #495057;
    background-color: #fff;
    border-color: #8bbafe;
    outline: 0;
    box-shadow: none
}

.inputbox {
    position: relative;
    margin-bottom: 20px;
    width: 100%
}

.inputbox span {
    position: absolute;
    top: 7px;
    left: 11px;
    transition: 0.5s
}

.inputbox i {
    position: absolute;
    top: 13px;
    right: 8px;
    transition: 0.5s;
    color: #3F51B5
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0
}

.inputbox input:focus~span {
    transform: translateX(-0px) translateY(-15px);
    font-size: 12px
}

.inputbox input:valid~span {
    transform: translateX(-0px) translateY(-15px);
    font-size: 12px
}

.pay button {
    height: 47px;
    border-radius: 37px
}
</style>