import pygame
import unicodedata
import sys
import string
import random
import json
import difflib
import datetime
import pygame.locals
import os
from PyGameLab.common import Data

class Unicode:
    @staticmethod
    def char(char_name):
        if Data.initialized:
            if char_name in Unicode.key:
                return Unicode.key[char_name]
            else:
                matches = difflib.get_close_matches(
                    char_name, Unicode.key.keys(), n=1)
                if matches:
                    return Unicode.key[matches[0]]
                else:
                    raise ValueError(
                        "No se encontró el carácter Unicode correspondiente.")
        else:
            raise TypeError("PyGameLab no se ha inicializado correctamente.")




class Colors:
    class text:
        RESET = "\033[0m"
        for i in range(256):
            locals()[f"C{i}"] = f"\033[38;5;{i}m"

    class background:
        RESET = "\033[0m"
        for i in range(256):
            locals()[f"C{i}"] = f"\033[48;5;{i}m"

    class styles:
        RESET_ALL = "\033[0m"
        BRIGHT = "\033[1m"
        DIM = "\033[2m"
        ITALIC = "\033[3m"
        UNDERLINE = "\033[4m"
        BLINK = "\033[5m"
        REVERSE = "\033[7m"
        HIDDEN = "\033[8m"