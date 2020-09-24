const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  for (let movie = 0; movie < data.count; movie++) {
    $('#list_movies').append('<li>' + data.results[movie].title + '</li>');
  }
});
