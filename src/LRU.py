# LRU using double linked list
from typing import List

class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}

        # dummy head and tail
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node): # insert node at tail,  most recently used
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key): # return true is hit, false if miss
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(node)
            return True
        
        # if miss
        if len(self.map) == self.capacity:
            # evict least recently used
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]

        # add new node
        new_node = Node(key)
        self._add(new_node)
        self.map[key] = new_node
        return False
    
    
def lru(capacity, m, requests):
    if capacity <= 0:
        raise ValueError("Cache capacity must be greater than 0.")
    if m != len(requests):
        raise ValueError("Number of requests must match the length of the requests list.")
    
    cache = LRUCache(capacity)
    page_faults = 0

    for r in requests:
        if not cache.get(r):
            page_faults += 1

    return page_faults