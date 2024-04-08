<template>
<form @submit.prevent="saveMovie" id="movieForm" ref="movieForm">        
    <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label> 
        <input type="text" name="title" placeholder="Enter movie" class="form-control" /> 
    </div>
    <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label> 
        <input type="text" name="description" placeholder="Enter description" class="form-control"/>             
    </div>
    <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label> 
        <input type="file" name="poster" class="form-control"/>             
    </div>    
            
    <div class="form-group mb-3">
        <button type="submit" name="submit" class="btn btn-primary">Post Movie</button>
    </div>
</form>
</template>
  
<script setup>    
    import { ref, onMounted } from 'vue';
    let csrf_token = ref(""); 
    

    onMounted(() => {
        getCsrfToken();
    });

    function saveMovie() {
        const movieform = document.getElementById('movieForm'); 
        console.log(movieform);
        let form_data = new FormData(movieform);
        
        fetch("/api/v1/movies", { 
            method: 'POST',
            body: form_data,
            headers: { 
                'X-CSRFToken': csrf_token.value 
            }
        }) 
            .then(function (response) { 
                return response.json(); 
            }) 
            .then(function (data) { 
                // display a success message 
                console.log(data); 
            }) 
            .catch(function (error) { 
                console.log(error); 
            });
    }

    function getCsrfToken() { 
        fetch('/api/v1/csrf-token') 
            .then((response) => response.json()) 
            .then((data) => { 
            console.log(data); 
            csrf_token.value = data.csrf_token; 
        }) 
    } 

     /*
    let csrf_token = ref(""); 
    const movieform = null; 
    let form_data = null;

    onMounted(() => {
        getCsrfToken();
        console.log(movieform.value);
        form_data = new FormData(movieform);
    });
 */

</script>
  
<style>    
    /* Add any component specific styles here */
</style>