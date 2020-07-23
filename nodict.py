#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Trey Dickerson'


class Node:
    def __init__(self, key, value=None):
        """
        set up class object instances
        """
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        """
        make it readable
        """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """
        compare by key
        """
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """
        define variables 
        """
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets
        

    def __repr__(self):
        """
        return a string with NoDict contents
        """
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                        for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """
        Add Node to NoDict
        """
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for i in bucket:
            if i == new_node:
                bucket.remove(i)
                break
        bucket.append(new_node)

    def get(self, key):
        """
        gets specific key and returns value
        """
        key_val = Node(key)
        bucket = self.buckets[key_val.hash % self.size]
        for each in bucket:
            if each == key_val:
                return each.value
        raise KeyError(f'{key} was not found')

    def __getitem__(self, key):
        """
        enables square-bracket behavior
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        returns value from key
        """
        self.add(key, value)
