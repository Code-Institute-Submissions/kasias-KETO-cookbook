$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    
  });



$("#delete").click(function(){
    if(confirm("Are you absolutely sure you want to delete this?")){
        $("#delete").attr("href", "query.php?ACTION=delete&ID='1'");
    }
    else{
        return false;
    }
});

