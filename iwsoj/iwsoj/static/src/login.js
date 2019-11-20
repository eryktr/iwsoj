var reg = document.querySelector("form")
reg.addEventListener("submit", register)

function register(e) {
    e.preventDefault();

    var password = document.getElementById("inputPassword");
    var username = document.getElementById("inputUserName");

    const api = "http://127.0.0.1:8000/api/token_auth/"

    var data = {
        username: username.value,
        password: password.value
    };

    const params = {
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
        method: 'POST'
    };

    fetch(api, params).then(res => {
        if (res.ok) {
            res.text().then(text => {
                var token = JSON.parse(text).token;
                localStorage.setItem('token', token);
                alert("Logged in");
                document.location.href = "tasks.html"
            })
        } else
            res.text().then(text => {
                alert(text);
            })
            
    }).catch(
        error => alert("Doesn't work2")
    );
}