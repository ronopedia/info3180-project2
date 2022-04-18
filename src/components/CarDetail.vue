<template>
<div v-for="car in cars" class="col-sm-6 col-md-4 mb-5">
    <div class="card w-77 h-100 border-top-0 border-start-0 border-end-0 border-bottom border-5 border-success shadow">
        <img :src="/" alt="car image" class="card-img-left"/>
            <div class="card-body">
                <h4 class="card-title"> {{ make }} </h4> 
                <h5 class="card-text"> {{ model }} </h5>
                <p class="card-text"> {{ description }} </p>
                <span>Colour {{color}}</span> <span >Body Type {{car_type}}</span>
                <span>Price {{price}}</span> <span> Transmission {{transmission}}</span>
                <a href="#" class="btn btn-primary">Email Owner</a>
                <a v-on:click="function()">
                    <i class="far fa-heart" style="color:red"></i>
                </a>
            </div>
    </div>
</div>  
</template>

<script>
export default {
    data(){
        return {
            message: ''
        };
    },
    methods: {
        getCar() {
            let self = this;
            fetch("/api/cars/{car_id}", {
                headers: {
                    'Authorization': `Bearer`
                }
            })
        }

    }
}

</script>