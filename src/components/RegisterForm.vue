<template>
<head> 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<div class="bg-light">
<div class="container-fluid col-6 min-vh-100">
    <div class="d-block align-items-center justify-content-center">
     <h2>Register New User</h2>
     <div class="shadow p-3 mb-5 bg-white rounded">
    <form @submit.prevent="registerUser" method="POST" enctype="multipart/form-data" id="registerForm">
    
    <div class="row">
        <div class="col-6">
        <label class="form-label" for="username">Username</label>
        <input class="form-control" type="text" name="user" id="user" required>
        </div>
        <div class="col-6">
        <label class="form-label" for="password">Password</label>
        <input class="form-control" type="text" name="pass" id="pass" required>
        </div>
    </div>    
    <div class="row">
        <div class="mt-2 col-6">
        <label class="form-label" for="name">Fullname</label>
        <input class="form-control" type="text" name="name" id="name" required>
        </div>
        <div class="mt-2 col-6">
        <label class="form-label" for="email">Email</label>
        <input class="form-control" type="text" name="email" id="email" required>
        </div>
    </div>
    <div class="row">
        <div class="mt-2 col-6">
        <label class="form-label" for="location">Location</label>
        <input class="form-control" type="text" name="loc" id="loc" required>
        </div>
    </div>    
    <div class="row"> 
        <div class="mt-2 col-12">  
        <label class="form-label" for="biography">Biography</label>
        <textarea class="form-control" name="bio" id="bio" cols="50" rows="4" required></textarea>
    </div> 
    </div>
    <div class="row">
        <div class="mt-2 col-6 ">
        <label class="form-label" for="photo">Upload Photo</label>
        <input class="form-control-file" type="file" name="photo" id="photo" required>
        </div> 
    </div>
    <div class="row">
        <div class="mt-4 col-4">
        <button type="submit" class="mb-2 btn btn-success">Register</button>
      </div>
      </div>
    </form>
</div>
</div>
</div>
</div>
</template>


<script>
export default {
    name: "registerForm",
    data(){
        return {
            message: ''
        }
    },
    methods: {
        registerUser(){
            let registerForm = document.getElementById('registerForm');
            let form_data = new FormData(registerForm);
            let self = this
            fetch("/api/register",{
                method: 'POST',
                body: form_data,
                headers: {
                    "Accept": "application/json"
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