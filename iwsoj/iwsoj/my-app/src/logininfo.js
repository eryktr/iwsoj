import React from 'react'
import axios from 'axios';
class Logininfo extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      username: '',
      password: ''	  
    }
  }
	
  changeHandler = e => {
    this.setState({[e.target.name]: e.target.value})
  }
  
  submitHandler = e => {
    e.preventDefault()
    console.log(this.state)
	axios
      .post('http://localhost:8000/api/token_auth/', this.state)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
	  })
  }
  
  render() {
    const { username, password } = this.state  
    return (  
      <div>  
        <form onSubmit={this.submitHandler}>
          <div>
		    <input type="text" name="username" value={username} onChange={this.changeHandler} />
		  </div>
          <div>
		    <input type="text" name="password" value={password} onChange={this.changeHandler} />
		  </div>
          <button type="submit">Submit</button>
        </form>
      </div>  
    )  
  }  
}  
export default Logininfo