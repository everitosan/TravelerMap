<template lang="pug">
  form(
    novalidate
    :class="{ 'dirty': dirty}"
    on:submit="onSubmit"
    @submit="validate")
    slot
</template>

<script>
export default {
  name: 'customForm',
  props: ['submit'],
  data () {
    return {
      dirty: false
    }
  },
  methods: {
    validate () {
      this.dirty = true
      let invalid = this.$el.querySelectorAll('input:invalid')
      if (invalid.length !== 0) return false
      this.submit()
    }
  }
}
</script>

<style lang="stylus" scoped>
</style>
