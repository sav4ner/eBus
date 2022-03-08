<template>
  <div class="testimony">
      <div class="container mt-5">
    <div class="row">
        <div class="col-md-4">
            <div class="testimonial-1 rounded"><img class="mb-3" src="https://i.imgur.com/ECXzJ1k.png" width="40">
                <p>Thanks to you, we are able to gain real time visibility into our customer debt and follow up on unpaid invoices if necessary<br><br></p>
                <div class="d-flex flex-row align-items-center"><img class="rounded-circle" src="https://i.imgur.com/sKDeBrg.jpg" width="40">
                    <div class="ml-2 about"><span class="d-block name">Giralle Makau</span><span class="place">Operator Trade, Little AR, TX</span></div>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="testimonial-2 rounded"><img class="mb-3" src="https://i.imgur.com/OEJ9eQF.png" width="40">
                <p>Picassa Busses is vested in our comfortable and safe traveling and that is what makes us want to be associated with it. We value their cutting edge technology,reliability and easy to use platform<br><br></p>
                <div class="d-flex flex-row align-items-center"><img class="rounded-circle" src="data:image/jpeg;base64,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" width="40">
                    <div class="ml-2 about"><span class="d-block name">Sam Nyakundi</span><span class="place-2">Android Developer, Little AR, TX</span></div>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="testimonial-1 rounded"><img class="mb-3" src="https://i.imgur.com/ECXzJ1k.png" width="40">
                <p>You have transistioned my bussines from transporting my products to several parts of the country by the push of a button<br><br></p>
                <div class="d-flex flex-row align-items-center"><img class="rounded-circle" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgrXj_yvzNrAuekQLiv2Oec4vF9S541FHJAg&usqp=CAU" width="40">
                    <div class="ml-2 about"><span class="d-block name">Peter Oduor</span><span class="place">Operator Trade, Little AR, CA</span></div>
                </div>
            </div>
        </div>
    </div>
</div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.testimony{
    height: 60vh;
}
.testimonial-1 {
    background: #fff;
    padding: 14px;
    color: #000
}

.col-md-4 {
    margin-top: 25px
}

.name {
    font-weight: 700;
    font-size: 14px;
    margin-bottom: -3px
}

.place {
    font-size: 13px;
    color: #988c8c
}

.place-2 {
    font-size: 13px;
    color: #ffffff
}

.testimonial-2 {
    background: blue;
    padding: 14px;
    color: #fff
}
</style>