#!/usr/bin/node
/* Adds, removes and clears LI elements from a
list when the user clicks: */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
