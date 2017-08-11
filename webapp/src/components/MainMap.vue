<template lang="pug">
  #mainmap
</template>

<script>
import MapsTheme from '../googleMapsApi/theme'

export default {
  name: 'MainMap',
  created () {
    this.$bus.$on('goToGeoPoint', this.goToGeoPoint)
    this.$bus.$on('centerMapTo', this.centerMapTo)
    this.$bus.$on('addMarkers', this.addMarkers)
    this.$bus.$on('removeAuxMarker', this.removeAuxMarker)
    this.$bus.$on('cleanMarkers', this.cleanMarkers)
  },
  mounted () {
    this.map = new window.google.maps.Map(this.$el, this.initialState)
    this.map.addListener('dblclick', this.handleMapClick)
  },
  data () {
    return {
      addMode: false,
      map: {},
      auxMarker: [],
      markers: [],
      initialState: {
        center: {
          lat: 25.129247,
          lng: -49.944949
        },
        zoom: 3,
        styles: MapsTheme
      }
    }
  },
  methods: {
    removeAuxMarker () {
      this.auxMarker[0].setMap(null)
    },
    handleMapClick (e) {
      if (!this.addMode) return false

      let latitude = e.latLng.lat()
      let longitude = e.latLng.lng()

      let coords = {
        'lat': latitude,
        'lng': longitude
      }

      let marker = this.createMarker(coords)
      this.auxMarker.push(marker)
      this.addMode = false
      this.$bus.$emit('addGeopointStep3', coords)
    },
    centerMapTo (location) {
      this.map.setCenter(location)
      this.map.setZoom(16)
      this.addMode = true
    },
    goToGeoPoint (coords) {
      let Latlng = {
        lat: parseFloat(coords.split(',')[0]),
        lng: parseFloat(coords.split(',')[1])
      }
      this.map.setCenter(Latlng)
      this.map.setZoom(16)
    },
    addMarkers (geopoints) {
      geopoints.forEach((geopoint, index) => {
        let Latlng = {
          lat: parseFloat(geopoint.coords.split(',')[0]),
          lng: parseFloat(geopoint.coords.split(',')[1])
        }

        let marker = this.createMarker(Latlng)

        if (index === 0) {
          this.centerMapTo(Latlng)
          this.map.setZoom(10)
        }

        this.markers.push(marker)
      })
    },
    cleanMarkers () {
      this.markers.forEach(marker => {
        marker.setMap(null)
      })
      this.markers = []
      this.map.setZoom(3)
      this.map.setCenter(this.initialState.center)
    },
    createMarker (coords) {
      return new window.google.maps.Marker({
        position: coords,
        map: this.map,
        animation: window.google.maps.Animation.DROP
      })
    }
  }
}
</script>

<style lang="stylus" scoped>
#mainmap
  cursor: pointer
  background: #ccc
  height: 100vh
  position: absolute
  left: 0
  width: 100%
  .gmap
    width: 100%
    height: 100%

</style>
