import unittest
from ..src.easy_index_convict626.easy_index import TreeIndex, FlatIndex

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

if __name__ == '__main__':
    unittest.main()
