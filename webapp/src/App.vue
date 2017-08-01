<template lang="pug">
  #app
    router-view
</template>

<script>
import api from './travelerApi'

export default {
  name: 'app',
  data () {
    return {
      items: []
    }
  },
  mounted () {
    api.itinerary.getItineraies()
      .then(itineraries => {
        this.items = itineraries
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style lang="stylus">
@import './assets/icomoon/style'
body
  margin: 0
#app
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #2c3e50
.hDivider
  background: rgba(98,76,158, 0.64)
  margin: 0 auto
  height: 1px
  width: 90%
.dot
  bottom: 2px
  margin-right: 5px
  position: relative
  width: 6px
.container
  margin: 0 auto
  width: 85%
</style>
