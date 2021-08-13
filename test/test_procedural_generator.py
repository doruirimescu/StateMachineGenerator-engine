import unittest
from blueprint import blueprint
from generator.procedural.procedural_generator import ProceduralGenerator




class TestProceduralGenerator(unittest.TestCase):
    def compareFiles(self, filepath_1, filepath_2):
        f = open(filepath_1, "r+")
        data_1 = f.read()
        f.close()

        f = open(filepath_2, "r+")
        data_2 = f.read()
        f.close()

        self.assertEqual(data_1, data_2)

    def test_ProceduralGeneratorHeader(self):
        test_path = "test/test_files/procedural/header.h"
        generated_path = "generated/procedural/header.h"
        self.compareFiles(test_path, generated_path)

    def test_ProceduralGeneratorSource(self):
        test_path = "test/test_files/procedural/source.cpp"
        generated_path = "generated/procedural/source.cpp"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateHeader(self):
        test_path = "test/test_files/oop/state.h"
        generated_path = "generated/oop/state.h"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateSource(self):
        test_path = "test/test_files/oop/state.cpp"
        generated_path = "generated/oop/state.cpp"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateMachineHeader(self):
        test_path = "test/test_files/oop/state_machine.h"
        generated_path = "generated/oop/state_machine.h"
        self.compareFiles(test_path, generated_path)

    def test_OopGeneratorStateMachineSource(self):
        test_path = "test/test_files/oop/state_machine.cpp"
        generated_path = "generated/oop/state_machine.cpp"
        self.compareFiles(test_path, generated_path)
