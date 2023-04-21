# quickindex
A simple way to index lists in python

![Flake8-&-Build](https://github.com/dbernadett/quickindex/actions/workflows/flake8-and-test.yml/badge.svg)
## Example Usage
### Input
```
from quickindex import TreeIndex
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
age_index = TreeIndex(lambda x: (x["age"], x["last_name"]), lambda x: x["first_name"])
age_index.add_list(data_list)
print(age_index.as_dict())
```
### Output
```
{
    25: {
        'Emmy': ['Davina'],
        'Busch': ['Kondwani']
    },
    32: {
        'Shannon': ['Betty']
    },
    38: {
        'Shannon': ['Claude']
    }
}
```
### Input
```
from quickindex import FlatIndex
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
age_index = FlatIndex(lambda x: (x["age"], x["last_name"]), lambda x: x["first_name"])
age_index.add_list(data_list)
print(age_index.as_dict())
```
### Output
```
{
    (25, 'Emmy'): ['Davina'],
    (25, 'Busch'): ['Kondwani'],
    (32, 'Shannon'): ['Betty'],
    (38, 'Shannon'): ['Claude']
}
```
