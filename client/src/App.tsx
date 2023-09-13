import { useState, useEffect } from "react";

import "./app.css";

export default function App() {
  const [items, setItems] = useState([{}]);

  useEffect(() => {
    fetch("/items")
      .then((res) => res.json())
      .then((data) => {
        setItems(data);
        console.log(data);
      });
  }, []);

  return <div>{JSON.stringify(items)}</div>;
}
