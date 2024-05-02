#!/usr/bin/nod
/* Fetches and prints how to say “Hello” depending
on the language */
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#btn_translate').click(function () {
    $('#hello').empty();
    const lang = $('#language_code').val();
    $.get(url + lang, function (data) {
      $('#hello').append(data.hello);
    });
  });
});
