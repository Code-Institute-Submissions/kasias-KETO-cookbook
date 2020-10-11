$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.parallax').parallax();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });






