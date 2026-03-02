from typing import List, Tuple, Optional

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


def write_output_file(
    filepath: str,
    fifo_misses: Optional[int],
    lru_misses: Optional[int],
    optff_misses: Optional[int],
) -> None:
    """
    Write cache miss results to an output file using the required format.

    Args:
        filepath (str): Path to the output file.
        fifo_misses (Optional[int]): Number of cache misses produced by the 
                                     FIFO policy. If None, the FIFO result is not written.
        lru_misses (Optional[int]): Number of cache misses produced by the 
                                    LRU policy. If None, the LRU result is not written.
        optff_misses (Optional[int]): Number of cache misses produced by the 
                                      OPTFF policy. If None, the OPTFF result is not written.

    Output format:
        FIFO : <number_of_misses>
        LRU  : <number_of_misses>
        OPTFF: <number_of_misses>
    """
    with open(filepath, "w") as f:
        if fifo_misses is not None:
            f.write(f"FIFO : {fifo_misses}\n")

        if lru_misses is not None:
            f.write(f"LRU  : {lru_misses}\n")

        if optff_misses is not None:
            f.write(f"OPTFF: {optff_misses}\n")