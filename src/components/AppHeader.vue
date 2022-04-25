<template>
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
        
          <ul class="navbar-nav ml auto">
            <li class="nav-item">
              <RouterLink to="/register" class="nav-link active">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/login">Login</RouterLink>
            </li>
          </ul>
        </div>
      
    </nav>
  </header> 
</template>

<script>
import { RouterLink } from "vue-router";
</script>

<style>
/* Add any component specific styles here */
</style>