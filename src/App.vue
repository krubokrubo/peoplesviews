<template>
  <div id="app">
    <div id="headbar">
      <div id="logo">
        <a href="/">
          <h3>People's Views</h3>
          <i>A wider range of opinions</i>
        </a>
      </div>
      <PollQuestion :title="title" />
    </div>
    <PollVoting :rankedchoices="myVote" :pollid="pollId" />
    <PollResults
      :candidates="candidates"
      @choose-candidate="chooseCandidate($event)" />
  </div>
</template>

<script>
//  <PollResults :candidates="candidates" @choose-candidate="alert('chose candidate with id '+$event.id)" />
import axios from 'axios'
import PollQuestion from './components/PollQuestion.vue'
import PollVoting from './components/PollVoting.vue'
import PollResults from './components/PollResults.vue'

export default {
  name: 'app',
  components: {
    PollQuestion,
    PollVoting,
    PollResults
  },
  data: function() {
    return {
      pollId: window.location.pathname.substring(3),
      title: 'Loading question...',
      candidates: [],
      myVote: []
    }
  },
  mounted: function() {
    axios
      .get('/api/poll/'+this.pollId+'.json')
      .then(response => (this.title = 'Q: '+response.data.title))
    axios
      .get('/api/candidate.json?poll='+this.pollId)
      .then(response => (this.candidates = response.data))
  },
  methods: {
    chooseCandidate: function(candidate) {
      this.myVote.push(candidate)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#headbar {
  background: cyan;
}
#logo {
  float: left;
  width: 200px;
  text-align: left;
}
#logo h3 {
  margin: 0px;
  font-family: Times;
  text-decoration: none;
}
</style>
