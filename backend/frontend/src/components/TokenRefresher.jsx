import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import axios from 'axios';
function TokenRefresher() {
  const navigate = useNavigate();



  const changeTokens = async () => {
    try {
      const response = await axios.post("http://localhost:8000/api/token/refresh/", { refresh: localStorage.getItem("refresh") });
      if (response.status !== 200) {
        localStorage.removeItem("access")
        localStorage.removeItem("refresh")
        navigate("/login");
      }
      localStorage.setItem("access", response.data.access);
      localStorage.setItem("refresh", response.data.refresh);
    } catch (e) {
      localStorage.removeItem("access")
      localStorage.removeItem("refresh")
      navigate("/login");
    }
  }
  useEffect(()=>{
    changeTokens();
  },[])

  useEffect(() => {
    changeTokens();
    const interval = 300000; // 2 minutes
    const intervalId = setInterval(changeTokens, interval);
    return () => clearInterval(intervalId);
  }, []);

  return null; // This component does not render anything
}


export default TokenRefresher;
