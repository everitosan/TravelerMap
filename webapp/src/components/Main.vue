<template lang="pug">
  #mainMapScreen
    MainMap
    MapManager
</template>

<script>
import MainMap from '@/components/MainMap'
import MapManager from '@/components/MapManager'

export default {
  components: {MainMap, MapManager}
}
</script>

<style lang="stylus" scoped>
#mainMapScreen
  position: fixed
  top: 0
  left: 0
  height: 100vh
  width: 100%
</style>
