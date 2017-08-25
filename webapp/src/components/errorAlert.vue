<template lang="pug">
transition(name="fadeBox")
  .ErrorBg(v-show="shouldShow")
    transition(name="bounce")
      .popUp(v-show="shouldShow")
        h3.title {{content.title}}
        .Message
          p {{content.message}}
        .footer(v-show="isType('alert')")
          span.dismiss(@click="dismiss") Aceptar
        .footer.confirm(v-show="isType('confirm')")
          span.dismiss(@click="dismiss") Cancelar
          span.dismiss(@click="callback") Aceptar
</template>

<script>
export default {
  name: 'ErrorAlert',
  data () {
    return {
      type: 'alert',
      shouldShow: false,
      default: {
        title: 'Error !',
        message: 'There was a problem ...'
      },
      content: {},
      customCallback: {}
    }
  },
  created () {
    this.$bus.$on('showErrorAlert', this.showErrorAlert)
    this.$bus.$on('showErrorConfirm', this.showConfirmAlert)
  },
  methods: {
    isType (type) {
      return this.type === type
    },
    showErrorAlert (errorInfo = {title: 'Error'}) {
      this.type = 'alert'
      this.content.title = errorInfo.title || this.default.title
      this.content.message = errorInfo.message
      this.shouldShow = true
    },
    dismiss () {
      this.shouldShow = false
    },
    showConfirmAlert (info, callback) {
      this.type = 'confirm'
      this.customCallback = callback
      this.content = info
      this.shouldShow = true
    },
    callback () {
      this.customCallback()
      this.dismiss()
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../styles/colors'
@import "../styles/measures"

.bounce-enter-active
  animation: bounce-in .4s

.bounce-leave-active
  animation: bounce-in .4s reverse

@keyframes bounce-in
  0%
    transform: scale(0)
  50%
    transform: scale(1.5)
  100%
    transform: scale(1)

.fadeBox-enter-active, .fadeBox-leave-active
  transition: opacity .2s

.fadeBox-enter, .fadeBox-leave-to
  opacity: 0

.ErrorBg
  background-color: rgba(0,0,0,.69)
  display: flex
  justify-content: center
  align-items: center
  position: fixed
  top: 0
  left: 0
  height: 100%
  width: 100%
  z-index: 100
  .popUp
    background: white
    box-sizing: border-box
    border-radius: 10px
    max-width: 450px
    min-width: 200px
    min-height: 100px
    padding: 1em 1em .5em 1em
    .title
      color: primary-color
      text-align: left
      margin: 0
    .footer
      text-align: right
      &.confirm
        display: flex
        justify-content: space-around
      span
        cursor: pointer
        color: accent-color
@media screen and (max-width: $md-up)
  .ErrorBg
    .popUp
      max-width: 90%
</style>
