<template lang="pug">
#Itineraries
  itinerary(
    v-for="itinerary in itineraries"
    :key="itinerary.id"
    :itinerary="itinerary"
    v-on:gotToItinerary="gotToItinerary")
</template>

<script>
import travelerApi from '../travelerApi'
import itinerary from './itinerary'

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
  components: {itinerary},
  methods: {
    gotToItinerary (itineraryInfo) {
      this.$emit('gotToItinerary', itineraryInfo)
    }
  }
}
</script>

<style lang="stylus" scoped>
#Itineraries
  color: white
  text-align: left
</style>
