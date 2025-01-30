import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import axios from 'axios';
function TokenRefresher() {
  const navigate = useNavigate();

 useEffect(()=>{
    console.log("aaa")
 },[])

  const changeTokens = async () => {
    try {
      const response = await axios.post("http://localhost:8000/api/token/refresh/", { refresh: localStorage.getItem("refresh") });
      if (response.status !== 200) {
        navigate("/login");
      }
      localStorage.setItem("access", response.data.access);
      localStorage.setItem("refresh", response.data.refresh);
    } catch (e) {
      navigate("/login");
    }
  }

  useEffect(() => {
    changeTokens();
    const interval = 300000; // 5 minutes
    const intervalId = setInterval(changeTokens, interval);
    return () => clearInterval(intervalId);
  }, []);

  return null; // This component does not render anything
}


export default TokenRefresher;
