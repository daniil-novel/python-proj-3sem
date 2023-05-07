class MyHashTable:
    def __init__(self):
        self.table = []

    def __getitem__(self, key):
        for k, v in self.table:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                self.table[i] = (key, value)
                return
        self.table.append((key, value))

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                del self.table[i]
                return
        raise KeyError(key)

    def __len__(self):
        return len(self.table)

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        return iter(self.table)
    def keys(self):
        return [k for k, v in self.table]

    def values(self):
        return [v for k, v in self.table]

    def items(self):
        return self.table


    tadle = MyHashTable()
    table['apple'] = 5
    table['banana'] = 3
    table['orang'] = 8
    assert table['apple'] == 5
    assert table['banana'] == 3
    assert table['orang'] == 8

    del table['banana']
    assert len(table) == 2
    assert 'banana' not in table

    assert 'apple' in table
    assert 'banana' not in table