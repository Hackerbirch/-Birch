# -- coding: utf-8 --

class Lexer:
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = []

        for line in self.text.splitlines():
            if not line.strip():
                continue

            spaces = len(line) - len(line.lstrip(" "))

            tokens.append({
                "indent": spaces,
                "text": line.strip()
            })

        return tokens