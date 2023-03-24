<template>
  <div class="hello">
    hello world?<br>
    <img src="./img/D0007.jpg">
    <img src="./img/D0008.jpg">
    <img src="./img/D0071.jpg">
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
</style>
