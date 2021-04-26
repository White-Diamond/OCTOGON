function renderTime() {

    // Date
    var myDate = new Date();
    var year = myDate.getYear();
    if (year < 1000) {
        year += 1900;
    }
    var day = myDate.getDay();
    var month = myDate.getMonth();
    var daym = myDate.getDate();
    var dayArray = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
    var monthArray = new Array("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",);
    // Date End

    // Time
    var currentTime = new Date();
    var h = currentTime.getHours();
    var m = currentTime.getMinutes();
    var s = currentTime.getSeconds();
    var greet;

    if (h == 24) {
        h = 0;
        greet = "Good Morning\n";
    }

    else if (h < 12) {
        greet = "Good Morning\n";
    }

    else if (h > 11 && h < 16) {
        greet = "Good Afternoon\n";
    }

    else {
        greet = "Good Evening\n";
    }

    if (m < 10) {
        m = "0" + m;
    }

    if (s < 10) {
        s = "0" + s;
    }

    var myClock = document.getElementById("clockDisplay");
    

    // Option 1: Display Full Time
    // myClock.textContent = "" + greet + dayArray[day] + " " + daym + " " + monthArray[month] + ", " + year + " " + h + ":" + m + ":" + s;
    // myClock.innerText = "" + greet + dayArray[day] + " " + daym + " " + monthArray[month] + ", " + year + " " + h + ":" + m + ":" + s;

    // Option 2: Display Date & Time

    //myClock.textContent = "" + greet + daym + " " + monthArray[month] + ", " + year + " " + h + ":" + m;
    //myClock.innerText = "" + greet + daym + " " + monthArray[month] + ", " + year + " " + h + ":" + m;

    // Option 3: Display Only Date 
    myClock.textContent = "" + greet + daym + " " + monthArray[month] + ", " + year;
    myClock.innerText = "" + greet + daym + " " + monthArray[month] + ", " + year;

    // Option 4:

    setTimeout("renderTime()", 1000);
    // Time End
}
renderTime();