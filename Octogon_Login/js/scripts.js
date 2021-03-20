const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	e.preventDefault();

	  checkInputsSignUp();
});

function checkInputsSignIn(){
  const emailValue = email.value.trim();
	const passwordValue = password.value.trim();

  if(emailValue === '') {
		setErrorFor(email);
	} else {
		setSuccessFor(email);
	}

	if(passwordValue === '') {
		setErrorFor(password);
	} else {
		setSuccessFor(password);
	}
}

function checkInputsSignUp() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();

	if(usernameValue === '') {
		setErrorFor(username);
	} else {
		setSuccessFor(username);
	}

	if(emailValue === '') {
		setErrorFor(email);
	} else {
		setSuccessFor(email);
	}

	if(passwordValue === '') {
		setErrorFor(password);
	} else {
		setSuccessFor(password);
	}

	if(password2Value === '') {
		setErrorFor(password2);
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2);
	} else{
		setSuccessFor(password2);
	}
}

function setErrorFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control error';
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
