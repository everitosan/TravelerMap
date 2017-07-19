<template lang="pug">
  #MapManager(:class="{minified: minified}")
    .bgimage(:style="bgUnsplashImage")
    .color
      span.hide(v-show="minified" @click="toggleHeight") ↓
      span.hide(v-show="!minified" @click="toggleHeight") ocultar
</template>

<script>
import unsplashAPI from '../unsplashApi'

export default {
  name: 'MapManager',
  methods: {
    toggleHeight: function () {
      this._data.minified = !this._data.minified
      console.log(this._data.minified)
    }
  },
  data () {
    return {
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
  }
}
</script>

<style lang="stylus" scoped>
#MapManager
  border-radius: 10px
  margin-top: 20px
  margin-left: 20px
  height: 90%
  overflow: hidden
  position: relative
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
    span.hide
      cursor: pointer
      position: absolute
      bottom: 0
      right: 0
      text-transform: uppercase
      color: white
      float: right
      margin: .5em 1em
</style>
