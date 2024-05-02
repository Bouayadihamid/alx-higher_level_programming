#!/usr/bin/node
/* Fetches the character name from this
URL: https://swapi-api.alx-tools.com/api/people/5/?format=json */
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(document).ready(function () {
  $.get(url, function (data) {
    $('#character').text(data.name);
  });
});
