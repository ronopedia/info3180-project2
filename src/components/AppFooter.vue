<template>
      <footer>
          <div class="container">
              <p>Copyright &copy {{ year }} United Auto Sales</p>
          </div>
      </footer>
</template>

<script>
export default {
    data() {
      return {
          year: (new Date).getFullYear()
      }        
    }
}
</script>

<style>
/* Add any component specific styles here */
</style>