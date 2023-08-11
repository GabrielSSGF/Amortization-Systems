import Form from "./components/forms/form";

import { useState } from "react";
import { invoke } from "@tauri-apps/api/tauri";
import "./App.css";

function App() {
  const [greetMsg, setGreetMsg] = useState("");
  const [name, setName] = useState("");

  async function greet() {
    // Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
    setGreetMsg(await invoke("greet", { name }));
  }

  async function callRustFunction() {
    const dados_financiamento = {
      periodo: 10,
      saldo: 10000,
      taxajuros: 0.05
      // Add other required fields for the SAC function
    };
  
    try {
      // Call the Rust function with the JavaScript object as an argument
      const result = await invoke('sac', dados_financiamento);
      console.log('Result from Rust:', result);
      // Handle the result from Rust
    } catch (e) {
      console.error('Error calling Rust function:', e);
      // Handle the error
    }
  }
  
  // Call the Rust function when needed
  callRustFunction();

  return (
    <div className="container">
      <Form />
    </div>
  );
}

export default App;
