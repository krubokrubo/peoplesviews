<template>
  <li
    v-bind:class="{ chosen: ischosen }"
    @click="$emit('clicked', choice, arrayindex);">
    <span v-if="ischosen">
      {{ arrayindex + 1 }}.
    </span>
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
