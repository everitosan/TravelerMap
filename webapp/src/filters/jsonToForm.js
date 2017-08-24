const jsonToForm = {}

function convertToForm (obj) {
  let form = new FormData()
  for (let key in obj) {
    form.append(key, obj[key])
  }
  return form
}

jsonToForm.install = function (Vue) {
  Vue.filter('json-to-form', convertToForm)
}

export default jsonToForm
