function getTasks(n){

    const taskEndpoint = "http://127.0.0.1:8000/api/tasks/"
    var token = "Bearer " + localStorage.getItem('token');
    const params = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        },
        method: 'GET'
    };
    
    fetch(taskEndpoint, params).then(res => {
        if (res.ok) {
            res.text().then(text => {
                var tasks = JSON.parse(text);
                document.getElementById("title").innerHTML = tasks[n].title;
                document.getElementById("statement").innerHTML = tasks[n].statement;
            })
        } else
            res.text().then(text => {
                alert("Unauthorized");
            })
            
    }).catch(
        error => alert("Something went wrong")
    );
}
