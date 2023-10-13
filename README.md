# wasm-py

This repo contains an example of 
* A Rust library project which compiles to wasm
* A python project which then calls the wasm module using wasmer

To run this
1. Clone the repo
1. Build the Rust project `(cd wasm-add && cargo build --release)`
1. Copy the wasm into the Python project `cp wasm-add/target/wasm32-unknown-unknown/release/wasm_add.wasm adder-py/src/adder_py/resources/adder.wasm`
1. Run the python project tests `(cd adder-py && hatch run test)` 
