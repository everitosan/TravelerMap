<template lang="pug">
  #mainmap
</template>

<script>
import MapsTheme from '../googleMapsApi/theme'

export default {
  name: 'MainMap',
  created () {
    this.$bus.$on('centerMapTo', this.centerMapTo)
  },
  mounted () {
    this.map = new window.google.maps.Map(this.$el, this.initialState)
    this.map.addListener('dblclick', this.handleMapClick)
  },
  data () {
    return {
      addMode: false,
      map: {},
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
    handleMapClick (e) {
      if (!this.addMode) return false
      let coords = {
        'lat': e.latLng.lat(),
        'lng': e.latLng.lng()
      }
      let marker = new window.google.maps.Marker({
        position: e.latLng,
        map: this.map,
        animation: window.google.maps.Animation.DROP
      })

      this.markers.push(marker)
      this.addMode = false
      this.$bus.$emit('addGeopointStep3', coords)
    },
    centerMapTo (location) {
      this.map.setCenter(location)
      this.map.setZoom(16)
      this.addMode = true
    }
  }
}
</script>

<style lang="stylus" scoped>
#mainmap
  background: #ccc
  height: 100vh
  position: absolute
  left: 0
  width: 100%
  .gmap
    width: 100%
    height: 100%

</style>
