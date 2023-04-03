<template>
    <div class="fistPage">
    <h1>Artvenger</h1>
      Discover more passion of your art. Empower your imagination. Get to know
    your art today.
    <br>
    <br>
    <br>
    <button>Login</button>
    <br><br>
    <button>Register a new account</button>
    </div>
</template>

<script>
export default {
  name: 'firstPage',
  props: {
    data: String,
    msg: String
  }
}
</script>

<style>
button{
  background-color: grey;
  color: white;
  
}
</style>
