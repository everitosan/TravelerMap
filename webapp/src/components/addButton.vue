<template lang="pug">
.addButton
  span +
  | Agregar
</template>

<script>
export default {
  name: 'addButton'
}
</script>

<style lang="stylus" scoped>
.addButton
  display: inline-block;
  margin-top: 1em
  cursor: pointer
  transition: all ease 0.3s
  span
    color: #FF0077
    margin-right: 1em
  &:hover
    opacity: 0.8
</style>
