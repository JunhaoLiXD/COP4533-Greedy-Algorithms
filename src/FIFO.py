from typing import List
from collections import deque

def fifo(capacity, m, requests):
    if k <= 0:
        raise ValueError("Cache capacity must be greater than 0.")
    if m != len(requests):
        raise ValueError("Number of requests must match the length of the requests list.")
    
    cache = set()
    queue = deque()
    page_faults = 0

    for r in requests:
        if r not in cache:
            page_faults += 1
            if len(cache) < capacity:
                cache.add(r)
                queue.append(r)
            else:
                oldest = queue.popleft()
                cache.remove(oldest)
                cache.add(r)
                queue.append(r)

    return page_faults