<template>
  <div>
    <h1>{{ title }}</h1>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'PollQuestion',
  data (){
    return {
      title: 'Loading...',
      currentRoute: window.location.pathname,
      pollId: window.location.pathname.substring(3)
    };
  },
  mounted: function (){
    axios
      .get('/api/poll/'+this.pollId+'.json')
      .then(response => (this.title = response.data.title));
  }
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
