import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MyComponent from './components/MyComponent';

function App() {
  const [data, setData] = useState([]);

  console.log(JSON.stringify(data) + ' - data');

  useEffect(() => {
    getData();
  }, []);

  function getData() {
    // take data from jsonplaceholder
    axios.get('http://127.0.0.1:5000/students').then((res) => {
      setData(res.data);
    });
  }

  return (
    <div className="App">
      <h1>React 18 Alpha - Concurrent Mode</h1>
      <h2>Fetching data from jsonplaceholder</h2>
      <div className="data">
        {data.map((item, index) => ( // map data to display
          <div key={index}>
            <h3>{item.name}</h3> 
            <p>{item.grade}</p>
            <p>{item.age}</p>
          </div>
        ))}
      </div>
      <MyComponent name="eğitim" />
    </div>
  );
}

export default App;
