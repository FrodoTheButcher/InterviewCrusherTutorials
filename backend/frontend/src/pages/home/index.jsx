import axios from 'axios'
import { jwtDecode } from 'jwt-decode'
import React, { useEffect, useState } from 'react'
import { USER_ROLES } from '../../constants'
import User from './subpages/user'
import Manager from './subpages/admin'
import Receptionist from './subpages/receptionist'
import { useNavigate } from 'react-router'

const Home = () => {

    const [user,setUser] = useState()
    useEffect(()=>{
        const accessToken = localStorage.getItem("access")
        if(!accessToken)
            return;
        const decoded = jwtDecode(accessToken)
        const user_id = decoded.user_id
        const role = decoded.role
        console.log("decoded",decoded)
        setUser({
            "user_id":user_id,
            "role":role
        })
    },[])

  if(user?.role === USER_ROLES.USER)
  {
    return (
        <User/>
    )
  }
  else if(user?.role === USER_ROLES.MANAGER)
  {
    return (
        <Manager/>
    )
  }
  else if(user?.role === USER_ROLES.RECEPTIONIST)
    {
      return (
          <Receptionist/>
      )
    }
else{
    return <>nope</>
}
}

export default Home
