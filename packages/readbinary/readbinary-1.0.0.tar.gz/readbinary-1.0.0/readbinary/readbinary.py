class readBinary:
    functions = {}

    @staticmethod
    def definefunc(func_name, binary_string):
        decoded_string = readBinary.decode_binary_string(binary_string)
        readBinary.functions[func_name] = decoded_string

    @staticmethod
    def decode_binary_string(binary_string):
        binary_list = binary_string.split(" ")
        decoded_string = ""
        for binary_char in binary_list:
            decoded_string += chr(int(binary_char, 2))
        return decoded_string

    @staticmethod
    def execfunc(func_name, is_binary, *args):
        if func_name in readBinary.functions:
            func_code = readBinary.functions[func_name]
            if is_binary:
                decoded_args = []
                for arg in args:
                    decoded_args.append(readBinary.decode_binary_string(arg))
                eval(func_code)(*decoded_args)
            else:
                eval(func_code)(*args)
        else:
            raise ValueError("Function '{}' is not defined.".format(func_name))