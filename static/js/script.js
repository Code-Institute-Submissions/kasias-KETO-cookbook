$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    
  });



$("#edit").click(function(){
    if(confirm("Are you absolutely sure you want to delete this?")){
        $("#edit").attr("href", "query.php?ACTION=delete&ID='1'");
    }
    else{
        return false;
    }
});

