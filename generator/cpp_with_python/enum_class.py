from generator.cpp_with_python.code import Code
from generator.cpp_with_python.type import Type
from dataclasses import dataclass
from typing import List

@dataclass()
class EnumClass(Type):
    enumerator_list: List[str]
    code: Code

    def declare(self, code: Code):
        code.appendNewLineWithTabs()
        code.code += "enum class " + self.name
        code.appendNewLineWithTabs()
        code.code += "{"
        code.tabs += 1
        for label in self.enumerator_list:
            code.appendNewLineWithTabs()
            code.code += label + ","
        code.code = code.code.rstrip(",")
        code.tabs -= 1
        code.appendNewLineWithTabs()
        code.code += "}"

    def assign(self, value: str, code: Code):
        if value not in self.enumerator_list:
            raise ValueError("Value not in enum")
        code.appendNewLineWithTabs()
        code.code += self.label + " = " + self.name + "::" + value + ";"
