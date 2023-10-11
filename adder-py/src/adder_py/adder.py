from wasmer import engine, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler
from importlib import resources as impresources
from . import resources

def add(a, b):

    wasm_file = (impresources.files(resources) / "adder.wasm")

    # Create a store. Engines and compilers are explained in other
    # examples.
    store = Store(engine.Universal(Compiler))

    # Let's compile the Wasm module.
    module = Module(
        store,
        wasm_file.open('rb').read())

    # Let's instantiate the module!
    instance = Instance(module)

    print(instance.exports)

    # We now have an instance ready to be used.
    #
    # From an `Instance` we can retrieve any exported entities. Each of
    # these entities is covered in others examples.
    #
    # Here we are retrieving the exported function. We won't go into
    # details here as the main focus of this example is to show how to
    # create an instance out of a Wasm module and have basic interactions
    # with it.
    return instance.exports.add(a, b)

