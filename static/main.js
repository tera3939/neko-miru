window.addEventListener("load", function () {
    function sendData(form) {
        const button = form.getElementsByClassName("fav_button")[0];
        const url = "./operation/" + button.value;
        const toot_id = button.previousElementSibling.value;

        const XHR = new XMLHttpRequest();
        var FD = new FormData();
        FD.append("toot_id", toot_id);

        XHR.addEventListener("load", function(event) {
            if (button.value === "favorite") {
                button.value = "unfavorite";
            } else {
                button.value = "favorite"
            }
        });

        XHR.addEventListener("error", function(event) {
            console.log(event);
        });

        XHR.open("POST", url);

        XHR.send(FD);
    }
    const fav_form = document.getElementsByClassName("fav");
    for (let i = 0; i < fav_form.length; i++){
        fav_form[i].addEventListener("click", function (event) {
            event.preventDefault();
            sendData(fav_form[i]);
        });
    }
});
