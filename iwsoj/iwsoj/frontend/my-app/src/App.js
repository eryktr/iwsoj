import React from 'react'  
class App extends React.Component {  
  render() {  
    return (

<body>	
  <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
    <header class="masthead mb-auto">
      <div class="inner">
        <h3 class="masthead-brand">iwsoj</h3>
        <nav class="nav nav-masthead justify-content-center">
          <a class="nav-link active" href="#">Home</a>
          <a class="nav-link" href="login.html">Login</a>
          <a class="nav-link" href="register.html">Register</a>
        </nav>
      </div>
    </header>

    <main role="main" class="inner cover">
      <h1 class="cover-heading">Intelligent Web-Based Scalable Online Judge</h1>
      <p class="lead">This project is made for people new to programming to help them understand basics of few chosen languages by using training tasks</p>
      <p class="lead flex-row">
        <a href="logreg" class="btn btn-lg btn-secondary">Login</a>
        <a href="logreg" class="btn btn-lg btn-secondary">Register</a>
      </p>
    </main>

    <footer class="mastfoot mt-auto">
      <div class="inner">
        <p>Iwsoj, developed by <a href="https://github.com/eryktr">eryktr</a>, <a href="https://github.com/drzewiec123">drzewiec123</a>,
           <a href="https://github.com/Rafal1997">Rafal1997</a> and <a href="https://github.com/Sliderro">Sliderro</a>.</p>
      </div>
    </footer>
  </div>
</body>  
    )  
  }  
}  
export default App 