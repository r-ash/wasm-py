# wasm-add

To build

```
cargo build --release
```

To run compiled wasm code via wasmer on command line, you will need [wasmer CLI](https://docs.wasmer.io/install) installed

```
wasmer run target/wasm32-unknown-unknown/release/wasm_add.wasm --command-name=add 2 3
```

Should print 5
