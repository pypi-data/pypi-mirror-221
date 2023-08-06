import difflib
from PyGameLab import data

unicode = {}
def init():
   for codepoint in range(0x10000):
      char = chr(codepoint)
      name = name(char, "")
      unicode[name] = char


def char(char_name):
   if char_name in unicode:
      return unicode[char_name]
   else:
      matches = difflib.get_close_matches(char_name, unicode.keys(), n=1)
      if matches:
         return unicode[matches[0]]
      else:
         raise ValueError(
            "No se encontró el carácter Unicode correspondiente.")
