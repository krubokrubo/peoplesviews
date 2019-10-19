<template>
  <div id="app">
    <div id="headbar">
      <div id="logo">
        <a href="/">
          <h3>People's Views</h3>
          <i>A wider range of opinions</i>
        </a>
      </div>
      <PollQuestion />
    </div>
    <PollVoting />
    <PollResults />
  </div>
</template>

<script>
import PollQuestion from './components/PollQuestion.vue'
import PollVoting from './components/PollVoting.vue'
import PollResults from './components/PollResults.vue'

export default {
  name: 'app',
  components: {
    PollQuestion,
    PollVoting,
    PollResults
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
