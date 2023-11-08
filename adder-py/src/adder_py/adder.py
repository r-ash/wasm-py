from wasmer import engine, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler
from importlib import resources as impresources
from . import resources


def get_wasm_instance(lib):
    wasm_file = (impresources.files(resources) / lib)

    # Create a store. Engines and compilers are explained in other
    # examples.
    store = Store(engine.Universal(Compiler))

    # Let's compile the Wasm module.
    module = Module(
        store,
        wasm_file.open('rb').read())

    # Let's instantiate the module!
    return Instance(module)


def add(a, b):

    instance = get_wasm_instance("adder.wasm")

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


def alloc_input(instance, input):
    ## +1 for terminating C-string
    length_of_input = len(input) + 1

    # Allocate memory for the subject, and get a pointer to it.
    input_pointer = instance.exports.allocate(length_of_input)

    # Write the subject into the memory.
    memory = instance.exports.memory.uint8_view(input_pointer)
    memory[0:length_of_input - 1] = input
    memory[length_of_input] = 0  # C-string terminates by NULL.

    return input_pointer, length_of_input

def read_output_from_pointer(instance, output_pointer):
    # Read the result of the `greet` function.
    memory = instance.exports.memory.uint8_view(output_pointer)
    memory_length = len(memory)

    output = []
    nth = 0

    while nth < memory_length:
        byte = memory[nth]

        if byte == 0:
            break

        output.append(byte)
        nth += 1

    length_of_output = nth

    result = bytes(output).decode()
    return result, length_of_output


def greet():

    instance = get_wasm_instance("adder.wasm")

    subject = bytes('Wasmer 🐍', 'utf-8')
    print(subject)
    input_pointer, length_of_subject = alloc_input(instance, subject)

    # Run the `greet` function. Give the pointer to the subject.
    output_pointer = instance.exports.greet(input_pointer)

    result, length_of_output = read_output_from_pointer(instance,
                                                        output_pointer)

    # Deallocate the subject, and the output.
    instance.exports.deallocate(input_pointer, length_of_subject)
    instance.exports.deallocate(output_pointer, length_of_output)
    return result


def json_example():
    instance = get_wasm_instance("adder.wasm")

    input = bytes('{"name": "Rob", "value": 24}', 'utf-8')
    print(input)
    input_pointer, length_of_subject = alloc_input(instance, input)

    # Run the `json_example` function. Give the pointer to the subject.
    print(instance.exports)
    output_pointer = instance.exports.json_example(input_pointer)

    result, length_of_output = read_output_from_pointer(instance,
                                                        output_pointer)

    # Deallocate the input, and the output.
    instance.exports.deallocate(input_pointer, length_of_subject)
    instance.exports.deallocate(output_pointer, length_of_output)
    return result
