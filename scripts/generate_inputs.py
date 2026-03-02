import random
import sys


def generate_input_file(
    filepath: str,
    k: int,
    m: int,
    value_range: int = 10,
) -> None:
    """
    Generate a cache simulation input file with randomly created requests.

    The output file follows the required two-line format:

        k m
        r1 r2 r3 ... rm

    Args:
        filepath (str): Path where the generated input file will be saved.
        k (int): Cache capacity.
        m (int): Number of requests to generate.
        value_range (int, optional): Maximum request ID value.
                                     Requests are sampled uniformly from 1 to value_range.
                                     Defaults to 10.
    """
    requests = [random.randint(1, value_range) for _ in range(m)]

    with open(filepath, "w") as f:
        f.write(f"{k} {m}\n")
        f.write(" ".join(str(req) for req in requests))


def main():
    """
    Usage:
        python generate_inputs.py <filename> <k> <m> <value_range>

    Example:
        python generate_inputs.py file1.txt 3 60 10
    """
    if len(sys.argv) != 5:
        print(
            "Usage: python generate_inputs.py <filename> <k> <m> <value_range>",
            file=sys.stderr,
        )
        sys.exit(1)

    filename = sys.argv[1]
    k = int(sys.argv[2])
    m = int(sys.argv[3])
    value_range = int(sys.argv[4])

    random.seed(42)  # reproducibility (optional but recommended)

    generate_input_file(filename, k, m, value_range)


if __name__ == "__main__":
    main()
