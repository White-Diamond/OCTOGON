const form = document.getElementById('form');
const email = document.getElementById('email');


form.addEventListener('submit', e => {
	e.preventDefault();

	  checkInputsSignUp();
});


function checkInputsSignUp() {
	// trim to remove the whitespaces
	const emailValue = email.value.trim();

	if(emailValue === '') {
		setErrorFor(email);
	} else {
		setSuccessFor(email);
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
