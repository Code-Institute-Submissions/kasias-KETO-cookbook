$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.parallax').parallax();
  });



$("#delete-this").click(function(){
    if(confirm("Are you absolutely sure you want to delete this?")){
        $("#delete-this").attr("href");
    }
    else{
        return false;
    }
});



