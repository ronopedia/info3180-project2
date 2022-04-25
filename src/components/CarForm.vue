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
 <div class="bg-light">
<div class="container-fluid col-6 min-vh-100">
    <div class="d-block align-items-center justify-content-center">
     <h2>Add New Car</h2>
     <div class="shadow p-3 mb-5 bg-white rounded">
    <form @submit.prevent="addCar" method="POST" enctype="multipart/form-data" id="carForm">
    
    <div class="row">
        <div class="col-6">
        <label class="form-label" for="make">Make</label>
        <input class="form-control" type="text" name=" make" id="make" required>
        </div>
        <div class="col-6">
        <label class="form-label" for="model">Model</label>
        <input class="form-control" type="text" name="model" id="model" required>
        </div>
    </div>    
    <div class="row">
        <div class="mt-2 col-6">
        <label class="form-label" for="colour">Colour</label>
        <input class="form-control" type="text" name="colour" id="colour" required>
        </div>
        <div class="mt-2 col-6">
        <label class="form-label" for="year">Year</label>
        <input class="form-control" type="text" name="year" id="year" required>
        </div>
    </div>
    <div class="row">
        <div class="mt-2 col-6">
        <label class="form-label" for="price">Price</label>
        <input class="form-control" type="text" name="price" id="price" required>
        </div>
        <div class="mt-2 col-6">
        <label class="form-label" for="car_type">Car Type</label>
        <select class="form-control" name="ctype" id="ctype" required></select>
        </div>
    </div>
    <div class="row">
        <div class="mt-2 col-6">
        <label class="form-label" for="transmission">Transmission</label>
        <select class="form-control" name="trans" id="trans" required></select>
        </div>
      </div>
    <div class="row"> 
        <div class="mt-2 col-12">  
        <label class="form-label" for="description">Description</label>
        <textarea class="form-control" name="desc" id="desc" cols="50" rows="4" required></textarea>
    </div> 
    </div>
    <div class="row">
        <div class="mt-2 col-6 ">
        <label class="form-label" for="photo">Upload Photo</label>
        <input class="form-control-file" type="file" name="photo" id="photo" required>
        </div> 
    </div>
    <div class="row">
        <div class="mt-4 col-4">
        <button type="submit" class="mb-2 btn btn-success">Save</button>
      </div>
      </div>
    </form>
</div>
</div>
</div>
</div>
</template>


<script>
export default {
    name: "carForm",
    data(){
        return {
            message: 'New car added successfully!'
        }
    },
    methods: {
        addCar(){
            let carForm = document.getElementById('carForm');
            let form_data = new FormData(carForm);
            let self = this
            fetch("/api/cars",{
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