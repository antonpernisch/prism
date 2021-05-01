import re
import sys
import getopt
from colorama import init

from Exceptions import *
from Helpers import *
from Keywords import *


class Runtime:
    def __init__(self):
        self.filepath = ''
        self.filepathreg = re.compile("^(.+)\/([^\/]+)$")
        self.debug = False

    def Main(self, argv):
        try:
            opts, args = getopt.getopt(argv, "h:f:d", ["file="])
        except getopt.GetoptError:
            Print('python3 Prism.py -f <filepath>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                Print('python3 Prism.py -f <filepath>')
                sys.exit()
            elif opt in ("-f", "--file"):
                self.filepath = arg
            elif opt in ("-d", "--debug"):
                self.debug = True
        if not self.filepathreg.search(self.filepath):
            raise InvalidArgsException
        if not self.debug:
            sys.tracebacklimit = 0
        comp = Compiler(self.filepath)
        comp.Compile()


class Compiler:
    def __init__(self, path):
        self.path = path
        self.indentation = 0
        self.vars = {}
        return

    def Compile(self):
        instructions = self.ParseFile()
        lineNum = 0
        prevGroup = 0
        currentGroup = 0
        for line in instructions[:]:
            lineNum += 1
            if self.indentation == 0 and Utility.CountIndent(line) > 0:
                # Indetation wasn't detected yet and we have a chance to set it now
                self.indentation = Utility.CountIndent(line)
            line = line.lstrip()
            if line.startswith("comment: ") or line == "[(0)]":
                continue
            thisindent = Utility.GetIndent(line, lineNum)
            if self.indentation > 0:
                currentGroup = int(thisindent) / self.indentation
            if (self.indentation > 0 and int(thisindent) % self.indentation != 0) or (self.indentation > 0 and currentGroup - prevGroup > 1):
                raise CompilerError(lineNum, "Prism Indentation Error. Your indentation is uneven.\nYou have started using indentation with " + str(
                    self.indentation) + " spaces, but on line " + str(lineNum) + ", you have used indentation with " + thisindent + " spaces.")
            line = line[:-5]
            parsedList = line.split(" ")
            if KeywordParser.GetType(lineNum, parsedList[0]) == "var":
                if Regex.Matches("^\S+ is .+$", line, lineNum):
                    Print("Saving var")
                else:
                    raise CompilerError(
                        lineNum, f"Unexpected statement:\n{line}")
            Print(f"Line {lineNum} has these args: {str(parsedList)}")

    def ParseFile(self):
        try:
            with open(self.path) as file:
                raw = file.read()
                try:
                    parsed = raw.splitlines()
                    for i in range(len(parsed)):
                        parsed[i] += "[(" + \
                            str(Utility.CountIndent(parsed[i])) + ")]"
                    return parsed
                except Exception as e:
                    raise UnspecifiedException(
                        "Unable to parse provided file.\nIt exists and is detectable, just unreadble for compiler. More info:\n" + e)
        except:
            raise FileException


if __name__ == "__main__":
    init(autoreset=True)
    runtime = Runtime()
    runtime.Main(sys.argv[1:])
