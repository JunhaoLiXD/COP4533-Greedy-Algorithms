from typing import List, Tuple

def read_input_file(filepath: str) -> Tuple[int, int, List[int]]:
    """
    Read cache simulation input data from a file.

    The input file must contain exactly two lines with the format:

        k m
        r1 r2 r3 ... rm

    Args:
        filepath (str): Path to the input file.

    Raises:
        ValueError: If the first line does not contain exactly two integers.
        ValueError: If the number of requests does not match m.
        FileNotFoundError: If the file cannot be opened.

    Returns:
        Tuple[int, int, List[int]]: A tuple containing:
                                        k (int): cache capacity,
                                        m (int): number of requests,
                                        requests (List[int]): list of request IDs.
    """
    try:
        with open(filepath, "r") as f:
            # Read first line: k m
            first_line = f.readline().strip().split()
            if len(first_line) != 2:
                raise ValueError("First line must contain exactly two integers: k m")
            k = int(first_line[0])
            m = int(first_line[1])

            # Read second line: requests
            second_line = f.readline().strip().split()
            requests = [int(req) for req in second_line]

        if len(requests) != m:
            raise ValueError(f"Expected {m} requests, got {len(requests)}")
        
        return k, m, requests

    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot open file: {filepath}")
    