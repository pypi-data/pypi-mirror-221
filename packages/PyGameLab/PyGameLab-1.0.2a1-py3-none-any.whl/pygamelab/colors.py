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
