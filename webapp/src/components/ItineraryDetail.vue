<template lang="pug">
#itinerary-detail
  .list
    div(class="geopoint" v-for="geopoint in geopoints")
      GeoPoint(:geopoint="geopoint")

    div(v-show="isGeopintsEmpty()")
      p No existen puntos a visitar en el itinerario

    span(@click="showAddGeoPoint")
      addButton
  .add
</template>

<script>
import travelerApi from '../travelerApi'
import addButton from './addButton'
import GeoPoint from './GeoPoint'

export default {
  name: 'ItineraryDetail',

  data () {
    return {
      geopoints: [],
      hover: false
    }
  },
  created () {
    this.$bus.$on('addGeoPointToList', this.addGeoPointToList)
  },
  computed: {
    itinerary () {
      return this.$store.state.currentItinerary
    }
  },
  watch: {
    itinerary: function () {
      this.getItineraryInfo()
    },
    geopoints: function () {
      this.$bus.$emit('updateMap', this.geopoints)
    }
  },
  methods: {
    getItineraryInfo: function () {
      if (this.itinerary.id === 0) return false
      travelerApi.itinerary.getItineraryGeopoints(this.itinerary.id)
        .then(res => {
          this.geopoints = res
        })
        .catch(err => {
          this.$bus.$emit('showErrorAlert', {message: err.message})
        })
    },
    isGeopintsEmpty () {
      return (this.geopoints.length === 0)
    },
    showAddGeoPoint () {
      this.$store.commit('ShouldShowBottomButtons', false)
      this.$store.commit('showAddGeoPoint')
    },
    addGeoPointToList (geopoint) {
      this.geopoints.push(geopoint)
      this.orderGepoints()
    },
    orderGepoints () {
      this.geopoints = this.geopoints.sort((a, b) => {
        if (a.dateTime > b.dateTime) {
          return 1
        } else if (a.dateTime < b.dateTime) {
          return -1
        } else {
          return 0
        }
      })
    }
  },
  components: {addButton, GeoPoint}
}
</script>

<style lang="stylus" scoped>
.list
  cursor: pointer
</style>
