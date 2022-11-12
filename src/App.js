import './App.css';
import { useState } from 'react';
import axios from 'axios';

function App() {
  const [profileData, setProfileData] = useState(null)
  
  function getData(){
    axios({
      method:"GET", 
      url:"/info",
    }).then((response)=>{
      const res = response.data
      setProfileData(({profile_name: res.name, profile_purpose: res.purpose}))
    }).catch((error) =>{
      if(error.response){
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
      }
    })
  }
  return (
    <div className="App">
       <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {profileData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.profile_purpose}</p>
            </div>
        }
    </div>
  );
}

export default App;
