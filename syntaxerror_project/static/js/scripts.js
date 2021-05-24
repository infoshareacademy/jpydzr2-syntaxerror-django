$(document).ready(function() {
    $('#results_table').DataTable();
} );

$(function () {
  $(document).scroll(function () {
    var $nav = $("#main-nav");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});