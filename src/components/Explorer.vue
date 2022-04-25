<template>
<head> 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/"><i class="fa-solid fa-car"></i> United Auto Sales</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/cars/new">Add Car</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/users/1">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/">Logout</RouterLink>
            </li>
          </ul>
        </div>
      
    </nav>
</header> 
<div class="container-fluid col-10 min-vh-100">
    <h2>Explore</h2>
    <div class="shadow-lg p-3 bg-white rounded">
        <form @submit.prevent="explore" id="searchForm" enctype="multipart/form-data">
            <div class="row g-1">
                <div class="mx-auto col-4">
                    <label for="make" >Make</label>
                    <input class="form-control" type="search" name="make" id="make">
                </div>
                    <div class="mx-auto col-4">
                        <label for="model" >Model</label>
                        <input class="form-control" type="search" name="model" id="model">
                    </div>
                
                    <div class="mt-4 mx-auto col-3">
                        <label for="search" class="visually-hidden">Search</label>
                        <button class="btn btn-success">Search</button>
                    </div>
            </div>
        </form>
    </div>
    <br>
    <br>
    <br>
    <div class="col-sm-2 col-md-4 ">
        <div class="card w-77 h-100 border-top-0 border-start-0 border-end-0 border-bottom border-5 border-success shadow">
            <img src="uploads/lambo2020.jpg" alt="car image" class="card-img-top"/>
                <div class="card-body">
                   <div class="row"> 
                       <div class="col-8">
                            <h5 class="card-title"> 2020 Lamborghini{{ make }} </h5> 
                       </div>
                       <div class="col-4">
                            <span class="badge bg-success"><i class="fa-solid fa-tag"></i> $36,000{{price}}</span>
                       </div>
                    </div>
                    <h6 class="card-text text-muted mb-4"> Huracan {{ model }} </h6>
                    <div class="row">
                    <div class="col mt-4 text-center">   
                        <a href="cars/2" class="btn btn-primary btn-sm">View more details</a>
                    </div>
                    </div>
                </div>
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