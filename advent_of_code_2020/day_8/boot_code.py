class BootCode:
    def __init__(self, input_code):
        self.input_code = input_code
        self.accumulator = 0
        self.code = []
        self.terminated = False

        for instruction in input_code:
            operation = instruction.split(" ")[0]
            argument = instruction.split(" ")[1]
            sign = argument[0]
            number = int(argument[1:].replace("\n", ""))
            executed = False
            self.code.append([operation, sign, number, executed])

    def run(self):
        instruction = 0
        executed = False

        while not executed:
            executed = self.code[instruction][3]
            if executed:
                break

            self.code[instruction][3] = True

            operation = self.code[instruction][0]
            sign = self.code[instruction][1]
            number = self.code[instruction][2]

            if operation == "nop":
                instruction += 1
            elif operation == "jmp":
                if sign == "+":
                    instruction += number
                else:
                    instruction -= number
            else:
                if sign == "+":
                    self.accumulator += number
                else:
                    self.accumulator -= number
                instruction += 1

            if instruction >= len(self.code):
                self.terminated = True
                break

    def modified_run(self):
        self.run()

        if self.terminated:
            return

        for instruction in range(len(self.code)):
            if self.code[instruction][0] == "acc":
                continue

            modified_code = BootCode(self.input_code)
            if (
                modified_code.code[instruction][0] == "nop"
                and modified_code.code[instruction][2] != 0
            ):
                modified_code.code[instruction][0] = "jmp"
            elif modified_code.code[instruction][0] == "jmp":
                modified_code.code[instruction][0] = "nop"

            modified_code.run()

            if modified_code.terminated:
                return modified_code.accumulator
