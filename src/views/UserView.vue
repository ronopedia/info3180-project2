<template>
<div class="card">
        <img :src="images/car.png" alt="user image" class="card-img-left"/>
            <div class="card-body">
                <h3 class="card-title"> {{ name }} </h3> 
                <h4 class="card-text"> @{{ username }} </h4>
                <p class="card-text"> {{biography}} </p>
                <span>Email {{email}}</span>
                <span>Location {{location}}</span>
                <span>Joined {{date_joined}}</span>
            </div>
</div>

<h3>Cars Favourited</h3>
<div  class="col-sm-6 col-md-4 mb-5">
    <div class="card w-77 h-100 border-top-0 border-start-0 border-end-0 border-bottom border-5 border-success shadow">
        <img  alt="car image" class="card-img-top"/>
            <div class="card-body">
                <h5 class="card-title"> {{ make }} </h5> <span class="badge rounded-pill bg-success">Price {{price}}</span>
                <h6 class="card-text"> {{ model }} </h6>
                <a href="#" class="btn btn-primary">View more details</a>
            </div>
    </div>
</div>  

</template>

<script>
export default {
    name: "users",
    data(){
        return {
    
        }
    },
    methods: {
        User(){
            let self = this
            let userid = new self.id;
            fetch("/api/users/" + new URLSearchParams({ userid }),{
                method: 'POST',
                body: form_data
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