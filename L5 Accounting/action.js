$('.message a').click(function(){
$('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});

// FUNCTION FOR THE LOGIN BUTTON //
function validate(){

	// VARIABLES TO STORE THE USER INPUTS //
	var username = document.getElementById("usn").value;
	var password = document.getElementById("psw").value;

	// CHEKING THE USER INPUT TO SEE IF IT MATCHES //
	if ( username === "Admin" && password === "adminPassword"){

 		// REDIRECTING TO ANOTHER PAGE. //
    	open('mainpage.html');
    	//alert ("Login successfully");
	}
	else{
		alert("wrong password");
    }
}