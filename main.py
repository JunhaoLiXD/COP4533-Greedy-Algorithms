import sys

from src.io_utils import read_input_file, write_output_file

from src.OPTFF import optff
# from src.FIFO import fifo
# from src.LRU import lru

def main() -> None:
    """
    Driver program:
    - parse input file
    - run FIFO / LRU / OPTFF
    - print misses in required format
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read input
    k, m, requests = read_input_file(input_file)

    # Run algorithms
    # fifo_misses = fifo(k, m, requests)
    # lru_misses = lru(k, m, requests)
    optff_misses = optff(k, m, requests)

    # Print the output (Optional)
    # print(f"FIFO : {fifo_misses}")
    # print(f"LRU : {lru_misses}")
    print(f"OPTFF : {optff_misses}")

    # Write output file
    write_output_file(
        output_file,
        fifo_misses=None,
        lru_misses=None,
        optff_misses=optff_misses,
    )

if __name__ == "__main__":
    main()
