// Export a function named "hello_wasm". This can be called
// from the embedder!
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}

