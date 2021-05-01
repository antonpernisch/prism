import re

from Exceptions import *


class Regex:
    def Extract(pattern, str, group=1, line=0):
        search = re.search(pattern, str, re.IGNORECASE)
        if search:
            try:
                return search.group(group)
            except:
                raise CompilerError(
                    line, "Couldn't read indentation count. This is an internal error and should not happend.\nSend your Prism code to Prism developers.")

    def Matches(pattern, str, line=0):
        try:
            pattern = re.compile(pattern)
            return pattern.search(str)
        except:
            raise CompilerError(
                line, "Couldn't read indentation count. This is an internal error and should not happend.\nSend your Prism code to Prism developers.")
