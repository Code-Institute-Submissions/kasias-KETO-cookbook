$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.parallax').parallax();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
        format: "dd/mm/yy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });






