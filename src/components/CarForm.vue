<template>
    <form @submit.prevent="addCar" method="POST" enctype="multipart/form-data" id="carForm">
        <label for="make">Make</label>
        <input type="text" name="make" id="make" required>
        
        <label for="model">Model</label>
        <input type="text" name="model" id="model" required>
        
        <label for="colour">Colour</label>
        <input type="text" name="colour" id="colour" required>
        
        <label for="year">Year</label>
        <input type="text" name="year" id="year" required>

        <label for="price">Price</label>
        <input type="text" name="price" id="price" required>
        
        <label for="price">Car Type</label>
        <select name="price" id="price" required></select>

        <label for="transmission">Transmission</label>
        <select name="trans" id="trans" required></select>

        <label for="description">Description</label>
        <textarea name="desc" id="desc" cols="50" rows="4" required></textarea>
        
        <label for="photo">Upload Photo</label>
        <input type="file" name="photo" id="photo" required>

        <button type="submit">Save</button>
    </form>
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