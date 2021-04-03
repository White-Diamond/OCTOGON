const chai = window.chai;
const expect = chai.expect;

var formControl;

var err_msg = "form-control error";

/* password recovery test */
describe("checkInputsPswrdRecv", () =>{
    it("Function should properly check the pswrd recovery input", () =>{
        checkInputsPswrdRecv();
        /* email */
        const email = document.getElementById("email");
        formControl = email.parentElement;
        expect(formControl.className).to.equal(err_msg);
    })
})

/* sign in test */
describe("checkInputsSignIn", () =>{
    it("Function should properly check the sign-in inputs", () =>{
        checkInputsSignIn();
        /* email */
        const email = document.getElementById("email");
        formControl = email.parentElement;
        expect(formControl.className).to.equal(err_msg);

        /* passwrd */
        const passwrd = document.getElementById("password");
        formControl = passwrd.parentElement;
        expect(formControl.className).to.equal(err_msg);
    })
})

/* sign up test */
describe("checkInputsSignUp", () =>{
    it("Function should properly check the sign-up inputs", () =>{
        checkInputsSignUp();
        /* username */
        const usrname = document.getElementById("username");
        formControl = usrname.parentElement;
        expect(formControl.className).to.equal(err_msg);

        /* email */
        const email = document.getElementById("email");
        formControl = email.parentElement;
        expect(formControl.className).to.equal(err_msg);

        /* passwrd */
        const passwrd = document.getElementById("password");
        formControl = passwrd.parentElement;
        expect(formControl.className).to.equal(err_msg);

        /* passwrd 2 */
        const passwrd2 = document.getElementById("password2");
        formControl = passwrd2.parentElement;
        expect(formControl.className).to.equal(err_msg);
    })
})
