import enum
import re


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for idx, val in enumerate(self.data_map[index]):
                if val[0] == key:
                    return self.data_map[index][idx]
        return None

    def keys(self):
        res = []
        list_keys = [res.extend(i) for i in self.data_map if i is not None]
        tar = [i[0] for i in res]
        return tar



my_hashtable = HashTable()

my_hashtable.set_item('bolts', 1400)
my_hashtable.set_item('washers', 50)
my_hashtable.set_item('lumber', 70)

# print(my_hashtable.get_item('lumber'))
# print(my_hashtable.get_item('bolts'))

print(my_hashtable.keys())

# my_hashtable.print_table()