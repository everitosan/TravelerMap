<template lang="pug">
  #MapManager(:class="{minified: minified}")
    .bgimage(:style="bgUnsplashImage")
    .color
      span.back(v-show="!isStep('ITINERARY_LIST')" @click="showIntineraryList") ←
      span.hide(v-show="minified" @click="toggleHeight") ↓
      span.hide(v-show="!minified" @click="toggleHeight") ocultar

      h2.title(v-show="isStep('ITINERARY_LIST')")  Itinerarios
      h2.title(v-show="isStep('ITINERARY_DETAIL')")  {{currentItinerary.name}}
      h2.title(v-show="isStep('ADD_ITINERARY')")  Agregar Itinerario
      .hDivider
      ItinerariesList(
        v-show="isStep('ITINERARY_LIST')"
        )
      addItinerary(
        v-show="isStep('ADD_ITINERARY')"
        )
      ItineraryDetail(
        v-show="isStep('ITINERARY_DETAIL')"
        )
</template>

<script>
import unsplashAPI from '../unsplashApi'
import ItinerariesList from './ItinerariesList'
import ItineraryDetail from './ItineraryDetail'
import addItinerary from './addItinerary'

export default {
  name: 'MapManager',
  computed: {
    step () {
      return this.$store.state.step
    }
  },
  methods: {
    isStep (stepName) {
      return this.step === stepName
    },
    toggleHeight: function () {
      this._data.minified = !this._data.minified
    },
    showIntineraryList () {
      this.$store.commit('showIntineraryList')
    }
  },
  data () {
    return {
      currentItinerary: {},
      index: 0,
      minified: false,
      bgUnsplashImage: {
        backgroundImage: 'url(https://images.unsplash.com/photo-1483030096298-4ca126b58199?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=)'
      }
    }
  },
  mounted () {
    unsplashAPI.getBackgroundPhoto()
      .then(res => {
        this._data.bgUnsplashImage.backgroundImage = `url(${res})`
      })
      .catch(err => console.log(err))
  },
  components: {ItinerariesList, ItineraryDetail, addItinerary}
}
</script>

<style lang="stylus" scoped>
#MapManager
  border-radius: 10px
  color: white
  font-weight: 100
  margin-top: 20px
  margin-left: 20px
  height: 90%
  overflow: hidden
  position: relative
  text-align: left
  transition: all ease .8s
  width: 320px
  -webkit-box-shadow: 2px 2px 5px 2px rgba(0,0,0,0.5);
  -moz-box-shadow: 2px 2px 5px 2px rgba(0,0,0,0.5);
  box-shadow: 2px 2px 5px 2px rgba(0,0,0,0.5);
  z-index: 1
  &.minified
    height: 65px

  .bgimage
    background-size: cover
    background-position: center
    height: 100%

  .color
    background-color: rgba(121, 45, 139, 0.56)
    height: 100%
    position: absolute
    top: 0
    left: 0
    width: 100%
    span.back
      cursor: pointer
      position: absolute
      left: 10px
      top: 6px
    span.hide
      cursor: pointer
      position: absolute
      bottom: 0
      right: 0
      text-transform: uppercase
      color: white
      float: right
      margin: .5em 1em
  .title
    font-weight: 100
    margin: 1.1em auto 0.3em auto
    text-transform: uppercase
    width: 90%
</style>
