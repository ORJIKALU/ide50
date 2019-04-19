$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight'); 
			} else {
		    label.removeClass('highlight');   
			}   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
    		label.removeClass('highlight'); 
			} 
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a,.links a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});

addEventListener("load", function() { 
  setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } 
  
addEventListener("load", function() 
{ setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } 

$(function() {
    $('#login').bind('click', function() {
  // Stop form from submitting normally
  event.preventDefault();
  if($('input[name="username"]').val() == ""){
    alert("you must provide a username");
  }
  
 else if($('input[name="password"]').val() ==""){
    alert("you must provide a password");
  }
 else{
      $.post( $SCRIPT_ROOT + '/login_check',{
        username: $('input[name="username"]').val(),
        password: $('input[name="password"]').val()
      }, function(data) {
          if (data == "fail"){alert("invalid username or password")}
          else{
            $("#var1").val(data.username);
            $("#var2").val(data.password);
            $("#form").submit();
          }
      });}
    });
  });