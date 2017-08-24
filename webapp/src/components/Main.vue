<template lang="pug">
  #mainMapScreen
    ErrorAlert
    MainMap
    NotesList
    MapManager
</template>

<script>
import MainMap from '@/components/MainMap'
import MapManager from '@/components/MapManager'
import NotesList from '@/components/NotesList'
import ErrorAlert from '@/components/ErrorAlert'

export default {
  components: {MainMap, MapManager, ErrorAlert, NotesList}
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
