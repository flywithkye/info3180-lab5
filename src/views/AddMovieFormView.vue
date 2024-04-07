<script setup>
    import MovieForm from '@/components/MovieForm.vue';
</script>

<template>    
    <div class="formbox">
        <h1>Submit A Movie</h1>
        <MovieForm />   
    </div> 
</template>
  
<style>
    /* Add any component specific styles here */
    .formbox {
        display: flex;
        flex-direction: column;
        width: 50%;
        margin: auto;
    }

    h1 {
        font-size: 32px;
        margin-bottom: 30px;
    }
</style>