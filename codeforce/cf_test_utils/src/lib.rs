use duct::cmd;
use std::fs;

pub fn run_with_stdin_file(binary_path: &str, stdin_file_path: &str) -> Result<String, Box<dyn std::error::Error>> {
    let stdin_content = fs::read_to_string(stdin_file_path)?;

    let output = cmd!(binary_path)
        .stdin_bytes(stdin_content)
        .read()?;

    let stdout = output;
    Ok(stdout)
}

pub fn run_with_stdin_str(binary_path: &str, stdin_str: &str) -> Result<String, Box<dyn std::error::Error>> {
    let output = cmd!(binary_path)
        .stdin_bytes(stdin_str)
        .read()?;

    let stdout = output;
    Ok(stdout)
}