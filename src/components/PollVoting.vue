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
   <p v-show="!showAddInput" @click="doShowAddInput" class="click-show-add">
     add a new answer
   </p>
   <input v-show="showAddInput"
          v-model="addInput"
          @change="addCandidate"
          :ref="'addinput'">
   <p v-if="rankedchoices.length > 0" class="submit-vote">
     Sorry, there still isn't a way to submit your vote yet...
   </p>
 </div>
</template>

<script>
export default {
  name: 'PollVoting',
  props: ['rankedchoices'],
  data: function() {
    return {
      'addInput': '',
      'showAddInput': false
    }
  },
  methods: {
    addCandidate: function() {
      var newCandidate = {}
      newCandidate.title = this.addInput
      newCandidate.id = 404
      this.rankedchoices.push(newCandidate)
//    alert('about to reset addInput and showAddInput')
      this.showAddInput = false
      this.addInput = ''
    },
    doShowAddInput: function() {
      this.showAddInput = true
      this.$nextTick(() => {
        this.$refs.addinput.focus()
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
