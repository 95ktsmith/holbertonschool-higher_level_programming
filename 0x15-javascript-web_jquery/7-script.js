const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (data, textStatus) {
  $('#character').text(function (i, origText) {
    return data.name;
  });
});
