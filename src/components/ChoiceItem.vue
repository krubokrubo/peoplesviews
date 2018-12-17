<template>
  <li @click="$emit('clicked', choice, arrayindex);">
    {{ choice.title }}
  </li>
</template>

<script>
export default {
  name: 'ChoiceItem',
  props: ['choice', 'arrayindex'],
}
</script>

<style>
</style>
