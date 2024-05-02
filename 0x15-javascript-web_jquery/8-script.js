#!/usr/bin/node
/* Fetches and lists the title for all movies by using this
URL: https://swapi-api.alx-tools.com/api/films/?format=json */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(document).ready(function () {
  $.get(url, function (data) {
    data.results.forEach(movie => {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
