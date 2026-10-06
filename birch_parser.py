# -- coding: utf-8 --

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        program = []
        i = 0

        while i < len(self.tokens):
            token = self.tokens[i]
            line = token["text"]
            indent = token["indent"]

            if line == "birch":
                i += 1
                continue

            # birch set
            if line.startswith("birch set "):
                data = line[10:]

                if "=" in data:
                    name, value = data.split("=", 1)

                    program.append({
                        "type": "set",
                        "name": name.strip(),
                        "value": value.strip()
                    })

                i += 1
                continue

            # birch say
            if line.startswith("birch say "):
                program.append({
                    "type": "say",
                    "value": line[10:].strip()
                })

                i += 1
                continue

            # birch if
            if line.startswith("birch if "):
                condition = line[9:].strip()

                true_command = None
                false_command = None

                i += 1

                # Команда всередині if повинна мати відступ
                if i < len(self.tokens):
                    inside = self.tokens[i]

                    if inside["indent"] > indent:
                        if inside["text"].startswith("birch say "):
                            true_command = {
                                "type": "say",
                                "value": inside["text"][10:].strip()
                            }

                        i += 1

                # else
                if i < len(self.tokens):
                    else_line = self.tokens[i]

                    if else_line["text"] == "birch else":
                        i += 1

                        if i < len(self.tokens):
                            inside_else = self.tokens[i]

                            if inside_else["indent"] > indent:
                                if inside_else["text"].startswith("birch say "):
                                    false_command = {
                                        "type": "say",
                                        "value": inside_else["text"][10:].strip()
                                    }

                                i += 1

                program.append({
                    "type": "if",
                    "condition": condition,
                    "true": true_command,
                    "false": false_command
                })

                continue

            i += 1

        return program