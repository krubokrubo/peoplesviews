<template>
  <div id="results">
    <h4>Most popular answers so far</h4>
    <p>Poll results are supposed to go here, showing other people's answers that you can click</p>
  </div>
</template>

<script>
export default {
  name: 'PollResults',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div#results {
  background: #dfd;
  min-height: 500px;
  text-align: left;
  padding: 25px;
}
</style>
