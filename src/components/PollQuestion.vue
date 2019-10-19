<template>
  <div>
    <h1>{{ title }}</h1>
  </div>
</template>

<script>
export default {
  name: 'PollQuestion',
  props: ['title']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  margin: 0;
  min-height: 150px;
  background: #aaeeff;
  display: flex;
  align-items: center;
}
</style>
