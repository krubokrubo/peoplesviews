<template>
  <li
    v-bind:class="{ chosen: ischosen }"
    @click="$emit('clicked', choice, arrayindex);">
    {{ choice.title }}
  </li>
</template>

<script>
export default {
  name: 'ChoiceItem',
  props: ['choice', 'arrayindex', 'ischosen'],
}
</script>

<style>
</style>
