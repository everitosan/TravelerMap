<template lang="pug">
#addGeopoint
    .step1(v-show="isStep(0)")
      customForm(:submit="findPlace")
        p Ingresa la dirección (aproximada) del lugar.
        .input
          input(type="text" v-model="details.place" required)
          label Dirección
        input.light_button(type="submit" value="Buscar")
    .step2(v-show="isStep(1)")
      p
        | Presiona doble click en el mapa para agregar el marcador en el lugar exacto.
    .step3(v-show="isStep(2)")
      p
        | Agrega los detalles de tu actividad
      customForm(:submit="saveGeopoint")
        .row
          .col-xs-7
            .input
              input(type="text" v-model="details.activity" required)
              label actividad
          .col-xs-5
            .input
              input(type="time" v-model="details.time" required)
              label hora
              span.icon-stop-watch
        .row
          .col-xs-7
            .input
              input(type="text" v-model="details.place" required)
              label lugar
          .col-xs-5
            .input(@click="focusCalendar")
              input(type="date" id="date" v-model="details.date" required)
              label fecha
              span.icon-date
        .row
          .col-xs-12
            AddCancelBar(:cancel="goBack")
</template>

<script>
import MapsAPI from '../googleMapsApi'
import customForm from './customForm'
import AddCancelBar from './AddCancelBar'
import TravelerApi from '../travelerApi'
import moment from 'moment-timezone'

export default {
  name: 'addGeopoint',
  data () {
    return {
      step: 0,
      details: {}
    }
  },
  computed: {
    itineraryId () {
      return this.$store.state.currentItinerary.id
    }
  },
  created () {
    this.$bus.$on('addGeopointStep3', this.getMarkerCoords)
  },
  methods: {
    focusCalendar () {
      this.$el.querySelector('#date').focus()
    },
    isStep (step) {
      return this.step === step
    },
    stepAdd () {
      this.step++
    },
    stepMinus () {
      this.step--
    },
    findPlace () {
      MapsAPI.findAddress(this.details.place)
        .then(res => {
          if (res.status !== 'OK') throw new Error(res.status)
          this.$bus.$emit('centerMapTo', res.results[0].geometry.location)
          this.stepAdd()
        })
        .catch(err => {
          alert(err)
        })
    },
    getMarkerCoords (location) {
      this.details.coords = location.lat + ',' + location.lng
      this.stepAdd()
    },
    saveGeopoint () {
      let nObject = Object.assign({}, this.details)
      let timestamp = Math.floor(
                        Date.parse(nObject.date + 'T' + nObject.time + '+0000') / 1000)

      MapsAPI.getTimeZone(nObject.coords, timestamp)
        .then(res => {
          let ZoneID = res.timeZoneId
          nObject.dateTime = moment.tz(`${nObject.date} ${nObject.time}`, ZoneID).format()
          console.log(nObject)
          return TravelerApi.itinerary.addGeoPoint(this.itineraryId, nObject)
        })
        .then(res => {
          // this.goBack()
          this.$bus.$emit('addGeoPointToList', res)
        })
        .catch(err => {
          alert(err)
        })
    },
    goBack () {
      this.details = {}
      this.step = 0
      this.$store.commit('showIntineraryDetail')
      this.$store.commit('ShouldShowBottomButtons', true)
    }
  },
  components: {customForm, AddCancelBar}
}
</script>

<style lang="stylus" scoped>

@import '../styles/flexboxgrid'

.light_button
  float: right
.AddCancelBar
  margin-top: 2em
</style>
