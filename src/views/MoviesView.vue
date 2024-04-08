<script setup>
    import { ref, onMounted } from "vue"; 
    import Card from "@/components/Card.vue";

    let movies = ref([]); 

    onMounted(() => {
        fetchMovies();
    });

    function fetchMovies() {
        fetch("/api/v1/movies", { 
            method: 'GET',
        }) 
            .then(function (response) { 
                return response.json(); 
            }) 
            .then(function (data) { 
                movies.value = data.data;
                console.log(data); 
            }) 
            .catch(function (error) { 
                console.log(error); 
            });
    }
</script>

<template>    
    <main class="container py-5">
        <h1>Movies</h1>
        <hr>
        <div id="movies">
            <Card :movie="movie" v-for="movie in movies" :key="movie.id" />
        </div>
    </main>
</template>
  
<style>
    /* Add any component specific styles here */
    #movies {
        display: grid;
        gap: 30px 30px;
        grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);  
        padding: 15px 0px 15px 0px;
    }

</style>