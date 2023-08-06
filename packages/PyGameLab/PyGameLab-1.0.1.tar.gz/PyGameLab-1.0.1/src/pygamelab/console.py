import sys

def log(*values, sep=" "):
   print("\033[0m", *values, "\033[0m", sep=sep, file=sys.stdout)

def warn(*values, sep=" "):
   print("\033[33m", *values, "\033[0m", sep=sep, file=sys.stdout)

def error(*values, sep=" "):
   print("\033[31m", *values, "\033[0m", sep=sep, file=sys.stdout)