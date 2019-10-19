<template>
  <div id="results">
    <h4>Most popular answers so far</h4>
    <p>Poll results are supposed to go here, showing other people's answers that you can click...</p>
    <h4>All submitted answers so far</h4>
    <div class="answerbuttons">
      <div v-for="candidate in candidates" v-item="candidate" :key="candidate.id" @click="$emit('choose-candidate', candidate)" class="answerbutton">
        {{ candidate.title }}        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PollResults',
  props: ['candidates'],
  methods: {
    chooseCandidate2: function(candidate) {
      alert('chose candidate id '+candidate.id)
    }
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
.answerbuttons {
  display: flex;
}
.answerbutton {
  border: 4px outset gray;
  width: 18%;
  min-width: 150px;
  max-width: 300px;
  margin: 10px;
}
</style>
