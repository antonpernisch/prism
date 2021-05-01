from Exceptions import *
from Regex import *


class Print:
    def __init__(self, mess):
        print(mess)
        return


class Utility:
    def CountIndent(str):
        return len(str) - len(str.lstrip(' '))

    def GetIndent(instruct, line):
        indentRegex = "(.+)\[\((\d+)\)\]$"
        return Regex.Extract(indentRegex, instruct, 2, line)
