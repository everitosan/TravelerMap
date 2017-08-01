<template lang="pug">
#Itineraries
  itinerary(
    v-for="itinerary in itineraries"
    :key="itinerary.id"
    :itinerary="itinerary")
  span(@click="showAddItinerary")
    addButton
</template>

<script>
import travelerApi from '../travelerApi'
import itinerary from './itinerary'
import addButton from './addButton'

export default {
  'name': 'ItinerariesList',
  data () {
    return {
      itineraries: []
    }
  },
  mounted () {
    travelerApi.itinerary.getItineraies()
      .then(json => {
        this.itineraries = json
      })
      .catch(err => console.log(err))
  },
  methods: {
    showAddItinerary (ev) {
      this.$store.commit('showAddItinerary')
    }
  },
  components: {itinerary, addButton}
}
</script>

<style lang="stylus" scoped>
#Itineraries
  color: white
  margin: 0.1em auto
  text-align: left
  width: 85%
</style>
