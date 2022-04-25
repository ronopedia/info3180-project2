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
              <RouterLink class="nav-link active" to="/newcars">Add Car</RouterLink>
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
<div class="container-fluid col-10 min-vh-100 ">
<div class="card mb-3 shadow-lg">
  <div class="row g-0">
    <div class="col-md-6">
        <img src="../images/car2.jpg" alt="car image" class="img-fluid rounded-start mh-100"/>
    </div>
    <div class="col-md-6">
        <div class="card-body">
            <div class="row">
                <div class="col-md-4">
                <h4 class="card-title">2018 Tesla {{ make }} </h4>
            </div>
            </div> 
            <div class="row mt-2">
                <div class="col-md-4">
                <h5 class="card-text"> Model S{{ model }} </h5>
            </div>
            </div>
            <div class="row mt-2">
                <div class="col-md-10">
                <p class="card-text"> With the longest range and quickest acceleration of any electric vehicle in production.{{ description }} </p>
            </div>
            </div>
            <div class="row mt-2">
                <div class="col-md-6">
                <p>Colour  {{color}}</p> 
                </div>
                <div class="col-md-6">
                <p>Body Type  {{car_type}}</p>
                </div>
            </div>
            <div class="row mt-2">
                <div class="col-md-6">
                <p>Price {{price}}</p>
                </div> 
                <div class="col-md-6">
                <p> Transmission  {{transmission}}</p>
            </div>
            </div>
            <div class="row mt-4">
                <div class="col-md-6">
                <a href="#" class="btn btn-success">Email Owner</a>
                </div>
                <div class="col-md-2">
                <i class="far fa-heart" style="color:red"></i>
            </div>
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
            
        };
    },
    methods: {
        getCar() {
            let self = this;
            let carID = self.id
            fetch("/api/cars/"+ carID, {
                headers: {
                    'Authorization': `Bearer`
                }
            })
        }

    }
}

</script>