export default function (json) {
  let form = new FormData()
  for (let key in json) {
    form.append(key, json[key])
  }
  return form
}
