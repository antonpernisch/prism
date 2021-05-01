from colorama import init, Fore, Back, Style
init(autoreset=True)


class InvalidArgsException(Exception):
    def __init__(self):
        super().__init__(Back.RED + Fore.WHITE + "Invalid arguments provided")


class FileException(Exception):
    def __init__(self):
        super().__init__(Back.RED + Fore.WHITE + "Couldn't read provided file")


class UnspecifiedException(Exception):
    def __init__(self, mess="Something went wrong, but we don't know what..."):
        super().__init__(Back.RED + Fore.WHITE + mess)


class CompilerError(Exception):
    def __init__(self, line, mess):
        super().__init__(Back.RED + Fore.WHITE +
                         "Prism excpetion on line " + str(line) + ":\n" + mess)
