<template lang="pug">
#addItinerary.container
  form
    div.input.col-8
      input(type="text",  required)
      label Nombre

    div.input.col-4
      input(type="number", max="9999" required)
      label Año
</template>

<script>
export default {
  name: 'addItinerary'
}
</script>

<style lang="stylus" scoped>
#addItinerary
  form
    display: flex
    padding: 1em 0
  .col-8
    flex: .6
  .col-4
    flex: .4
  .input
    position: relative;
    height: 45px
    label
      text-transform: uppercase
      font-size: 12px
      position: absolute
      left: 0
      bottom: 2px
      font-weight: 100
      transition: all 0.4s ease-in-out
    input
      width: 90%
      background: transparent
      border: none
      border-bottom: 1px solid rgba(255, 255, 255, .71)
      color: white
      font-size: 14px
      font-weight: 100
      position: absolute
      bottom: 0
      &:focus, &:valid
        outline: none
        & ~ label
          font-size: 8px
          bottom: 24px
</style>
