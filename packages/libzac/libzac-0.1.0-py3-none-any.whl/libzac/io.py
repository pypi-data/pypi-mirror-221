import os
import re
import numpy as np
np.set_printoptions(threshold=999999)

def c2np(filename):
    """
    parse c array from file to numpy array
    
    WARNING: this function use `eval()` so not secure, do not use it on untrusted file
    """
    with open(filename,'r') as f:
        raw = f.read()
    dtype_dict = {
        'float':            np.float32,
        'double':           np.float64,

        'unsigned char':    np.uint8,
        'uint8_t':          np.uint8,
        'char':             np.int8,
        'int8_t':           np.int8,

        'unsigned short':   np.uint16,
        'uint16_t':         np.uint16,
        'short':            np.int16,
        'int16_t':          np.int16,
        
        'unsigned int':     np.uint32,
        'uint32_t':         np.uint32,
        'int':              np.int32,
        'int32_t':          np.int32,
    }
    regex = "((?:"+")|(?:".join(list(dtype_dict.keys()))+"))" + r"\s*(\w*)(\[.*\])\s*=\s*(\{[\s\S]*?\});"
    match = re.findall(regex, raw)
    array_dict = {}
    for group in match:
        dtype = dtype_dict[group[0]]
        array_name = group[1]
        data_str = group[3].replace("{","[").replace("}",']')   # change c array {} to python list []
        clean_str = re.sub("\/\/[\S\s]*?\\n", '', data_str)    # remove comment //
        clean_str = re.sub("\/\*[\S\s]*?\*\/",'', clean_str)   # remove comment /* */
        try:
            data = eval(clean_str) # this is not secure but i dont care
        except Exception as error:
            print(f"parse {array_name} error: ",error)
        array = np.array(data).astype(dtype)
        array_dict[array_name] = array
    return array_dict

def np2c(np_dict_array, filename, addition="", const=True, formatter={"float_kind":lambda f:f"{f:f}f"}, **kwargs):
    """write numpy array to `<filename>.h` as c array format"""
    filename = os.path.splitext(filename)[0]
    filename_no_ext = os.path.split(filename)[1]
    with open(filename+".h", "w") as f:
        const = "const " if const else "" 
        f.write(f"#ifndef __{filename_no_ext}__\n#define __{filename_no_ext}__\n#include <stdint.h>\n\n")        
        f.write(addition)        
        for array_name,array in np_dict_array.items():
            dtype = array.dtype
            if np.issubdtype(dtype, np.floating):
                dtype_name = "float" if dtype.itemsize == 4 else "double"
            elif np.issubdtype(dtype, np.integer):
                dtype_name = f"{np.dtype(dtype).base.name}_t"
            else:
                raise TypeError(f"unsupported dtype {dtype} for {array_name}")
            f.write(f"{const}{dtype_name} {array_name}[{array.size}] = {{\n ")
            array_str = np.array2string(array, separator=",", formatter = formatter, **kwargs)[1:-1] # remove []
            f.write(array_str)
            f.write("\n};\n\n")
        f.write(f"\n#endif /* __{filename_no_ext}__ */")           

def file2c(filename_in, filename_out, array_name, dtype=np.uint8, pad_tail=False, **kwargs):
    """read file to byte array then to numpy array with dtype, kwargs pass to np2c"""
    with open(filename_in, "rb") as f:
        raw_byte = f.read()
    byte2c(raw_byte, filename_out, array_name, dtype, pad_tail, **kwargs)

def byte2c(byte, filename, array_name="byte_buf", dtype=np.uint8, pad_tail=False, **kwargs):
    """convert byte array to numpy array with dtype then write to `<filename>.h` as c array format, kwargs pass to np2c"""
    dtype = np.dtype(dtype)
    size = dtype.itemsize
    if len(byte)%size != 0:
        print(f"WARNING: byte size {len(byte)} is not multiple of {size}, ", end="")
        if pad_tail:
            print(f"pad last {size-len(byte)%size} byte")
            byte = byte + b'\x00'*(size-len(byte)%size)
        else:
            print(f"remove last {len(byte)%size} byte")
            byte = byte[:len(byte)//size*size]
    array = np.frombuffer(byte, dtype=dtype)
    np2c({array_name:array}, filename, **kwargs)