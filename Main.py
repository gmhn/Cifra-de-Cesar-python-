## MgzhnSad
start = '''
888b     d888 .d8888b. 8888888888P888    888888b    888
8888b   d8888d88P  Y88b      d88P 888    8888888b   888
88888b.d88888888    888     d88P  888    88888888b  888
888Y88888P888888           d88P   8888888888888Y88b 888
888 Y888P 888888  88888   d88P    888    888888 Y88b888
888  Y8P  888888    888  d88P     888    888888  Y88888
888   "   888Y88b  d88P d88P      888    888888   Y8888
888       888 "Y8888P88d8888888888888    888888    Y888

Code the world
'''
print(start)
msg = ''
def esconde(msg):
    s = ''
    for c in msg: s = s + chr(ord(c) + 30000)
    return s

def mostrar(msg):
    s = ''
    for c in msg: s = s + chr(ord(c) - 30000)
    return s




