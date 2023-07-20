// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use pyo3::prelude::*;
use tauri::{Endpoint, Manager, Invoke, Result};

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
use pyo3::prelude::*;
use pyo3::types::IntoPyDict;
use tauri::{Manager, Invoke, Result};

// Implement the SAC Python function as a Rust function
#[tauri::command]
fn sac(dados_financiamento: serde_json::Value) -> Result<serde_json::Value> {
    let gil = Python::acquire_gil();
    let py = gil.python();

    // Convert the JavaScript object to a Python dictionary
    let dict = dados_financiamento.into_py(py);

    // Import the Python script
    let my_script = PyModule::new(py, "Amortizacao").expect("Failed to create Python module");
    let code = include_str!("Amortizacao.py"); // Update the path accordingly
    py.run(code, None, Some(Amortizacao.dict(py)))
        .expect("Failed to run Python script");

    // Call the Python function with the dictionary as an argument
    let df: PyObject = my_script
        .call1("SAC", (dict,))
        .expect("Failed to call Python function")
        .to_object(py);

    // Convert the Python DataFrame to a JSON string
    let json_str = df
        .call_method0(py, "to_json")
        .expect("Failed to convert DataFrame to JSON")
        .extract::<String>()
        .expect("Failed to extract DataFrame JSON");

    // Convert the JSON string to a serde_json::Value
    let json_value: serde_json::Value = serde_json::from_str(&json_str).unwrap();

    Ok(json_value)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![sac])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}