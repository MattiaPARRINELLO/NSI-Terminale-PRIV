import sys


def print_colored(text, color, end='\n'):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m', 'orange': '\x1b[38;5;208m', 'purple': '\x1b[35m', 'cyan': '\x1b[36m', 'gray': '\x1b[37m'}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get(color, '') + text + reset + end)