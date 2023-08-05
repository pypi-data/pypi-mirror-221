from PyGameLab import common, data, document
import pygame
import unicodedata
import sys


def init():
    global pivot_point
    if not data.initialized:
        pygame.init()
        document.Unicode.key = {}
        for codepoint in range(0x10000):
            char = chr(codepoint)
            name = unicodedata.name(char, "")
            document.Unicode.key[name] = char
        data.initialized = True
        pivot_point = (0, 0)
        print(
            f"\npygamelab {data.version} ({data.interpreter})", file=sys.stdout)
        print("Hello from PyGameLab Services.", file=sys.stdout)
        print(
            f"You are currently using {len(data.dependences)} dependences:", file=sys.stdout)
        print(f"  - {data.dependences_printable}.", file=sys.stdout)
        print("You can visit https://feippe.com/documentation.html for our documentation.\n", file=sys.stdout)
    else:
        print("PyGameLab already initialized.", file=sys.stdout)
