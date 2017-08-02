<template lang="pug">
.AddCancelBar
  .light_button(@click="cancelFn")
    span.icon-close2
    | Cancelar

  .light_button(@click="acceptFn")
    span.icon-check
    | Aceptar
</template>

<script>
export default {
  name: 'addCancelBar',
  props: ['cancel', 'accept'],
  methods: {
    cancelFn () {
      this.cancel()
    },
    acceptFn () {
      this.accept()
    }
  }
}
</script>

<style lang="stylus" scoped>
.AddCancelBar
  display: block
  display: flex
  justify-content: space-around
</style>
