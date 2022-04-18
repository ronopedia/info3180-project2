<template>
<form @submit.prevent="explore" id="searchForm" enctype="multipart/form-data">
    <div class="input-group mx-sm-3 mb-2">
        <label for="make" class="form-label">Make</label>
        <input type="search" name="make" id="make" placeholder="Enter car make">
                
        <label for="model" class="form-label">Model</label>
        <input type="search" name="model" id="model" placeholder="Enter car model">
                
        <button class="btn btn-success mb-2">Search</button> 
    </div>
</form>

<div v-for="car in cars" class="col-sm-6 col-md-4 mb-5">
    <div class="card w-77 h-100 border-top-0 border-start-0 border-end-0 border-bottom border-5 border-success shadow">
        <img :src="/" alt="car image" class="card-img-top"/>
            <div class="card-body">
                <h5 class="card-title"> Make {{ make }} </h5> <span class="badge rounded-pill bg-success">Price {{price}}</span>
                <h6 class="card-text"> Model {{ model }} </h6>
                <a href="#" class="btn btn-primary">View more details</a>
            </div>
    </div>
</div>  
</template>

<script>
export default {
    data(){
        return {
            name: 'explore'
        };
    },
    methods: {
        explore() {
            let self = this;
            let searchForm = document.getElementById('searchForm')
            let make1 = document.getElementById('make').value;
            let model1 = document.getElementById('model').value;
            fetch("/api/search" +"?"+ new URLSearchParams({ make:make1,model:model1 }), {
                headers: {
                    Accept: 'application/json'
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
            })
        }

    }
}

</script>