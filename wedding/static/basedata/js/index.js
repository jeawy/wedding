$(document).ready(function() {
	$(".username").each(function(){
    $(this).text($(this).text().replace(/^(.).*(.)$/,"$1**$2"));
  }); 
});