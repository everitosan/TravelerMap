<template lang="pug">
  #mainmap
</template>

<script>
import MapsTheme from '../googleMapsApi/theme'

export default {
  name: 'MainMap',
  mounted () {
    this.map = new window.google.maps.Map(this.$el, this.initialState)
    this.map.addListener('click', this.handleMapClick)
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

      let marker = new window.google.maps.Marker({
        position: e.latLng,
        map: this.map
      })

      this.markers.push(marker)
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
