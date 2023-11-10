var isControllerRunning = localStorage.getItem('isControllerRunning') === 'true'; // Nouvelle variable pour stocker l'état du bouton

function toggleState() {
    var nav = document.getElementsByClassName("toggleButton");

    if (isControllerRunning) {
        for (let i = 0; i < nav.length; i++) {
            nav[i].style.backgroundColor = "#4CAF50"; /* Green */
            nav[i].innerHTML = "Play Controlleur";
        }
        isControllerRunning = false;
        sendToggleRequest(false);
    } else {
        for (let i = 0; i < nav.length; i++) {
            nav[i].style.backgroundColor = "#f44336"; /* Red */
            nav[i].innerHTML = "Stop Controlleur";
        }
        isControllerRunning = true;
        sendToggleRequest(true);
    }

    // Enregistrez l'état dans le localStorage
    localStorage.setItem('isControllerRunning', isControllerRunning);
}

function sendToggleRequest(newState) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/toggle", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({"newState": newState}));
}

window.onload = function() {
    var nav = document.getElementsByClassName("toggleButton");

    if (isControllerRunning) {
        for (let i = 0; i < nav.length; i++) {
            nav[i].style.backgroundColor = "#f44336"; /* Red */
            nav[i].innerHTML = "Stop Controlleur";
        }
    } else {
        for (let i = 0; i < nav.length; i++) {
            nav[i].style.backgroundColor = "#4CAF50"; /* Green */
            nav[i].innerHTML = "Play Controlleur";
        }
    }
}