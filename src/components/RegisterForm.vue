<template>
    <form @submit.prevent="registerUser" method="POST" enctype="multipart/form-data" id="registerForm">
        <label for="username">Username</label>
        <input type="text" name="user" id="user" required>
        
        <label for="password">Password</label>
        <input type="text" name="pass" id="pass" required>
        
        <label for="email">Email</label>
        <input type="text" name="email" id="email" required>
        
        <label for="name">Fullname</label>
        <input type="text" name="name" id="name" required>

        <label for="location">Location</label>
        <input type="text" name="loc" id="loc" required>

        <label for="biography">Biography</label>
        <textarea name="bio" id="bio" cols="50" rows="4" required></textarea>
        
        <label for="photo">Upload Photo</label>
        <input type="file" name="photo" id="photo" required>

        <button type="submit">Register</button>
    </form>
</template>


<script>
export default {
    name: "registerForm",
    data(){
        return {
            message: 'Registration successful!'
        }
    },
    methods: {
        registerUser(){
            let registerForm = document.getElementById('registerForm');
            let form_data = new FormData(registerForm);
            let self = this
            fetch("/api/register",{
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