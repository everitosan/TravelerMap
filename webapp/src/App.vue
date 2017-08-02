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
@import './styles/main'

</style>
