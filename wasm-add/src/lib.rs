use std::ffi::{CStr, CString};
use std::mem;
use std::str;
use std::os::raw::{c_char, c_void};
use serde::{Deserialize, Serialize};

#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[no_mangle]
pub extern fn allocate(size: usize) -> *mut c_void {
    let mut buffer = Vec::with_capacity(size);
    let pointer = buffer.as_mut_ptr();
    mem::forget(buffer);

    pointer as *mut c_void
}

#[no_mangle]
pub extern fn deallocate(pointer: *mut c_void, capacity: usize) {
    unsafe {
        let _ = Vec::from_raw_parts(pointer, 0, capacity);
    }
}

#[no_mangle]
pub extern fn greet(subject: *mut c_char) -> *mut c_char {
    let subject = unsafe { CStr::from_ptr(subject).to_bytes().to_vec() };
    let mut output = b"Hello, ".to_vec();
    output.extend(&subject);
    output.extend(&[b'!']);

    unsafe { CString::from_vec_unchecked(output) }.into_raw()
}

#[no_mangle]
pub extern fn json_example(input: &mut c_char) -> *mut c_char {
    let subject = unsafe { CStr::from_ptr(input).to_bytes().to_vec() };
    let input = deserialize_input(str::from_utf8(&subject).unwrap());
    let output = get_favourite_food(input);

    let output = serialize_output(&output).as_bytes().to_vec();

    unsafe { CString::from_vec_unchecked(output) }.into_raw()
}

fn get_favourite_food(input: InputStruct) -> OutputStruct {
    OutputStruct {
        name: input.name,
        value: input.value + 1,
        favourite_food: String::from("Beans")
    }
}


#[derive(Debug, Deserialize)]
struct InputStruct {
    name: String,
    value: i32
}

fn deserialize_input(input: &str) -> InputStruct {
    serde_json::from_str(input).unwrap()
}

#[derive(Debug, Serialize)]
struct OutputStruct {
    name: String,
    value: i32,
    favourite_food: String
}

fn serialize_output(output: &OutputStruct) -> String {
    serde_json::to_string(output).unwrap()
}