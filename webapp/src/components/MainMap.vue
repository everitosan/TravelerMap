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
    this.$bus.$on('updateMap', this.updateMap)
    this.$bus.$on('removeAuxMarker', this.removeAuxMarker)
    this.$bus.$on('cleanMap', this.cleanMap)
  },
  mounted () {
    this.map = new window.google.maps.Map(this.$el, this.initialState)
    this.map.addListener('dblclick', this.handleMapClick)
    this.resetPolyLine()
  },
  data () {
    return {
      addMode: false,
      map: {},
      Polyline: undefined,
      auxMarker: {},
      markers: [],
      initialState: {
        center: {
          lat: 25.129247,
          lng: -49.944949
        },
        zoom: 3,
        styles: MapsTheme
      },
      polylineConfig: {
        strokeColor: '#483553',
        strokeOpacity: 0.6,
        strokeWidth: 2,
        map: this.map
      }
    }
  },
  methods: {
    removeAuxMarker () {
      this.auxMarker.setMap(null)
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
      this.auxMarker = marker
      this.addMode = false
      this.$bus.$emit('addGeopointStep3', coords)
    },
    resetPolyLine () {
      if (this.Polyline !== undefined) {
        this.Polyline.setMap(null)
      }
      this.Polyline = new window.google.maps.Polyline(this.polylineConfig)
      this.Polyline.setMap(this.map)
    },
    cleanMap () {
      this.resetPolyLine()
      this.cleanMarkers()
      this.zoomOutMap()
    },
    centerMapTo (location) {
      this.map.setCenter(location)
      this.map.setZoom(16)
      this.addMode = true
    },
    zoomOutMap () {
      this.map.setZoom(3)
      this.map.setCenter(this.initialState.center)
    },
    goToGeoPoint (coords) {
      let Latlng = {
        lat: parseFloat(coords.split(',')[0]),
        lng: parseFloat(coords.split(',')[1])
      }
      this.map.setCenter(Latlng)
      this.map.setZoom(16)
    },
    updateMap (geopoints) {
      this.cleanMarkers()
      this.resetPolyLine()
      geopoints.forEach((geopoint, index) => {
        let Latlng = {
          lat: parseFloat(geopoint.coords.split(',')[0]),
          lng: parseFloat(geopoint.coords.split(',')[1])
        }

        let marker = this.createMarker(Latlng)
        let latLng = new window.google.maps.LatLng(Latlng.lat, Latlng.lng)
        this.createLine(latLng)

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
    },
    createMarker (coords) {
      return new window.google.maps.Marker({
        position: coords,
        map: this.map,
        animation: window.google.maps.Animation.DROP
      })
    },
    createLine (coords) {
      let path = this.Polyline.getPath()
      path.push(coords)
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
