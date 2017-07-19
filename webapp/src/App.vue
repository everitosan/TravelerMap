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
body
  margin: 0
#app
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #2c3e50
</style>
