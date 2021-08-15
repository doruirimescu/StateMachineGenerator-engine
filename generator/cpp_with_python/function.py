from logging import BASIC_FORMAT
from generator.cpp_with_python.code import Code
from generator.cpp_with_python.type import Type
from generator.cpp_with_python.comment import *
from dataclasses import dataclass, field
from typing import List


@dataclass()
class Function:
    return_type: str
    name: str
    parameters_list: List[Type]
    body: str = ""
    brief: Brief = None
    parameters: str = field(init=False)

    def __post_init__(self):
        self.parameters = ", ".join([i.asParameter() for i in self.parameters_list])

    def declare(self, code: Code):
        if self.brief is not None:
            self.brief.generate(code)
        code.appendNewLineWithTabs()
        code.code += self.return_type + " " + self.name + "(" + self.parameters+");"
        code.appendNewLineWithTabs()

    def define(self, code: Code, class_name=None):
        if class_name:
            to_append = class_name + "::"
        else:
            to_append = ""

        if self.return_type is not "":
            self.return_type += " "
        code.appendNewLineWithTabs()
        code.code += self.return_type + to_append + self.name + "(" + self.parameters+")"
        code.appendNewLineWithTabs()
        code.code += "{"
        splits = self.body.split("\n")
        code.tabs += 1
        for split in splits:
            code.appendNewLineWithTabs()
            code.code += split
        code.tabs -= 1
        code.appendNewLineWithTabs()
        code.code += "}"
        code.appendNewLineWithTabs()

    def call(self, args: List, code: Code, object_type: Type = None):
        if len(args) != len(self.parameters_list):
            raise ValueError("Wrong number of arguments")
        code.appendNewLineWithTabs()

        if object_type is not None:
            object = object_type.label + "."
        code.code += object + self.name + "(" + ", ".join(args) + ");"
