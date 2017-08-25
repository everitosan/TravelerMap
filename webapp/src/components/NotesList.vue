<template lang="pug">
.NotesList(:class="{'active': active }")
  .header
    h3 Notas
    .date
      .day {{date.day}}
      .other
        .weekDay {{date.weekDay}}
        .month {{date.month}}
        .hour {{date.hour}}
  .hDivider
  .notesList
    .note(v-for="note in notes")
      .dot
      .text {{note.content}}
    .newNote(v-show="showNewInput")
      .dot
      input(
        type="text"
        v-model="newNote"
        placeholder="Escribe tu nota ..."
        autofocus
        @keydown.enter="postNote")
    span(@click="addNote")
      addButton
  .light_button.hide(@click="toggleNotes") ocultar
</template>

<script>
import addButton from './addButton'
import travelerApi from '../travelerApi'
export default {
  name: 'NotesList',
  created () {
    this.$bus.$on('showNotes', this.showNotes)
  },
  data () {
    return {
      showNewInput: false,
      active: false,
      newNote: '',
      geopoint: {},
      date: {
        day: '6',
        weekDay: 'martes',
        month: 'junio',
        hour: '10:00'
      },
      notes: []
    }
  },
  methods: {
    showNotes (geopoint) {
      this.geopoint = geopoint
      travelerApi.geoPoint.getNotes(geopoint.id)
      .then(res => {
        this.notes = res
        this.active = true
      })
    },
    postNote () {
      let note = {
        content: this.newNote
      }
      travelerApi.geoPoint.addNote(this.geopoint.id, note)
      .then(res => {
        this.notes.push(res)
        this.newNote = ''
        this.showNewInput = false
      })
      .catch(err => {
        this.$bus.$emit('showErrorAlert', {message: err.message})
      })
    },
    toggleNotes () {
      this.active = !this.active
    },
    addNote (e) {
      this.showNewInput = true
    }
  },
  components: { addButton }
}
</script>

<style lang="stylus" scoped>
@import '../styles/colors'
@import '../styles/measures'

.NotesList
  border-radius: 0 10px 10px 0
  background: white
  position: absolute
  z-index: 2
  top: 44px
  height: 80%
  text-align: left
  left: 20px
  padding: 0 1em
  width: 300px
  transition: all ease .3s
  opacity: 0
  &.active
    box-shadow: 0 0 5px 2px #b9b9b9
    opacity: 1
    left: 360px
  .header
    padding-top: 8px
    display: flex
    justify-content: space-between
    .date
      display: flex
      .day
        font-size: 64px
        line-height: 1
      .other
        position: relative
        top: 6px
        display: flex
        flex-direction: column
        align-items: center
        text-transform: uppercase
        line-height: 15px
        .weekDay
          font-size: 10.5px
        .month
          font-size: 16px
        .hour
          font-size: 17px
          position: relative
          top: 2px
  h3
    text-transform: uppercase
    font-size: 44px
    color: black-color
    margin: 10px 0
    line-height: 1
    font-weight: 100

  .hDivider
    background: black-color
    width: 100%

  .addButton
    color: black-color

  .newNote
    input
      border: none
      border-bottom: 1px solid black-color
      &:focus
        outline: none

  .hide
    text-transform: uppercase
    color: black-color
    position: absolute
    right: 10px
    bottom: 10px
  .dot
    display: inline-block
    background: #4977D1
    border-radius: 50%
    height: 5px
    width: 5px
  .notesList
    padding: 1em 0
  .note
    display: flex
    align-items: center
    padding: 0.4em 0
@media screen and (max-width: $md-up)
  .NotesList
    left: -110%
    height: 87%
    width: 86%
    &.active
      top: 20px
      left: 0
      z-index: 4
</style>
