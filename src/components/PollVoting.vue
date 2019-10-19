<template>
  <div id="pollvoting">
   <h3>What Are Your Views?</h3>
   <p v-if="rankedchoices.length == 0">
     Click your favorite answers or
   </p>
   <ol class="ranked-choices">
     <li v-for="candidate in rankedchoices" :key="candidate.id">
       {{ candidate.title }}
     </li>
   </ol>
   <p v-if="addInputState == 'hidden'"
       @click="showAddInput"
       class="click-show-add"
     >
     add a new answer
   </p>
   <input v-if="addInputState != 'hidden'"
          :disabled="addInputState == 'working'"
          :ref="'addinput'"
          v-model="addInput"
          @change="addCandidate"
     >
   <p v-if="rankedchoices.length > 0" class="submit-vote">
     Got all your views?<br>
     <button @click="submitVote">
       Submit your views now
     </button>
   </p>
 </div>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

export default {
  name: 'PollVoting',
  props: [
    'pollid',
    'rankedchoices'
  ],
  data: function() {
    return {
      'addInput': '',
      'addInputState': 'hidden'
    }
  },
  methods: {
    addCandidate: function() {
      this.addInputState = 'working'
      axios.post('/api/candidate.json', {
          poll: this.pollid,
          title: this.addInput
        })
        .then(response => {
          var newCandidate = {}
          newCandidate.title = response.data.title
          newCandidate.id = response.data.id
          this.rankedchoices.push(newCandidate)
          this.addInputState = 'hidden'
          this.addInput = ''
        })
    },
    showAddInput: function() {
      this.addInputState = 'open'
      this.$nextTick(() => {
        this.$refs.addinput.focus()
      })
    },
    submitVote: function() {
      var rankingString = this.rankedchoices.map(x => x.id).join(',')
      axios.post('/api/vote.json', {
          poll: this.pollid,
          ranked_choices: rankingString
        })
        .then(response => {
          alert('Vote submitted! '+response.data.id)
          window.location.reload()
        })
        .catch(error => {
          alert(error.response)
        })
    }
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
.click-show-add {
  text-decoration: underline;
  color: blue;
}
.ranked-choices {
  text-align: left;
}
.submit-vote {
  margin-top: 50px;
}
</style>
