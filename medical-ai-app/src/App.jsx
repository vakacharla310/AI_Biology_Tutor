import { useState } from "react";
import './App.css';

function App() {
  const [symptom, setSymptom] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = () => {
    const s = symptom.toLowerCase();

    if (s === "fever") {
      setResponse("You may have a fever. Drink plenty of water and rest.");
    } else if (s === "cough") {
      setResponse("You may have a cold or throat infection.");
    } else if (s === "headache") {
      setResponse("You may be dehydrated or stressed. Take rest.");
    } else if (s === "stomach pain") {
  setResponse("It may be indigestion. Drink water and eat light food.");
} else if (s === "cold") {
  setResponse("You may have a common cold. Take rest and stay hydrated.");
} else {
  setResponse("Please consult a doctor for proper diagnosis.");
}
  };

  return (
    <div>
      <h1>🩺 AI Medical Assistant</h1>
      <p>Enter your symptoms and get basic health advice.</p>

      <input
        type="text"
        placeholder="Enter your symptoms..."
        value={symptom}
        onChange={(e) => setSymptom(e.target.value)}
      />

      <button onClick={handleSend}>Send</button>

      <div className="response-box">
  <b>AI Response:</b>
  <p>{response}</p>
</div>
    </div>
  );
}

export default App;