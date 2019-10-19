<template>
  <div id="pollvoting">
   <h3>What Are Your Views?</h3>
   <p>Click your favorite answers or
     <a>add a new answer</a>
   </p>
 </div>
</template>

<script>
export default {
  name: 'PollVoting',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div#pollvoting {
  float: left;
  width: 25%;
  padding: 10px;
  margin-right: 25px;
  background: orange;
  min-height: 500px;
}
</style>
