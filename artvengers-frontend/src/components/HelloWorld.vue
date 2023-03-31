<template>
  <div class="hello">
    Discover more passion of your art. Empower your imagination. Get to know
    your art today.
    <router-link :to="{ path: './components/Login.vue' }"><button>Login</button></router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
img{
  width: 60%;
}
div{
  font-size: 30px;
}
</style>
