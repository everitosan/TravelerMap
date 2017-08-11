<template lang="pug">
.GeoPoint(v-if="!deleted" @click="goToGeoPoint")
  span.dateTime {{geopoint.dateTime | date }}
  div
    img(
      :src="require('../assets/dot.svg')"
      class="dot"
    )
    span {{geopoint.activity}}
    span.buttons
      span.icon-edit
      span.icon-times-rectangle-o(@click="removeGeoPoint")
</template>

<script>
import travelerApi from '../travelerApi'
import moment from 'moment'

export default {
  name: 'GeoPoint',
  props: ['geopoint'],
  filters: {
    date (str) {
      return moment(str).format('LLL')
    }
  },
  data () {
    return {
      deleted: false
    }
  },
  methods: {
    removeGeoPoint (e) {
      travelerApi.geoPoint.removeGeoPoint(this.geopoint.id)
        .then(res => {
          this.deleted = true
        })
        .catch(err => {
          alert(err)
        })
    },
    goToGeoPoint () {
      this.$bus.$emit('goToGeoPoint', this.geopoint.coords)
    }
  }
}
</script>

<style lang="stylus">
.GeoPoint
  transition: all ease 0.3s
  opacity: 1
  .dateTime
    font-size: .5em
    position: relative
    left: 13px
    top: 3px
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
