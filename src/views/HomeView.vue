<script>
export default {
    data() {
        return {
            
        };
    },
}
</script>

<template>
<head> 
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>

  <div class="container-fluid">
    <div class="row g-0" >
      <div class="col-6 min-vh-100">
        <div class="mx-auto">
          <h2>Buy and Sell Cars Online</h2>
          <p class="text-muted d-block"> United Auto Sales provides the fastest easiest and most user friendly way to buy and sell cars online. Find a Great Price on the Vehicle You Want.</p>
        
          <button class="btn btn-primary mb-2" @click="$router.push('register')">Register</button>
          <button class="btn btn-success mb-2"  @click="$router.push('login')" >Login</button>
       
        </div>
      </div>
        <div class="col-6 min-vh-100" >
          <img src="../images/car.png" class="img-fluid" alt="Car Image">
        </div> 
    </div>
  </div> 
</template>

<style>

</style>