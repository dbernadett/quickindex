import copy

def _add_recursive(path, dict, values):
    index = path[0]
    # base_case
    if len(path) == 1:
        if index not in dict:
            dict[index] = []
        dict[index] += values
        return
    # induction_step
    if index not in dict:
        dict[index] = {}
    _add_recursive(path[1:], dict[index], values)


def _flatten_dict_helper(dictionary, path):
    for key, value in dictionary.items():
        if type(key) == tuple:
            current_path = path + key
        else:
            current_path = path + (key,)
        if type(value) == dict:
            yield from _flatten_dict_helper(value, current_path)
        else:
            yield (current_path, value)


class FlatIndex():
    '''A dictionary, where they keys are tuples and values are lists'''
    def __init__(self, index_map_function, value_map_function=lambda x: x):
        self._index_map_function = index_map_function
        self._value_map_function = value_map_function
        self._index = {}

    def add(self, item):
        index = self._index_map_function(item)
        value = self._value_map_function(item)
        if index not in self._index:
            self._index[index] = []
        self._index[index].append(value)

    def add_list(self, list):
        for item in list:
            self.add(item)

    def to_tree_index(self, index_to_path_function):
        def item_to_path(item):
            return index_to_path_function(self._index_map_function(item))
        result = TreeIndex(item_to_path, self._value_map_function)
        for index, values in self._index.items():
            path = index_to_path_function(index)
            _add_recursive(path, result._index, values)
        return result

    def diff(self, flat_index_b):
        dict_a = self._index
        dict_b = flat_index_b._index
        only_a = {}
        common = {}
        only_b = {}
        for key, value in dict_a.items():
            if key in dict_b:
                common[key] = value
            else:
                only_a[key] = value
        for key, value in dict_b.items():
            if key in dict_a:
                continue
            only_b[key] = value
        return only_a, common, only_b

    def remove(self, item):
        path = self._index_map_function(item)
        value = self._value_map_function(item)
        self._index[path].remove(value)

    def items(self):
        return self._index.items()
    
    def as_dict(self):
        return copy.copy(self._index)

    def __getitem__(self, index):
        return self._index[index]

    def __contains__(self, index):
        return index in self._index

    def __delitem__(self, index):
        del self._index[index]


class TreeIndex():
    '''A tree, where nodes are dictionaries and leaves are lists'''
    def __init__(self, path_map_function, value_map_function=lambda x: x):
        self._path_map_function = path_map_function
        self._value_map_function = value_map_function
        self._index = {}

    def add(self, item):
        path = self._path_map_function(item)
        value = self._value_map_function(item)
        _add_recursive(path, self._index, [value])

    def add_list(self, list):
        for item in list:
            path = self._path_map_function(item)
            value = self._value_map_function(item)
            _add_recursive(path, self._index, [value])

    def remove(self, item):
        path = self._path_map_function(item)
        value = self._value_map_function(item)
        dict = self._index
        for current in path:
            dict = dict[current]
        list = dict
        list.remove(value)

    def flatten(self):
        items = [bin for bin in _flatten_dict_helper(self._index, ())]
        return dict(items)

    def as_dict(self):
        return copy.copy(self._index)

    def items(self):
        return self._index.items()

    def __getitem__(self, index):
        return self._index[index]

    def __contains__(self, index):
        return index in self._index

    def __delitem__(self, index):
        del self._index[index]