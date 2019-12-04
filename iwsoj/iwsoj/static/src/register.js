var reg = document.querySelector("form")
reg.addEventListener("submit", register)

function register(e) {
    e.preventDefault();

    var pswdInput = document.getElementById("inputPassword");
    var emailInput = document.getElementById("inputEmail");
    var usrInput = document.getElementById("inputUserName");
    var nameInput = document.getElementById("inputFirstName");

    const regEndpoint = "http://127.0.0.1:8000/api/register/"

    var data = {
        username: usrInput.value,
        first_name: nameInput.value,
        email: emailInput.value,
        password: pswdInput.value
    };

    const params = {
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
        method: 'POST'
    };

    fetch(regEndpoint, params).then(res => {
        if (res.ok) {
            alert("Registered");
            document.location.href = "login.html";
        } else
            res.text().then(text => {
                alert(text);
            })
            
    }).catch(
        error => alert("Something went wrong")
    );
}
