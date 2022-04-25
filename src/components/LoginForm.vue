<template>
<div class="container-fluid col-4 min-vh-100">
    <div class="d-block align-items-center justify-content-center">    
        <h2> Log into your account</h2>
    <div class="shadow p-3 mb-5 bg-white rounded">
    <form @submit.prevent="userLogin" method="POST" enctype="multipart/form-data" id="loginForm">
        <div class="col-12"> 
            <div class="row">
                <label class="form-label" for="username">Username</label>
                <input class="form-control" type="text" name="user" id="user" required>
            </div>
            <div class="row">
                <label class="form-label" for="password">Password</label>
                <input class="form-control" type="text" name="pass" id="pass" required> 
            </div>
            <div class="row">
                <div class="mt-4 col-12">
                    <button type="submit" class="btn btn-success mb-2">Login</button>
                </div>
            </div>
        </div>
    </form>
    </div>
    </div>
    </div>
</template>


<script>
export default {
    name: 'loginForm',
    data(){
        return {
            message: ''
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
                    "Accept":"application/json",
                    "Content-Type": "application/json"
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                console.log(data);
            })
        }
    }
}
</script>