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
<div class="card mb-3 shadow-lg">
  <div class="row g-0">
    <div class="col-md-6">
        <img src="../images/car2.jpg" alt="car image" class="img-fluid rounded-start mh-100"/>
    </div>
    <div class="col-md-6">
        <div class="card-body">
            <div class="row">
                <div class="col-md-4">
                <h4 class="card-title">Danica Patrick {{ name }} </h4>
            </div>
            </div> 
            <div class="row mt-2">
                <div class="col-md-4">
                <h5 class="card-text"> @dpatrick{{ username }} </h5>
            </div>
            </div>
            <div class="row mt-2">
                <div class="col-md-10">
                <p class="card-text"> I am a professional racing driver and the most successfull woman in the history of American Open wheel racing. I love cars and driving fast.{{ description }} </p>
            </div>
            </div>
            <div class="row mt-2">
                <div class="col-md-6">
                <p>Email  {{email}}</p> 
                </div>
                </div>
            <div class="row mt-2">
                <div class="col-md-6">
                <p>Location  {{location}}</p>
                </div>
                </div>
                <div class="row mt-2">
                <div class="col-md-6">
                <p>Joined  {{date_joined}}</p>
                </div>
                </div>
            </div>
            </div>
          </div>
      </div>
      
      
<br>
<h3>Cars Favourited</h3>

    <div class="col-sm-2 col-md-4 ">
        <div class="card w-77 h-100 border-top-0 border-start-0 border-end-0 border-bottom border-5 border-success shadow">
            <img src="../uploads/lambo2020.jpg" alt="car image" class="card-img-top"/>
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