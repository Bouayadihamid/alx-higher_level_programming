#!/usr/bin/node
/* Changes the color of an element by id. */
$(document).ready(function () {
  $('#red_header').click(function () {
    $("header").css('color', '#FF0000');
  });
});
