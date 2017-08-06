<template lang="pug">
#itinerary-detail
  .list
    div(class="geopoint" v-for="geopoint in geopoints")
      span.dateTime {{geopoint.dateTime | date }}
      div
        img(
          :src="require('../assets/dot.svg')"
          class="dot"
        )
        span {{geopoint.activity}}
        span.buttons
          span.icon-edit
          span.icon-times-rectangle-o
    div(v-show="isGeopintsEmpty()")
      p No existen puntos a visitar en el itinerario

    span(@click="showAddGeoPoint")
      addButton
  .add
</template>

<script>
import travelerApi from '../travelerApi'
import addButton from './addButton'
import moment from 'moment'

export default {
  name: 'ItineraryDetail',
  filters: {
    date (str) {
      return moment(str).format('LLL')
    }
  },
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
          console.log(err)
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
    }
  },
  components: {addButton}
}
</script>

<style lang="stylus" scoped>
.list
  cursor: pointer
  .dateTime
    font-size: .5em
    position: relative
    left: 13px
    top: 3px
  .geopoint
    transition: all ease 0.3s
    opacity: 1
    .buttons
      float: right
      display: none
      span
        opacity: 0.5
        margin-left: 1em
        &:hover
          opacity: 1
    &:hover
      opacity: 0.8
    &:hover .buttons
      display: block

</style>
