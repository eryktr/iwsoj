var reg = document.querySelector("form")
reg.addEventListener("submit", register)

function register(e) {
    e.preventDefault();

    var password = document.getElementById("inputPassword");
    var email = document.getElementById("inputEmail");
    var username = document.getElementById("inputUserName");
    var firstname = document.getElementById("inputFirstName");

    const api = "http://127.0.0.1:8000/api/register/"

    var data = {
        username: username.value,
        first_name: firstname.value,
        email: email.value,
        password: password.value
    };

    const params = {
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
        method: 'POST'
    };

    fetch(api, params).then(res => {
        if (res.ok) {
            alert("Registered");
            document.location.href = "login.html";
        } else
            res.text().then(text => {
                alert(text);
            })
            
    }).catch(
        error => alert("Doesn't work2")
    );
}