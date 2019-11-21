var reg = document.querySelector("form")
reg.addEventListener("submit", register)

function register(e) {
    e.preventDefault();

    var pswdInput = document.getElementById("inputPassword");
    var usrInput = document.getElementById("inputUserName");

    const loginEndpoint = "http://127.0.0.1:8000/api/token_auth/"

    var data = {
        username: pswdInput.value,
        password: usrInput.value
    };

    const params = {
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
        method: 'POST'
    };

    fetch(loginEndpoint, params).then(res => {
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
        error => alert("Something went wrong")
    );
}
