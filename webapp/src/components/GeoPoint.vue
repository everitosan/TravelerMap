<template lang="pug">
.GeoPoint(v-if="!deleted")
  span.dateTime {{geopoint.dateTime | date }}
  .geopoint-container
    img(
      :src="require('../assets/dot.svg')"
      class="dot"
    )
    .geopoint-activity(@click="goToGeoPoint") {{geopoint.activity}}
    span.buttons
      span.icon-document-edit-dark
      span.icon-note-checked-dark(@click="showNotes")
      span.delete.icon-trash-dark(@click="confirm")
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
    showNotes (e) {
      this.$bus.$emit('showNotes', this.geopoint)
    },
    confirm (e) {
      this.$bus.$emit(
        'showErrorConfirm', {
          title: 'Eliminar !',
          message: `Estas seguro que deas eliminar "${this.geopoint.activity}" de la lista ?`
        },
        this.removeGeoPoint
      )
    },
    removeGeoPoint () {
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
@import '../styles/colors'
@import '../styles/measures'

.GeoPoint
  transition: all ease 0.3s
  opacity: 1
  .geopoint-container
    position: relative
    .dot
      position: absolute
      top: 8px
  .geopoint-activity
    position: relative
    left: 10px
    width: 70%
  .dateTime
    font-size: .5em
    position: relative
    left: 13px
    top: 3px
  .buttons
    position: absolute
    top: 2px
    right: 0
    display: none
    span
      opacity: 0.5
      margin-left: 0.5em
      &:hover
        opacity: 1
      &.delete:hover
        color: accent-color
  &:hover
    opacity: 0.8
  &:hover .buttons
    display: block
@media screen and (max-width: $md-up)
  .GeoPoint
    .buttons
      display: block
</style>
