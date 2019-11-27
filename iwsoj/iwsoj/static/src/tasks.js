var tasks;
var sender;

function getAllTasks() {

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
                tasks = JSON.parse(text);
                insertTasks();
            })
        } else
            res.text().then(text => {
                alert("Unauthorized");
            })

    }).catch(
        error => alert("Something went wrong")
    );
}

function insertTasks() {
    var titles = '<table><tr><th>LP</th><th>Task</th><th>C</th><th>C++</th><th>GO</th><th>Python</th><th>Java</th></tr>';
    for (const task of tasks) {
        titles += '<tr><th>'+ task.id + '</th><th>' + task.title + '</th>';
        titles += '<th><a href="javascript:showSingleTask(' + task.id + ', \'C\')">C</a></th>';
        titles += '<th><a href="javascript:showSingleTask(' + task.id + ', \'C++\')">C++</a></th>';
        titles += '<th><a href="javascript:showSingleTask(' + task.id + ', \'GO\')">GO</a></th>';
        titles += '<th><a href="javascript:showSingleTask(' + task.id + ', \'Python\')">Python</a></th>';
        titles += '<th><a href="javascript:showSingleTask(' + task.id + ', \'Java\')">Java</a></th></tr>';
    }
    titles += '</table>'
    document.getElementById("tasks").innerHTML = titles;
    document.getElementById("sender").innerHTML = '';
}

function showSingleTask(n, lang) {
    localStorage.setItem('task_id', n);
    localStorage.setItem('task_lang', lang);
    var task = tasks[n-1];
    var idHTML = '<h3>' + task.id;
    var titleHTML = '. ' + task.title + '</h3>';
    var backButtonHTML = '<a href="javascript:insertTasks()">back</a>';
    var statementHTML = '<p>' + task.statement; + '</p>'
    var formHTML = '<textarea id="codeArea"></textarea><input type="submit" value="Submit">'
    document.getElementById("tasks").innerHTML = idHTML + titleHTML + backButtonHTML + statementHTML;
    document.getElementById("sender").innerHTML = formHTML;
    sender = document.querySelector("form");
    sender.addEventListener("submit", sendTask);
}

function sendTask(e) {
    e.preventDefault();

    var task_id = localStorage.getItem('task_id');
    var task_lang = localStorage.getItem('task_lang');
    var codeInput = document.getElementById("codeArea").value;

    var data = {
        sourceCode: codeInput,
        task: task_id,
        language: task_lang
    };

    var token = "Bearer " + localStorage.getItem('token');
    const submissionEndpoint = "http://127.0.0.1:8000/api/submissions/";

    const params = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        },
        body : JSON.stringify(data),
        method: 'POST'
    };
    console.log(JSON.stringify(data));
    fetch(submissionEndpoint, params).then(res =>{
        if (res.ok){
            res.text().then(text => {
                var info = JSON.parse(text);
                alert(info.status + '\n' + info.error);
            });
        }
        else {
            alert("Unauthorized");
        }
    }).catch(
        error => alert("Something went wrong")
    );
}