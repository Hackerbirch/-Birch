# -- coding: utf-8 --

class Interpreter:
    def __init__(self, runtime):
        self.runtime = runtime

    def get_value(self, value):
        value = value.strip()

        if value in self.runtime.variables:
            return self.runtime.get_variable(value)

        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]

        try:
            return int(value)
        except ValueError:
            return value

    def check_condition(self, condition):
        operators = [">=", "<=", "==", "!=", ">", "<"]

        for operator in operators:
            if operator in condition:
                left, right = condition.split(operator, 1)

                left = self.get_value(left)
                right = self.get_value(right)

                if operator == ">=":
                    return left >= right

                if operator == "<=":
                    return left <= right

                if operator == "==":
                    return left == right

                if operator == "!=":
                    return left != right

                if operator == ">":
                    return left > right

                if operator == "<":
                    return left < right

        return False

    def run_command(self, command):
        if command is None:
            return

        if command["type"] == "say":
            print(self.get_value(command["value"]))

    def run(self, program):
        for command in program:

            if command["type"] == "set":
                value = self.get_value(command["value"])

                self.runtime.set_variable(
                    command["name"],
                    value
                )

            elif command["type"] == "say":
                self.run_command(command)

            elif command["type"] == "if":
                if self.check_condition(command["condition"]):
                    self.run_command(command["true"])
                else:
                    self.run_command(command["false"])