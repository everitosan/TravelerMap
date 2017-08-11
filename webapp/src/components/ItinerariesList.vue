<template lang="pug">
#Itineraries
  itinerary(
    v-for="itinerary in itineraries"
    :key="itinerary.id"
    v-show="!isEmpty()"
    :itinerary="itinerary")
  div(v-show="isEmpty()")
    p No existen itinerarios, comienza tu aventura.
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
  created () {
    this.$bus.$on('add-itinerary-to-list', (itinerary) => {
      this.itineraries.push(itinerary)
    })
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
      this.$store.commit('ShouldShowBottomButtons', false)
    },
    isEmpty () {
      return this.itineraries.length === 0
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
</style>
