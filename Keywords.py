class KeywordParser:
    def GetType(line, word):
        keyw = ["if", "else", "message"]
        if word in keyw:
            return "key"
        else:
            return "var"
