<template>
  <firstPage></firstPage>
</template>

<script>
import firstPage from './components/firstPage.vue'
export default {
  name: 'App',
  components: {
    firstPage: firstPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
