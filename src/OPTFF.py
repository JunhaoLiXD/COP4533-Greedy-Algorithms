from typing import List

def optff(k: int, m: int, requests: List[int]) -> int:
    """
    Simulate the OPTFF (Optimal Farthest-in-Future) cache replacement policy
    and return the total number of cache misses.

    The input parameters correspond to values read from an input file
    with the following format:

        k m
        r1 r2 r3 ... rm

    Args:
        k (int): Cache capacity (maximum number of items the cache can hold).
                 Must be greater than or equal to 1.
        m (int): Total number of requests in the sequence.
        requests (List[int]):  A list representing the request sequence,
                              where each element is an item identifier.

    Raises:
        ValueError: If k <= 0.
        ValueError: If m does not equal len(requests).

    Returns:
        int: The total number of cache misses produced by the OPTFF policy.
    """
    if k <= 0:
        raise ValueError("Cache capacity must be >= 1")
    
    if m != len(requests):
        raise ValueError(f"m must equal len(requests), got m={m}, len={len(requests)}")
    
    cache = set()
    misses = 0

    # Process requests sequentially
    for i, req in enumerate(requests):
        # Cache hit, no action needed
        if req in cache:
            continue

        # Cache miss occuus
        misses += 1

        # (1) Cache not full, insert directly
        if len(cache) < k:
            cache.add(req)
            continue

        # (2) Cache full, apply OPTFF eviction rule
        # Evict the item whose next use is farthest in the future
        evict_item = None
        farthest_next_use = -1

        for item in cache:
            next_use = -1

            # Find next occurrence in the future
            for j in range(i + 1, m):
                if requests[j] == item:
                    next_use = j
                    break

            # If item never appears, evict it
            if next_use == -1:
                evict_item = item
                break

            # Track the item used farthest in the future
            if next_use > farthest_next_use:
                farthest_next_use = next_use
                evict_item = item

        # Evict selected item and insert current request
        cache.remove(evict_item)
        cache.add(req)

    return misses
