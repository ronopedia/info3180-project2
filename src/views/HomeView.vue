<script>
export default {
    data() {
        return {
            
        };
    },
}
</script>

<template>
  <div class="home-grid">
    <div class="home-text-section">
      <h1>Buy and Sell Cars Online</h1>
      <p>United Auto Sales provides the fastest easiest and most user friendly way to buy and sell cars online.
        Find a Great Price on the Vehicle You Want.</p>
      
      <button class="btn btn-primary mb-2" @click="$router.push('register')">Register</button>
        
      <button class="btn btn-success mb-2"  @click="$router.push('login')" >Login</button>
    </div>
    <img class="home-image" src="../assests/car.png" alt="Car Image">
  </div> 
</template>

<style>
/* Add any component specific styles here */
</style>