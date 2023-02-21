import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.quickindex.quickindex import TreeIndex, FlatIndex

data_list = [
            {
                "first_name": "Davina",
                "last_name": "Emmy",
                "age": 25
            },
            {
                "first_name": "Kondwani",
                "last_name": "Busch",
                "age": 25
            },
            {
                "first_name": "Betty",
                "last_name": "Shannon",
                "age": 32
            },
            {
                "first_name": "Claude",
                "last_name": "Shannon",
                "age": 38
            }
        ]

class TestTreeIndex(unittest.TestCase):
    def test_1_level_index(self):
        age_index = TreeIndex(lambda x: (x["age"],), lambda x: x["first_name"])
        age_index.add_list(data_list)
        target_index = {
            25: ["Davina", "Kondwani"],
            32: ["Betty"],
            38: ["Claude"],
        }
        self.assertEqual(age_index._index, target_index)
    def test_2_level_index(self):
        age_index = TreeIndex(lambda x: (x["age"], x["last_name"]), lambda x: x["first_name"])
        age_index.add_list(data_list)
        target_index = {
            25: {
                "Emmy": ["Davina"],
                "Busch": ["Kondwani"]
            },
            32: {
                "Shannon": ["Betty"],
            },
            38: {
                "Shannon": ["Claude"]
            }
        }
        self.assertEqual(age_index._index, target_index)

class TestFlatIndex(unittest.TestCase):
    def test_1_level_index(self):
        age_index = FlatIndex(lambda x: (x["age"],), lambda x: x["first_name"])
        age_index.add_list(data_list)
        target_index = {
            (25,): ["Davina", "Kondwani"],
            (32,): ["Betty"],
            (38,): ["Claude"],
        }
        self.assertEqual(age_index._index, target_index)
    def test_2_level_index(self):
        age_index = FlatIndex(lambda x: (x["age"], x["last_name"]), lambda x: x["first_name"])
        age_index.add_list(data_list)
        target_index = {
            (25, "Emmy"): ["Davina"],
            (25, "Busch"): ["Kondwani"],
            (32, "Shannon"): ["Betty"],
            (38, "Shannon"): ["Claude"]
        }
        self.assertEqual(age_index._index, target_index)
    def test_2_level_index(self):
        modified_list = data_list[1:]
        modified_list.append({"first_name": "Phillip", "age":32, "last_name":"Fry"})
        index_1 = FlatIndex(lambda x: (x["last_name"],), lambda x: x["first_name"])
        index_1.add_list(data_list)
        index_2 = FlatIndex(lambda x: (x["last_name"],), lambda x: x["first_name"])
        index_2.add_list(modified_list)
        only_1, common, only_2 = index_1.diff(index_2)
        assert(set(only_1.keys()) == set([("Emmy",)]))
        assert(set(common.keys()) == set([("Busch",), ("Shannon",)]))
        assert(set(only_2.keys()) == set([("Fry",)]))

if __name__ == '__main__':
    unittest.main()
