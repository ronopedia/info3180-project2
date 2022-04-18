<template>
    <form @submit.prevent="userLogin" method="POST" enctype="multipart/form-data" id="loginForm">
        <label for="username">Username</label>
        <input type="text" name="user" id="user" required>
        
        <label for="password">Password</label>
        <input type="text" name="pass" id="pass" required>

        <button type="submit">Login</button>
    </form>
</template>


<script>
export default {
    name: 'loginForm',
    data(){
        return {
            message: 'Login successful!'
        }
    },
    methods: {
        userLogin(){
            let loginForm = document.getElementById('loginForm');
            let form_data = new FormData(loginForm);
            let self = this
            fetch("/api/auth/login",{
                method: 'POST',
                body: form_data,
                headers:{
                    Accept:'application/json',
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