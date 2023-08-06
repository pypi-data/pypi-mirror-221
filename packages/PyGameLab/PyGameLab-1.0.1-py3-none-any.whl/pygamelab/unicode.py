import difflib
from PyGameLab import data

key = {}
for codepoint in range(0x10000):
    char = chr(codepoint)
    name = name(char, "")
    key[name] = char


def char(char_name):
    if data.initialized:
      if char_name in key:
         return key[char_name]
      else:
         matches = difflib.get_close_matches(char_name, key.keys(), n=1)
         if matches:
            return key[matches[0]]
         else:
            raise ValueError(
               "No se encontró el carácter Unicode correspondiente.")
    else:
      raise NameError("PyGameLab no se ha inicializado correctamente.")
