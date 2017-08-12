<template lang="pug">
  #mainMapScreen
    ErrorAlert
    MainMap
    MapManager
</template>

<script>
import MainMap from '@/components/MainMap'
import MapManager from '@/components/MapManager'
import ErrorAlert from '@/components/ErrorAlert'

export default {
  components: {MainMap, MapManager, ErrorAlert}
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
