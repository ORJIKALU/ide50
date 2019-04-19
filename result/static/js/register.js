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


  function validateEmail(email) {
  var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}

$(function() {
    $('#submit_registration').bind('click', function() {
  // Stop form from submitting normally
  event.preventDefault();
  
  if($('input[name="username"]').val() == ""){
    alert("you must provide a username");
  }
   else if($('input[name="username"]').val() != "") {
      $.post( $SCRIPT_ROOT + '/register_check',{
        username: $('input[name="username"]').val()
      }, function(data) {
          if (data == "false")
          {alert("username already taken")}
          else return;
      });}
  
  if($('input[name="schoolname"]').val() ==""){
    alert("you must provide a school name");
  }
  else if($('input[name="email"]').val() ==""){
    alert("you must provide a email");
  }
  else if(validateEmail($('input[name="email"]').val()) !=true){
    alert("email not valid");
  }
  
  else if($('input[name="admin_password"]').val() ==""){
    alert("you must provide a password for admin");
  }
   else if($('input[name="phone"]').val() ==""){
    alert("you must provide a phone number");
  }
   else if($('input[name="address"]').val() ==""){
    alert("you must provide an address");
  }
   else if($('input[name="password"]').val() ==""){
    alert("you must provide a password");
  }
   else if($('input[name="confirmation"]').val() ==""){
    alert("you must provide a password");
  }
   else if($('input[name="admin_confirmation"]').val() ==""){
    alert("you must provide a password");
  }
   else if($('input[name="ca_max"]').val() ==""){
    alert("ca will be marked over?");
  } 
  else if($('input[name="test_max"]').val() ==""){
    alert("test will be marked over?");
  }
  else if($('input[name="exam_max"]').val() ==""){
    alert("exam will be marked over");
  }
  else if((parseInt($('input[name="exam_max"]').val(), 10)+parseInt($('input[name="ca_max"]').val(), 10) + parseInt($('input[name="test_max"]').val(), 10)) != 100 ){
    alert("total score should be 100");
  }
   else if($('input[name="password"]').val() != $('input[name="confirmation"]').val()){
    alert("password and confirmation do not match");
  }
  else if($('input[name="admin_password"]').val() != $('input[name="admin_password_confirmation"]').val()){
    alert("admin password and confirmation do not match");
  }
    else if($('input[name="admin_password"]').val() == $('input[name="password"]').val()){
    alert("your admin password must be different from staff password");
  }
  
  
 else{            
     $("#register").submit();
     
 }
    });
  });
  
  
  




