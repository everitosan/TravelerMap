<template lang="pug">
#addItinerary
  form(:class="{ 'dirty': dirty}")
    .row
      .col-xs-8
        .input
          input(type="text", required, v-model="itineraryInfo.name")
          label Nombre

      .col-xs-4
        .input
          input(type="number", min="2017", max="9999", required, v-model="itineraryInfo.year")
          label Año
  add-cancel-bar(:cancel="goBack", :accept="accept")
</template>

<script>
import AddCancelBar from './AddCancelBar'
import travelerApi from '../travelerApi'

export default {
  name: 'addItinerary',
  data () {
    return {
      dirty: false,
      itineraryInfo: {}
    }
  },
  methods: {
    goBack () {
      this.dirty = false
      this.$store.commit('showIntineraryList')
      this.itineraryInfo = {}
      this.$store.commit('ShouldShowBottomButtons', true)
    },
    accept () {
      this.dirty = true
      let invalid = this.$el.querySelectorAll('input:invalid')
      if (invalid.length !== 0) return false

      travelerApi.itinerary.createItinerary(this.itineraryInfo)
        .then(res => {
          this.$bus.$emit('add-itinerary-to-list', res)
          this.goBack()
        })
        .catch(error => {
          this.$bus.$emit('showErrorAlert', error)
        })
    }
  },
  components: { AddCancelBar }
}
</script>

<style lang="stylus" scoped>
@import '../styles/colors'
@import '../styles/flexboxgrid'


#addItinerary
  form
    padding: 1em 0
  .input
    position: relative;
    height: 45px
    label
      text-transform: uppercase
      font-size: 12px
      position: absolute
      left: 0
      bottom: 2px
      font-weight: 100
      transition: all 0.4s ease-in-out
    input
      width: 100%
      background: transparent
      border: none
      border-bottom: 1px solid rgba(255, 255, 255, .71)
      color: white
      font-size: 14px
      font-weight: 100
      position: absolute
      bottom: 0
      &:focus, &:valid
        outline: none
        & ~ label
          font-size: 8px
          bottom: 24px
  .dirty
    .input
      input:invalid
        border-color: accent-color
        color: accent-color
        & ~ label
          color: accent-color
          font-size: 8px
          bottom: 24px
</style>
