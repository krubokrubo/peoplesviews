<template>
  <div class="main">
    <div class="instructions">
      Select as many views as you like.
      Then move them into the order you prefer.
    </div>
    <ul class="choices chosen">
      <draggable v-model="chosenchoices">
        <ChoiceItem
          v-for="(choice, index) in chosenchoices"
          :key="choice.id"
          :choice="choice"
          :arrayindex="index"
          :ischosen="true"
          @clicked="unchoose">
        </ChoiceItem>
      </draggable>
    </ul>
    <ul class="choices">
      <draggable v-model="choices">
        <ChoiceItem
          v-for="(choice, index) in choices"
          :key="choice.id"
          :choice="choice"
          :arrayindex="index"
          :ischosen="false"
          @clicked="choose">
        </ChoiceItem>
      </draggable>
    </ul>
    <div class="afterchoices">
      <div class="instructions">
        <span>When done, click here:</span>
        <input
          class="submit"
          type="submit"
          value="Submit"
          :disabled="!submitenabled"
          @click="submit"
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import draggable from 'vuedraggable'
import ChoiceItem from './ChoiceItem.vue'

export default {
  name: 'Chooser',
  components: {
    draggable,
    ChoiceItem,
  },
  data () {
    return {
      choices: [],
      chosenchoices: [],
      apichoices: [],
    };
  },
  computed: {
    submitenabled: function() {
      return this.chosenchoices.length != 0;
    },
  },
  mounted: function() {
    this.getAvailableChoices();
  },
  methods: {
    getAvailableChoices: function() {
      axios.get("/api/choice/").then(response => {
        this.apichoices = response.data;
        this.choices = response.data;
      });
    },
    choose: function(choice, index) {
      choice.chosen = true;
      this.chosenchoices.push(this.choices.splice(index, 1)[0]);
    },
    unchoose: function(choice, index) {
      choice.chosen = false;
      this.choices.unshift(this.chosenchoices.splice(index, 1)[0]);
    },
    submit: function() {
      alert('Sorry, the "Submit" function hasn\'t been built yet. Hopefully it will work later.');
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .main {
    max-width: 800px;
    margin: 0px auto 0px auto;
    padding: 20px 0px 20px 0px;
    border-radius: 12px;
    background: #aa9422;
    border: 5px outset #400;
  }
  .instructions {
    padding: 20px 20px 20px 20px;
    background: #cef;
    color: #730;
    font-size: 15pt;
    font-style: italic;
    text-align: center;
  }
  .afterchoices .instructions {
    margin: 30px 0px 30px 0px;
    padding: 5px 20px 5px 20px;
  }
  .submit {
    width: 140px;
    height: 50px;
    border-radius: 5px;
    border: 3px outset #aa9422;
    vertical-align: middle;
    background: #aa9422;
    color: #444;
    font-size: 15pt;
    font-weight: bold;
  }
  .submit[disabled] {
    color: #777;
  }
  ul.choices {
    list-style-type: none;
    margin: 0px auto 0px auto;
    padding: 0px;
    max-width: 600px;
  }
  ul.choices li {
    margin: 15px;
    padding: 8px;
    border-radius: 12px;
    border: 5px outset #33c;
    font-size: 15pt;
    background: #cef;
    color: #730;
  }
  ul.choices li.chosen {
    background: #33c;
    color: #ffe;
  }
</style>
