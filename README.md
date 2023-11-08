# wasm-py

This repo contains an example of 
* A Rust library project which compiles to wasm
* A python project which then calls the wasm module using wasmer

To run this
1. Clone the repo
1. Build the Rust project `(cd wasm-add && cargo build --release)`. If this is your first time building wasm from Rust you'll also need to run `rustup target add wasm32-unknown-unknown`
1. Copy the wasm into the Python project `cp wasm-add/target/wasm32-unknown-unknown/release/wasm_add.wasm adder-py/src/adder_py/resources/adder.wasm`
1. Run the python project tests `(cd adder-py && hatch run test)`

This contains an example of a library which exposes 4 functions
* Add function which just adds 2 numbers together
* A function for allocating memory in WebAssembly's linear memory
* A function for deallocating memory in WebAssembly's linear memory
* A greet function

This shows an example of how to from python pass in and return a string from a WebAssembly module.  
