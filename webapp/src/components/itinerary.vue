<template lang="pug">
.itinerary(@click="gotToItinerary")
  span.year {{itinerary.year}}
  div
    img(
      :src="require('../assets/dot.svg')"
      class="dot"
    )
    | {{itinerary.name}}
</template>

<script>
export default {
  'name': 'itinerary',
  props: ['itinerary'],
  methods: {
    gotToItinerary (ev) {
      this.$store.commit('updateCurrentItinerary', { 'itinerary': this.itinerary })
      this.$store.commit('showIntineraryDetail')
    }
  }
}
</script>

<style lang="stylus" scoped>
.itinerary
  margin: 0.1em auto
  cursor: pointer
  transition: all ease 0.3s
  .year
    font-size: .5em
    position: relative
    left: 13px
    top: 3px
  &:hover
    opacity: 0.65
</style>
