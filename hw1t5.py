class Calculator(object):
    def evaluate(self, string):
        operands = {'+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y
                    }

        listofsymbols = string.split(" ")

        while True:
            for index, symbol in enumerate(listofsymbols):
                if symbol == "/" or symbol == "*":
                    listofsymbols[index - 1] = operands[symbol](float(listofsymbols[index - 1]), float(listofsymbols[index + 1]))
                    listofsymbols.pop(index)
                    listofsymbols.pop(index)
                    break
            else:
                break

        while True:
            for index, symbol in enumerate(listofsymbols):
                if symbol == "+" or symbol == "-":
                    listofsymbols[index - 1: index + 2] = operands[symbol](float(listofsymbols[index - 1]), float(listofsymbols[index + 1]))
                    listofsymbols.pop(index)
                    listofsymbols.pop(index)
                    break
            else:
                break

        return listofsymbols
