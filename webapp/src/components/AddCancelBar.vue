<template lang="pug">
.AddCancelBar
  .light_button(@click="cancelFn")
    span.icon-close2
    | Cancelar

  .light_button(@click="acceptFn")
    span.icon-check
    button.light_button Aceptar
</template>

<script>
export default {
  name: 'addCancelBar',
  props: {
    accept: {
      type: Function,
      default: function () {
        return function () {

        }
      }
    },
    cancel: {
      type: Function,
      default: function () {
        return function () {

        }
      }
    }
  },
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
  justify-content: space-between
  padding: 0 0.5em
.light_button
  margin-top: 0
</style>
