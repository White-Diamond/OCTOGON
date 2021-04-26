function checkInputsPswrdRecv(){
  const email = document.getElementById("email");

  // trim to remove the whitespaces
  const emailValue = email.value.trim();

  if(emailValue === "") {
		setErrorFor(email);
	}
  else if(!ValidateEmail(emailValue)){
		setErrorFor(email);
	} else {
    setSuccessFor(email);
  }
}

function checkInputsSignIn(){
  const email = document.getElementById("email");
  const password = document.getElementById("password");

  // trim to remove the whitespaces
  const emailValue = email.value.trim();
	const passwordValue = password.value.trim();

  if(emailValue === "") {
		setErrorFor(email);
	}
  else if(!ValidateEmail(emailValue)){
		setErrorFor(email);
	} else {
    setSuccessFor(email);
  }

	if(passwordValue === "") {
		setErrorFor(password);
	} else {
		setSuccessFor(password);
	}
}

function checkInputsSignUp() {
  const username = document.getElementById("username");
  const email = document.getElementById("email");
  const password = document.getElementById("password");
  const password2 = document.getElementById("password2");

	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();

	if(usernameValue === "") {
		setErrorFor(username);
	} else {
		setSuccessFor(username);
	}

  if(emailValue === "") {
		setErrorFor(email);
	}
  else if(!ValidateEmail(emailValue)){
		setErrorFor(email);
	} else {
    setSuccessFor(email);
  }

	if(passwordValue === "") {
		setErrorFor(password);
	} else {
		setSuccessFor(password);
	}

	if(password2Value === "") {
		setErrorFor(password2);
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2);
	} else{
		setSuccessFor(password2);
	}
}

function setErrorFor(input) {
	const formControl = input.parentElement;
	formControl.className = "form-control error";
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = "form-control success";
}

function ValidateEmail(inputText) {
  var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

  if(inputText.match(mailformat)){
    return true;
  } else {
    return false;
  }
}
