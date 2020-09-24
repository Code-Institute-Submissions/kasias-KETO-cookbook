$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    
  });



$("#delete-this").click(function(){
    if(confirm("Are you absolutely sure you want to delete this?")){
        $("#delete-this").attr("href", "query.php?ACTION=delete&ID='1'");
    }
    else{
        return false;
    }
});

